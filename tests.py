import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_not_add_if_name_too_long(self):
        collector = BooksCollector()
        long_name = "А" * 45
        collector.add_new_book(long_name)

        assert len(collector.get_books_genre()) == 0 #проверка добавления книги

    def test_add_new_book_not_add_if_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_new_book("Книга")

        assert len(collector.get_books_genre()) == 1

    def test_new_book_added_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        assert collector.get_book_genre("Книга") == ""

    @pytest.mark.parametrize("genre", ["Фантастика", "Комедии"])
    def test_set_book_genre_success(self, genre):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)

        assert collector.get_book_genre("Книга") == genre

    def test_set_book_genre_fail_if_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Поэзия")

        assert collector.get_book_genre("Книга") == ""

    def test_get_books_with_specific_genre_return_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга1", "Книга2"]

    def test_get_books_for_children_excludes_age_restricted(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Ужасы")      
        collector.set_book_genre("Книга2", "Фантастика") 

        assert collector.get_books_for_children() == ["Книга2"]

    def test_add_book_in_favorites_and_delete(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books() == ["Книга"]

        collector.delete_book_from_favorites("Книга")
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")

        assert collector.get_list_of_favorites_books() == ["Книга"]