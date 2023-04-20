FROM python:3

# Установка необходимых пакетов для графических приложений
RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Установка переменных окружения для проброса дисплея
ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Копирование исходного кода приложения в образ
WORKDIR /app
COPY . /app

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открытие необходимых портов
EXPOSE 80

# Запуск PyQt приложения
CMD ["python", "YPPRPO.py"]
