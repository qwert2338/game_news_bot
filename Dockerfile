# Используем официальный Python
FROM python:3.11-slim

# Устанавливаем рабочую папку
WORKDIR /app

# Копируем файлы в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда запуска бота
CMD ["python", "main.py"]
