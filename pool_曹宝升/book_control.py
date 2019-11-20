import book_pool
import book_orm
books = book_pool.getbooks()
book_orm.insertbook(books)
book_orm.find(books)
book_orm.xiugai(books)
book_orm.dele(books)