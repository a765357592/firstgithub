from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,TEXT,String,Float,Integer
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://puser:123456@localhost/pbook')
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'book'
    number = Column(TEXT)
    name = Column(TEXT)
    author = Column(TEXT)

    def __repr__(self):
        return "<Book(number='%s',name='%s')>" % (self.number,self.name)

def insertbook(books):
    for book in books:
        try:
            b = Book(number=book['number'],name=book['name'],author=book['author'])
        except ValueError:
            b = Book(number=book['number'],name=book['name'], author=book['author'])

            session.add(b)
    session.commit()


def find(books):
    our_books = session.query(Book).filter_by(number='25').first()
    our_books

def xiugai(books):
    mod_books = session.query(Book).filter_by(number='25').first()
    mod_books.name = 'pyhton'
    session.commit()

def dele(books):
    del_books = session.query(Book).filter_by(number='25').first()
    del_books
    session.delete(del_books)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)