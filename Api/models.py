from main.db import Base
from sqlalchemy import Column, String, Integer, DateTime, event, ForeignKey, column, Interval, Date, Float, Enum
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    categories = relationship("Category", backref='Category_info', nullable=True)


class Category(Base):

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    owner_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    category_name = Column(String)
    owner = relationship("User", backref="owner_user")
