from pathlib import Path

from src.csv_utils import read_csv
from src.json_utils import read_json, write_json


BASE_DIR = Path(__file__).resolve().parent


if __name__ == "__main__":
    try:
        data_path = BASE_DIR / "data"

        result_file_path = BASE_DIR / "result.json"
        csv_books_data = read_csv(data_path / "books.csv")
        json_users_data = read_json(data_path / "users.json")

        books_quantity, users_quantity = len(csv_books_data), len(json_users_data)


        counter = 0
        if csv_books_data and json_users_data:

            users_with_books = []

            books, users = divmod(books_quantity, users_quantity)

            books_counter_low, books_counter_high = 0, 0

            for i in range(users_quantity):
                user = json_users_data[i]
                if i >= users:
                    books_per_user = books
                else:
                    books_per_user = books + 1

                books_counter_high += books_per_user

                books_for_user = [
                    {
                        "title": book.get("Title", ""),
                        "author": book.get("Author", ""),
                        "pages": book.get("Pages", ""),
                        "genre": book.get("Genre", ""),
                    }
                    for book in csv_books_data[
                        books_counter_low : books_counter_low + books_per_user
                    ]
                ]
                counter += len(books_for_user)
                users_with_books.append(
                    {
                        "name": user.get("name", ""),
                        "gender": user.get("gender", ""),
                        "address": user.get("address", ""),
                        "age": user.get("age", 0),
                        "books": books_for_user,
                    }
                )
                books_counter_low = books_counter_high
            write_json(result_file_path, users_with_books)
        else:
            print(
                f"Один из файлов пустой: csv: {books_quantity}, json: {users_quantity}"
            )
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден — {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
