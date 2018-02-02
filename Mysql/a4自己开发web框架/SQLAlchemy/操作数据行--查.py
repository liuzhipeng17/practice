
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR, ForeignKey
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UserType(Base):
    __tablename__ = 'usertype'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(CHAR(64), index=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(CHAR(64),index=True)
    email = Column(CHAR(64), unique=True)
    usertype_id = Column(Integer, ForeignKey('usertype.id'))


connect_str = 'mysql+pymysql://root:@127.0.0.1:3306/db2?charset=utf8'
engine = create_engine(connect_str, max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()
# 只从下面添加数据
#1  查询所有
# user_type_lists = session.query(UserType).all() # 返回一个列表，列表元素为UserType对象
#2 filter(表达式，UserType.id == 2)
# user_type_lists = session.query(UserType).filter(UserType.id > 2)
#3 filter_by(参数)
# user_type_lists = session.query(UserType).filter_by(id=2)
#4 查询指定列
user_type_lists = session.query(UserType.title).all()
for row in user_type_lists:
    print(row.title)
# 只从上面添加数据
session.commit()
session.close()








