#!/usr/bin/env bash

apt-get update
apt-get dist-upgrade -y
apt-get install -y build-essential
apt-get install -y gettext

apt-get install -y zlib1g-dev
apt-get install -y libpq-dev
apt-get install -y libtiff5-dev
apt-get install -y libjpeg8-dev
apt-get install -y libfreetype6-dev

apt-get install -y libwebp-dev
apt-get install -y libmemcached-dev
apt-get install -y libssl-dev
apt-get install -y graphviz-dev
apt-get install -y liblcms2-dev

apt-get install -y python3-dev
apt-get install -y python3-pip
apt-get install -y python3-lxml

touch /home/vagrant/ubuntu_package.done
