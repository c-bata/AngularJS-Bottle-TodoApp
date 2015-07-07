from sqlalchemy import Column, Integer, Unicode, UnicodeText, Boolean
from sqlalchemy.ext import declarative
Base = declarative.declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    memo = Column(UnicodeText)
    done = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "<Task (title='%s')>" % self.title
