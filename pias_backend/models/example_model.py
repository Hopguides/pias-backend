
# Placeholder for database models
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExampleModel(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    name = Column(String)
