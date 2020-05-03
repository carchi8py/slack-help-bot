from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Usage(Base):
    """
    Some Metrics on usage
    """
    __tablename__ = 'usage'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    name = Column(String)
    email = Column(String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date,
            'name': self.name,
            'email': self.email
        }


engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)