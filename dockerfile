# Base image
FROM python:3.13.3-alpine

WORKDIR /app

RUN apk update && apk add --no-cache build-base postgresql-dev
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
