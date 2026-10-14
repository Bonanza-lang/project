Запуск базы:
  cp .env.example .env   # один раз, потом поправь под себя
  docker compose up -d db

Первый запуск:
  pip install -r requirements.txt
  python manage.py migrate

Если 5432 занят — поменяй DB_PORT в .env (например, на 5433).

Данные базы лежат в docker volume. Полный сброс:
  docker compose down -v
  docker compose up -d db
  python manage.py migrate