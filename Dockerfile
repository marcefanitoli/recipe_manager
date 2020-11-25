FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD ./app/ /app/
RUN pip install -r requirements.txt

EXPOSE 4000
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:4000"]