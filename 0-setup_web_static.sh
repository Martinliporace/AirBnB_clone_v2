#!/usr/bin/env bash
# Task 0. Prepare your web servers

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "hello" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
printf %s "server {
  location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html index.htm;
  }}" > /etc/nginx/sites-available/default                           
service nginx restart