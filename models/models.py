from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///storage.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Dispositivos(Base):
    __tablename__ = 'dispositivos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    data_hora = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Device {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)
