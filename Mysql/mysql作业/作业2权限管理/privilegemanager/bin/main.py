import sys
import os.path


path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(1,path)

from privilegemanager.src.index_view import IndexPage


obj = IndexPage()
while True:
    print("\033[34;1mWelcome to index page of privilege manage system!\n"
          "1 login \n"
          "2 exit \n\033[0m")

    choice = input("\033[34;1mplease input your choice: \033[0m").strip()
    if choice == "1":
        obj.interactive()
    else:
        break





