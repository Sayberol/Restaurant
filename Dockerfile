FROM python:3.9-slim-buster

# устанавливаем рабочую директорию в контейнере
WORKDIR /app

# копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# копируем все остальные файлы проекта в контейнер
COPY . .

# запускаем сервер Django при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]