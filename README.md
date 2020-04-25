# flask_tutorial

## steps to run

### build docker image

` docker build -t flaskr .`

### run docker image

`docker run -p 5000:5000/tcp -e PORT=5000 -e ENV=prod -t flaskr`
