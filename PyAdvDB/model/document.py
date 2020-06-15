from sqlalchemy import Column, BigInteger, VARCHAR

from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Document(base):
    __tablename__ = 'document'

    id = Column(BigInteger, primary_key=True)
    filename = Column(VARCHAR(255), nullable=False)
    path = Column(VARCHAR(255), nullable=False)
    text = Column(BYTEA, nullable=False)

    def __str__(self):
        return "<Document? id:" + str(self.id) + ", filename:" + self.filename + ">"
