FROM python:3.13
LABEL authors="ruslan bakeev"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN python manage.py fill_db

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]