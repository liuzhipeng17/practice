
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, CHAR, ForeignKey, MetaData

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


def create_tables():
    connect_str = 'mysql+pymysql://root:@127.0.0.1:3306/db2?charset=utf8'
    engine = create_engine(connect_str, max_overflow=5)
    Base.metadata.create_all(engine)  # Base一定要添加前面的Base.


def drop_tables():
    connect_str = 'mysql+pymysql://root:@127.0.0.1:3306/db2?charset=utf8'
    engine = create_engine(connect_str, max_overflow=5)
    Base.metadata.drop_all(engine)  # Base一定要添加前面的Base.


create_tables()