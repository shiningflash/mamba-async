PyBroker
=======================
(Using Celery with Flask and RabbitMQ)

Installing RabbitMQ
-----------

**Ubuntu 18.04**

Install:

`$ sudo apt-get install rabbitmq-server`

##### *Notes*
1. Check status by `$ systemctl status rabbitmq-server.service`
2. Check enablity by `$ systemctl is-enabled rabbitmq-server.service`
3. If disabled, enable it by `$ sudo systemctl enable rabbitmq-server`
4. Enable rabbitmq management dashboard by `$ sudo rabbitmq-plugins enable rabbitmq_management`
5. It should be listening TCP port 15672 `$ sudo ss -tunelp | grep 15672`


## Configure RabbitMQ

1. Add new user by `$ sudo rabbitmqctl add_user <admin> <mypassword>`
2. Add virtual host by `$ sudo rabbitmqctl add_vhost <myvhost>`
3. Add user tag by `$ sudo rabbitmqctl set_user_tags <admin> <mytag>`
4. Set permission by`$ sudo rabbitmqctl set_permissions -p <myvhost> <admin> ".*" ".*" ".*"`

**To start the server:** `$ sudo rabbitmq-server`

**To stop the server:** `$ sudo rabbitmqctl stop`


# Project Quick Setup

1. Clone this repository.
2. Create a virtualenv and install the requirements. `$ virtualenv venv`, `$ source venv/bin/activate` and `$ pip3 install -r requirements.txt`.
3. Open a terminal window and start a local RabbitMQ server.
4. Open the second terminal window. Start a Celery worker: `$ celery worker -A wsgi_app.celery --loglevel=info --pool=solo`.
5. Start the third terminal window for your application: `$ python3 wsgi_app.py`.
6. Go to `http://localhost:5000/` and enjoy this application!