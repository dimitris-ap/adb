from model.document import Document
from utils.DBUtils import get_db_session, array_to_bytes
from utils.InitializeUtils import initialize

if __name__ == '__main__':
    session = get_db_session()

    print("Initializing...")
    docs_df = initialize()
    print("Initialization completed!\n")

    print("Inserting documents into db...")
    for index, row in docs_df.iterrows():
        doc = Document(id=row['id'],
                       path=row['path'],
                       filename=row['filename'],
                       text=array_to_bytes(row['text']))
        print("Inserting obj:", doc)
        session.add(doc)
        session.commit()
    print("Done!")
