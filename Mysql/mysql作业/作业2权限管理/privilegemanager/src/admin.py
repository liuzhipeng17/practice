# -*- coding: utf-8 -*-

import pymysql
from .commfunc import encrypt


class Admin(object):
    def __init__(self, id, conn):
        self.uid = id
        self.conn = conn

    def show_privilege(self):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = """
            select privilege.pname from role_privilege_relation 
            left join 
                role on role_privilege_relation.rid = role.rid
            left join 
                user on role.rid = user.role_id
            left join
                privilege on privilege.pid = role_privilege_relation.pid
            where user.uid=%s
        """
        cursor.execute(sql,[self.uid])
        result = cursor.fetchall()
        cursor.close()
        if not result:
            return

        print("""\033[34;1mPrivileges your have are as follows \033[0m""")
        while True:
            for d in result:
                self.print("\t" + d.get('pname'))
            choice = input("\033[1mplease select menu(privilege,role,user,q etc): \033[0m").strip()
            if hasattr(self,"%s_manage" % choice):
                func = getattr(self, "%s_manage" % choice)
                func()
            elif choice == 'q':
                self.print("logout")
                break
            else:
                print('\033[34;1mnot permitted\033[0m')

    def role_manage(self):
        while True:
            self.print("""\trole_manage\n\t\tadd\n\t\tview""")
            choice = input('\033[1mPlease select menu(add, view, q): \033[0m').strip()
            if hasattr(self,"%s_role_manage" % choice):
                func = getattr(self, "%s_role_manage" % choice)
                func()
            elif choice == 'q':
                self.print("back to previous menu")
                return
            else:
                print('\033[1mnot permitted\033[0m')

    def add_role_manage(self):
        rname = ''
        # self.print("\trole_manage\t\tadd")
        print("\033[34;1mPlease fill in information\033[0m")
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        while True:
            rname = input("\033[1mrole name: \033[0m").strip()
            sql = "insert into role(rname) values(%s)"
            try:
                cursor.execute(sql, rname)
            except Exception as e:
                print(e)
                continue
            else:
                self.conn.commit()
                break

        self.print("add role successfully")
        cursor.execute("select rid from role where rname=%s", rname)
        role_id = cursor.fetchone().get('rid')
        cursor.close()

        self.assign_privilege(role_id)

    def view_role_manage(self):
        # self.print("\trole_manage\t\tview")
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = """select role.rid, role.rname, privilege.pname from role 
        left join role_privilege_relation 
        on role.rid = role_privilege_relation.rid
        left join privilege 
        on privilege.pid = role_privilege_relation.pid
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            self.print("%s %s %s" % (row['rid'], row['rname'], row['pname']))

        cursor.close()

    def assign_privilege(self, role_id):
        print("\033[1massign privileges to role\033[0m")
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select pid, pname from privilege order by pid")
        for row in cursor.fetchall():
            choice = input("\033[1mwhether add privilege: '%s'(y or n): \033[0m" %(row['pname'])).strip()
            if choice == "y":
                sql = "insert into role_privilege_relation(rid, pid) values(%s, %s)"
                try:
                    cursor.execute(sql, [role_id, row.get('pid')])
                except Exception as e:
                    print(e)
                else:
                    self.conn.commit()

        cursor.close()

    def user_manage(self):
        while True:
            self.print("""\tuser_manage\n\t\tadd\n\t\tview\n\t\tupdate""")
            choice = input('\033[1mPlease select menu(add,view,q): \033[0m').strip()
            if hasattr(self,"%s_user_manage" % choice):
                func = getattr(self, "%s_user_manage" % choice)
                func()
            elif choice == 'q': # return back previous menu
                self.print("return back previous menu")
                break
            else:
                print('\033[1mnot permitted\033[0m')

    def add_user_manage(self):
        # self.print("\tuser_manage\t\tadd")
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        while True:
            uname = input("\033[1m name: \033[0m").strip()
            sex = input("\033[1m sex: \033[0m").strip()
            email = input("\033[1m email: \033[0m").strip()
            password = input("\033[1m password: \033[0m").strip()
            self.view_role()
            role_id = input("\033[1m role id: \033[0m").strip()
            sql = "insert into user(uname, sex, email, role_id, password) values(%s, %s, %s, %s, %s)"
            password = encrypt(password)
            try:
                cursor.execute(sql, [uname, sex, email, role_id, password])
            except Exception as e:
                print(e)
                continue
            else:
                self.conn.commit()
                cursor.close()
                break

    def view_role(self):
        sql = "select * from role order by rid"
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for row in result:
                self.print("%-4s%-16s" % (row['rid'], row['rname']))
        else:
            self.print("not any role exist")
        cursor.close()

    def view_user_manage(self):
        # self.print("\tuser_manage\t\tview")
        sql = "select * from user"
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            self.print("not any user exist")
        cursor.close()

    def update_user_manage(self):
        old_role_id = 0
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        while True:
            uname = input("\033[1mplease input username want to update: \033[0m ").strip()
            email = input("\033[1mplease input email want to update: \033[0m ").strip()
            sql = "select role_id from user where uname = %s and email = %s "
            try:
                cursor.execute(sql, [uname, email])
            except Exception as e:
                self.print(e)
                continue
            else:
                result = cursor.fetchone()
                if result:
                    old_role_id = result.get('role_id')
                    self.print("old role_id = %s" % old_role_id)
                    break
                else:
                    self.print("check email and username")

        print("\033[1mrole you can select is as follows: \033[0m ")
        self.view_role()
        new_role_id = int(input("\033[1minput new role_id =\033[0m ").strip())
        sql = "update user set role_id = %s where role_id = %s"
        try:
            cursor.execute(sql,[new_role_id, old_role_id])
        except Exception as e:
            self.print(e)
        else:
            self.conn.commit()

        cursor.close()

    def privilege_manage(self):
        while True:
            self.print("""\tprivilege_manage\n\t\tview\n\t\tadd\n\t\tupdate\n\t\tdelete""")
            choice = input('\033[1mPlease select menu(view,q): \033[0m').strip()
            if hasattr(self,"%s_privilege_manage" % choice):
                func = getattr(self, "%s_privilege_manage" % choice)
                func()
            elif choice == 'q':
                self.print("return back previous menu")
                break
            else:
                print('\033[1mnot permitted\033[0m')

    def view_privilege_manage(self):
        sql = "select * from privilege order by pid"
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for row in result:
                self.print("%s %s"%(row.get('pid'), row.get('pname')))
        else:
            self.print("not any privilege exist")
        cursor.close()

    def add_privilege_manage(self):
        while True:
            self.print("please fill in privilege information")
            pname = input("privilege name: ").strip()
            sql = "insert into privilege(pname) values(%s)"
            cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            try:
                cursor.execute(sql, pname)
            except Exception as e:
                print(e)
                self.print("fill error")
            else:
                cursor.close()
                break

    def delete_privilege_manage(self):
        self.print("only delete role_privilege_relation, not support ")

    def update_privilege_manage(self):
        self.print("not support")

    def print(self, msg):
        print('\033[;34m%s\033[0m'% msg)

