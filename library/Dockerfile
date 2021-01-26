#FROM python:3.6
#
#WORKDIR /usr/src/app
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install dependencies
#RUN pip install --upgrade pip
#COPY . /usr/src/app
#RUN pip install -r /usr/src/app/requirements.txt
##RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . /usr/src/app
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#FROM python:3.6
#ENV PYTHONUNBUFFERED=1
#
#COPY requirements.txt /code/requirements.txt

#COPY /home/skhra/Desktop/Library/library/requirements.txt /code/requirements.txt
#WORKDIR /code
#RUN pip install -r requirements.txt
#COPY . /code/
#
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
