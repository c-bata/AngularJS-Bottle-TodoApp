from datetime import datetime

from sqlalchemy import (
    Column, Integer, Unicode, UnicodeText, Boolean, DateTime,
    create_engine
)
from sqlalchemy.ext import declarative

from bottle.ext import sqlalchemy


Base = declarative.declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',    # 関数内で挿入される変数名
    create=True,     # テーブルを作成するか
    commit=True,     # 関数終了時にトランザクションをコミットするか
    use_kwargs=False
)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False)
    memo = Column(UnicodeText)
    done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return "<Task (title='%s')>" % self.title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'memo': self.memo,
            'done': self.done,
            'created_at': self.created_at.strftime('%Y-%m-%d')
        }
