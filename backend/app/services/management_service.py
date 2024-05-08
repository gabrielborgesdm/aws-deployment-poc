from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.dtos.book_dto import BookCreateDto


class ManagementService:
    def get_authors(self):
        authors = AuthorModel.query.all()

        return authors

    def get_books(self):
        books = BookModel.query.all()

        return books

    def create_book(self, book: BookCreateDto):
        books = BookModel.query.all()

        return books