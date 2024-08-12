FROM python:3.12-slim

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install --no-cache-dir pipenv && pipenv install --deploy --ignore-pipfile

COPY / .

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "127.0.0.1:8000"]
