FROM python:3.9-slim-buster

# Установка необходимых пакетов для графических приложений
RUN apt-get update && apt-get install -y \
    qt5-default \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Копирование исходного кода приложения в образ
WORKDIR /app
COPY . /app

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY=host.docker.internal:0

# Запуск PyQt приложения
CMD ["python", "YPPRPO.py"]
