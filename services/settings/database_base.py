# флаг для создания таблицы при старте
CREATE_TABLES = True


# Таблица пользователей
# id - int
# логин - str 32
# пароль - str 32
# версия операционной системы - str 64
TABLE_BOOKS = '''
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(32) NOT NULL,
    author VARCHAR(32) NOT NULL
)
'''