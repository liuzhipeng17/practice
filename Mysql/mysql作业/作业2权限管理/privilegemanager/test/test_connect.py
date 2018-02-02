import sys
import os.path


path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(1,path)

from privilegemanager.src.index_view import IndexPage
obj = IndexPage()
# print(obj.conn, obj.cursor)
obj.interactive()



