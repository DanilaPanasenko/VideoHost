FROM python:3.12-alpine

# Задаем рабочую директорию
WORKDIR ./

# Установка переменной среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip setuptools
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .