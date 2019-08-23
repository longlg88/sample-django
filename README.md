# Sample Django 

## This project is sample django for deploying kubernetes cluster.

## 1. Following steps for installing django project in local env
### ENV : Ubuntu 18.04

```
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
sudo pip3 install virtualenvwrapper

cat .source_file >> ~/.bahrc
source ~/.bashrc

mkvirtualenv src
## deactivate - To deactivate this virtualenv
## rmvirtualenv [virtualenv name] - Remove this virtualenv
## workon [virtualenv name] - Move into working virtualenv


django-admin startproject [project name]
python3 manage.py runserver 0.0.0.0:8000
```

## 2. This steps for deploying kubernetes cluster.
