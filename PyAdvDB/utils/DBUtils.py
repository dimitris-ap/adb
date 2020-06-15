from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import numpy as np

from model.document import Document

db = create_engine("postgres://postgres:password@localhost:5432/documentsDB")
base = declarative_base()
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)


def get_db_session():
    return session


def load_data_from_db():
    docs = session.query(Document)
    df = pd.read_sql(docs.statement, docs.session.bind)
    df.text = df.text.apply(lambda x: bytes_to_array(x))
    return df


def array_to_bytes(arr):
    return arr.tobytes()


def bytes_to_array(text):
    return np.frombuffer(text)
