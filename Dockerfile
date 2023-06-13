FROM python:3.9

ENV PYTHONUNBUFFERED 1

# устанавливаем рабочую директорию в контейнере
WORKDIR /code

# копируем файлы зависимостей и устанавливаем их
COPY requirements.txt /code/

RUN pip install -r requirements.txt

# копируем все остальные файлы проекта в контейнер
COPY . /code/
