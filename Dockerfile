FROM python:3.6.1
RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
CMD python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000
