# Flask Cloud Web Application

This is a simple Flask Web Application using [Python Flask](http://flask.pocoo.org/) and [MySQL](https://www.mysql.com/) database. 

This project has been customized and containerzed using Docker for cloud-friendly deployment.
  
  Below are the steps required to get this working on a base linux system.
  
  - **Install all required dependencies**
  - **Install and Configure Web Server**
  - **Start Web Server**
   
## 1. Install all required dependencies
  
  Python and its dependencies
  ```bash
  apt-get install -y python3 python3-setuptools python3-dev build-essential python3-pip default-libmysqlclient-dev
  ```
   
## 2. Install and Configure Web Server

Install Python Flask dependency
```bash
pip3 install flask
pip3 install flask-mysql
```

- Copy `app.py` or download it from a source repository
- Configure database credentials and parameters 

## 3. Start Web Server

Start web server
```bash
FLASK_APP=app.py flask run --host=0.0.0.0
```

## 4. Test

Open a browser and go to URL
```
http://<IP>:5000                            => Hello from Gheath Docker App
http://<IP>:5000/how%20are%20you            => I am doing great! This app is running inside Docker.
http://<IP>:5000/about                      => This is a Flask app containerized using Docker.
```
