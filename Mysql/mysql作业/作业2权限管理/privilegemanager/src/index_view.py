# -*- coding: utf-8 -*-
import functools
import pymysql
import hashlib

from ..conf import settings
from .admin import Admin
from .common import Common
from .commfunc import encrypt, decrypt


class IndexPage:
    def __init__(self):

        self.conn,self.cursor = self.connect_mysql()

    def connect_mysql(self):
        conn = pymysql.connect(host=settings.host,
                               user=settings.user,
                               password=settings.password,
                               database=settings.database,
                               charset=settings.charset)
        try:
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        except:
            conn.close()
            raise
        return conn,cursor


    def login(func): # 类中定义装饰器
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # print("""\033[34;1mWelcome to index page of privilege manage system!\n\033[0m""".center(128))
            print("""\033[34;1mPlease input username and password \033[0m""")
            flag = False
            retry_count = 0
            while retry_count < 3:
                username = input('\033[1musername:\033[0m').strip()
                password = input('\033[1mpassword:\033[0m').strip()
                status = self.get_auth_result(username, password)
                if status == '200':
                    flag = True
                    break
                elif status == "404":
                    self.print("password error")
                    choice = input("\033[1mretrieve password, y/n: \033[0m").strip()
                    if choice == 'y':
                        self.retrieve_password(username)
                        print("\033[34;1mlogin again\033[0m")
                else:
                    self.print("%s don't exist, please register" % username)
                    choice = input("\033[1mregister new account, y/n: \033[0m").strip()
                    if choice == 'y':
                        self.register()
                        print("\033[34;1mlogin again\033[0m")

                retry_count += 1

            if flag:
                self.print("login successfully")
                func(self, *args, **kwargs) # 只有鉴权成功才会执行后面的操作
            else:
                exit(0)

        return wrapper

    def get_auth_result(self, username, password):
        # password = self.getmd5(username+password)
        password = encrypt(password)
        sql = "select * from user where uname=%s and password=%s"
        self.cursor.execute(sql,[username,password])
        result = self.cursor.fetchone()
        if not result:
            sql = "select * from user where uname=%s"
            self.cursor.execute(sql, username)
            if self.cursor.fetchall():
                return "404"
            else:
                return "401"
        else:
            self.user_dict = result
            # print(self.user_dict)
            return '200'

    def register(self):
        while True:
            print("\033[34;1mPlease input user information\033[0m")
            name = input("\033[1mname: \033[0m").strip()
            sex = input("\033[1msex: \033[0m").strip()
            email = input("\033[1memail: \033[0m").strip()
            password = input("\033[1mpassword: \033[0m").strip()
            password = encrypt(password)
            sql = "insert into user(uname, sex, email, password) values(%s, %s, %s, %s)"
            try:
                self.cursor.execute(sql, [name, sex, email, password])
            except Exception as e:
                print(e)
                continue
            else:
                self.conn.commit()
                self.print("register successfully")
                break

    def retrieve_password(self, username):
        while True:
            email = input("\033[1mplease input your email: \033[0m").strip()
            sql = "select password from user where uname = %s and email = %s"
            try:
                self.cursor.execute(sql, [username,email])
            except Exception as e:
                print(e)
                continue
            else:
                result = self.cursor.fetchone()
                if result:
                    password = result.get('password')
                    self.print("your password is: " + decrypt(password))
                    break
                else:
                    print("\033[34;1mPlease check your email is right\033[0m")

    def print(self, msg):
        print('\033[;34m%s\033[0m'% msg)


    def initialize_role(self):
        if self.user_dict['role_id'] == 1:
            self.role = Admin(self.user_dict.get('uid'), self.conn)
        else:
            self.role = Common(self.user_dict.get('uid'), self.user_dict.get('uname'), self.conn)


    @login
    def interactive(self):
        self.initialize_role()
        if hasattr(self.role, 'show_privilege'):
            self.role.show_privilege()






