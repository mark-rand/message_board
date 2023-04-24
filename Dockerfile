FROM python 
COPY . /srv/flask_app
WORKDIR /srv/flask_app
RUN pip install flask waitress
CMD waitress-serve --port=5050 --call flaskr:create_app
