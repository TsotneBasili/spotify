FROM python:3.8.2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
