
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

# 创建连接池（5个连接）
connect_str = 'mysql+pymysql://root:@127.0.0.1:3306/db2?charset=utf8'
engine = create_engine(connect_str, max_overflow=5)

# 创建一个会话（相当于拿一个连接）
Session = sessionmaker(bind=engine)
session = Session()

# 增加一行（创建一个对象）
# session.add(UserType(title="普通用户")) # 返回None

# 增加多行
session.add_all([
    UserType(title="白金用户"),
    UserType(title="黑金用户"),
    UserType(title="超级用户"),
])

session.commit()

# session关闭
session.close()








