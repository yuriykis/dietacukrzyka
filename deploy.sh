#!/bin/bash

sudo docker-compose down
sudo docker rmi dietacukrzyka_app
git pull origin master
rm -r /home/ubuntu/dietacukrzyka/dietacukrzyka/run/static/dist
cd frontend
npm run build
cp -r dist /home/ubuntu/dietacukrzyka/dietacukrzyka/run/static
cd ..
sudo docker-compose up -d