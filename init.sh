#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx start
sudo nginx -s reload

gunicorn -b 0.0.0.0:8080 hello:app &

