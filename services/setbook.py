from flask import session
from services.database.database import Book, DB


# функция регистрации пользователя
# вернет:
# 0 - ОК
# 1 - все плохо
def setboo(data: dict) -> int:
    user = Book(
        title=data.get("title"),
        author=data.get("author")
    )

    if not isinstance(user.title, str):
        return 1
    
    if not isinstance(user.author, str):
        return 1

    db : DB = DB()
    result_of_setbook = db.set_book(data=user)

    if isinstance(result_of_setbook, int):
        if result_of_setbook == 0:
            session["title"] = user.title
            return 0
        return 1
    return 1

def all_books() -> int:
    db : DB = DB()
    result_of_setbook = db.get_all_books()

    if isinstance(result_of_setbook, list):
        return result_of_setbook
    return 1