FROM python:3.11-slim

# Задаем рабочую директорию
WORKDIR ./app

# Установка переменной среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект
COPY . .