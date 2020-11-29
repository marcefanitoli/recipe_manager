FROM python:3.7

RUN mkdir /data
VOLUME /data
RUN mkdir /app
WORKDIR /app
ADD ./app/ /app/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py test

EXPOSE 4000
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:4000"]