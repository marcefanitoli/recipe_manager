FROM python:3.7

RUN mkdir /data
VOLUME /data
RUN mkdir /app
WORKDIR /app
ADD ./app/ /app/

RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py test

EXPOSE 4000
#This is temporary. Will be switched to gunicorn.
CMD exec gunicorn --bind :4000 --workers 1 --threads 8 --timeout 0 recipe_manager.wsgi
#CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:4000"]
