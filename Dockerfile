 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /task_tracker
 WORKDIR /task_tracker
 ADD requirements.txt /task_tracker/
 RUN pip install -r requirements.txt
 ADD . /task_tracker/
 RUN python manage.py test
