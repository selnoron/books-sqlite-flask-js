# sqlite3 позволяет работать с БД
# в режиме файловой системы
# без панели администратора и т.д.
import sqlite3
# Позволяет работать с датами
import datetime
# Для работы с json строками и различным
# преоразованием 
import json
# настройки для БД
from services.settings.database_base import TABLE_BOOKS, CREATE_TABLES
# подключение именованных кортежей
from typing import NamedTuple



# Модель пользователя User
class Book(NamedTuple):
    title      : str
    author     : str


# Предназначен для более простой работы
# с БД и хранению процедур, подключению и т.д.
class DB:
    def __init__(self) -> None:
        global CREATE_TABLES
        # имя БД
        self.basename = "sqlite.db"
        # объект подключения к БД
        self.connection = sqlite3.connect(self.basename)
        # Объект - указатель
        self.cursor = self.connection.cursor()
        if CREATE_TABLES:
            self.create_all_tables(
                TABLE_BOOKS
            )
            CREATE_TABLES = False
    

    def execute(self, query: str, is_commit: int = 0) -> object:
        try:
            result = self.cursor.execute(query)
            if is_commit == 1:
                self.connection.commit()
                return 0
            else:
                return result.fetchall()
        except Exception as e:
            print(f" --- EXCEPTION: <{e}> --- ")
            return 1
    
    # Метод создает все таблицы для БД
    # Нужно при старте работы с БД
    def create_all_tables(self, *tables: list[str]) -> None:
        for table in tables:
            self.execute(query=table, is_commit=1)
    

    # Метод для внесения записи о пользователе
    def set_book(self, data: Book) -> int:
        user_exists = self.execute(
            query=f'''
                SELECT id FROM books
                WHERE title='{data.title}'
                AND
                author='{data.author}'
            '''
        )
        print(user_exists, "EXISTS")
        if len(user_exists) > 0:
            return 1

        result = self.execute(
            query=f'''
                INSERT INTO books (title, author)
                VALUES ('{data.title}','{data.author}')
            ''',
            is_commit=1
        )

        return 0


    # Метод получения всех пользователей
    def get_all_books(self) -> list:
        result = self.execute(
            query='''
                SELECT * FROM books
            '''
        )

        return result
