#!/usr/bin/env bash

pip3 install virtualenv

cd /vagrant
virtualenv -p python3 /home/vagrant/venv
source  /home/vagrant/venv/bin/activate && pip install -r requirements/local.txt
source  /home/vagrant/venv/bin/activate && pip install -r requirements/test.txt

touch /home/vagrant/python_package.done
