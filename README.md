 Список тестов
1. test_add_new_book_not_add_if_name_too_long – add_new_book, get_books_genre  
   Проверяет, что книга не добавляется, если её название длиннее 40 символов.

2. test_add_new_book_not_add_if_duplicate – add_new_book, get_books_genre  
   Проверяет, что одна и та же книга не добавляется дважды.

3. test_new_book_added_without_genre – add_new_book, get_book_genre  
   Проверяет, что при добавлении новой книги её жанр изначально пустой.

4. test_set_book_genre_success – set_book_genre, get_book_genre  
   Проверяет, что у книги можно установить корректный жанр и метод возвращает установленное значение.

5. test_set_book_genre_fail_if_genre_invalid – set_book_genre, get_book_genre  
   Проверяет, что у книги не устанавливается жанр, если жанр недопустимый.

6. test_get_books_with_specific_genre_return_books – add_new_book, set_book_genre, get_books_with_specific_genre  
   Проверяет, что метод возвращает список книг, соответствующих указанному жанру.

7. test_get_books_for_children_excludes_age_restricted – add_new_book, set_book_genre, get_books_for_children
   Проверяет, что книги с возрастным ограничением не попадают в список для детей, а разрешённые книги – попадают.

8. test_add_book_in_favorites_and_delete – add_new_book, add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books  
   Проверяет, что книгу можно добавить в избранное, а затем удалить из него. После удаления список избранных пуст.

9. test_add_book_in_favorites_not_add_duplicate – add_new_book, add_book_in_favorites, get_list_of_favorites_books
    Проверяет, что одна и та же книга не добавляется в избранное повторно.