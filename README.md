# flask-restx-api-with-vue-front

A minimal Flask-restx API with VUE frontend integration served through same Flask app. Dockerfile included to run in K8S/Docker.

Two blueprints defined:
- API blueprint
- VUE-UI blueprint

A "todos" namespace has been defined and registered to API blueprint. You can scale the API blueprint adding more namespaces (for each type of data). Inside a namespace has been defined 2 files:
- endpoints.py --> API endpoints definition.
- models.py --> API models definition.

Source code structure:
```
├───run.py
├───app.py
├───api
│   └───__init__.py
│   └───todos
|         └───endpoints.py
|         └───models.py
└───vueui
    ├───__init__.py
    ├───static
    │   └───index.js
    └───templates
        └───index.html
```

## Run project in Docker

To build and run docker execute:

```
git clone https://github.com/jordips/flask-restx-api-with-vue-front.git
cd flask-restx-api-with-vue-front
docker build -t flask-restx-api-with-vue-front .
docker run -p 80:80 flask-restx-api-with-vue-front
```
Once Docker is running you can access Swagger via http://localhost/api and VUE UI through http://localhost/

## Development environment

### Requirements

To execute the application you need:
- python3
- pip3

### Run application

You should create and activate a python virtual environment before run the application.

To run development environment:
```
git clone https://github.com/jordips/flask-restx-simple-api.git
cd flask-restx-simple-api
pip3 install -r requirements.txt
python3 run.py
```
Once Docker is running you can access Swagger via http://localhost:5000/api and VUE UI through http://localhost:5000/
