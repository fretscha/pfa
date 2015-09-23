#!/usr/bin/env bash

source /vagrant/local.env

PG_VERSION=9.4
PG_CONF="/etc/postgresql/$PG_VERSION/main/postgresql.conf"
PG_HBA="/etc/postgresql/$PG_VERSION/main/pg_hba.conf"
PG_DIR="/var/lib/postgresql/$PG_VERSION/main"

apt-get install -y postgresql-$PG_VERSION postgresql-contrib-$PG_VERSION

sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/" "$PG_CONF"

echo "host    all     all     all     md5" >> "$PG_HBA"

echo "client_encoding = utf8" >> "$PG_CONF"

service postgresql restart

cat << EOF | su - postgres -c psql
-- Create the database user:
CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';

-- Create the database:
CREATE DATABASE $APP_DB_NAME WITH OWNER=$APP_DB_USER
                              LC_COLLATE='en_US.utf8'
                              LC_CTYPE='en_US.utf8'
                              ENCODING='UTF8'
                              TEMPLATE=template0;
EOF

touch /home/vagrant/postgres.done
