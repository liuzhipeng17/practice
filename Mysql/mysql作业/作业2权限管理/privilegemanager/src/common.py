
import pymysql
from .commfunc import encrypt


class Common(object):
    def __init__(self, id, name, conn):
        self.uid = id
        self.name = name
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

        print("""\033[1mPrivileges your have are as follows \033[0m""")
        while True:
            for d in result:
                self.print("\t" + d.get('pname'))
            choice = input("\033[1mplease select menu(account,q): \033[0m").strip()
            if hasattr(self,"%s_manage" % choice):
                func = getattr(self, "%s_manage" % choice)
                func()
            elif choice == 'q':
                self.print("logout")
                break
            else:
                print('\033[1mnot permitted\033[0m')

    def account_manage(self):
        while True:
            self.print("""\taccount_manage\n\t\tview\n\t\tmodify""")
            choice = input('\033[1mPlease select menu(view,modify,q): \033[0m').strip()
            if hasattr(self,"%s_account_manage" % choice):
                func = getattr(self, "%s_account_manage" % choice)
                func()
            elif choice == 'q':
                self.print("back to previous menu")
                break
            else:
                print('\033[1mnot permitted\033[0m')

    def view_account_manage(self):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select uid,uname,sex,email,role_id from user where uid=%s", self.uid)
        result = cursor.fetchone()
        cursor.close()
        self.print("%-4s%-8s%-8s%-24s%-4s" % (
                                        'uid',
                                        'uname',
                                        'sex',
                                        'email',
                                        'role_id'
                                        ))
        self.print("%-4s%-8s%-8s%-24s%-4s" % (
                                        result['uid'],
                                        result['uname'],
                                        result['sex'],
                                        result['email'],
                                        result['role_id']
                                        ))


    def modify_account_manage(self):
        cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.print("you can only modify name, sex, password, and email")

        choice = input("\033[1mwhether modify name (y/n)?\033[0m").strip()
        if choice == 'y':
            new_name = input("new name: ").strip()
            sql = "update user set name=%s where uid=%s"
            cursor.execute(sql, [new_name,self.uid])
            self.conn.commit()

        choice = input("\033[1mwhether modify sex (y/n)?\033[0m").strip()
        if choice == 'y':
            new_sex = input("new sex: ").strip()
            sql = "update user set sex=%s where uid=%s"
            cursor.execute(sql, [new_sex,self.uid])
            self.conn.commit()

        choice = input("\033[1mwhether modify email (y/n)?\033[0m").strip()
        if choice == 'y':
            new_email = input("new email: ").strip()
            sql = "update user set email=%s where uid=%s"
            cursor.execute(sql, [new_email,self.uid])
            self.conn.commit()

        choice = input("\033[1mwhether modify password (y/n)?\033[0m").strip()
        if choice == 'y':
            new_password = input("new password: ").strip()
            sql = "update user set password=%s where uid=%s"
            new_password = encrypt(new_password)
            cursor.execute(sql, [new_password, self.uid])
            self.conn.commit()

        cursor.close()

    def print(self, msg):
        print('\033[;34m%s\033[0m' % msg)