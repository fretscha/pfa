VIRTUALENV_DIR="/home/vagrant/venv"
PROJECT_DIR="/vagrant"


cat << EOF >> /home/vagrant/.bashrc

source $PROJECT_DIR/local.env

alias dj="/vagrant/manage.py"
alias djrun="/vagrant/manage.py runserver 0.0.0.0:8000"
alias djcelery="celery -A $PROJECT_NAME worker --loglevel=info -s /tmp/celerybeat-schedule \$1"

source $VIRTUALENV_DIR/bin/activate
export PS1="[$PROJECT_NAME \W]\\$ "
cd $PROJECT_DIR
EOF
