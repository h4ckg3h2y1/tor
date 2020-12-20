#!/bin/bash
sudo apt-get update -y
sleep 3
sudo wget https://seoz.ml/tor/tor.py
sleep 5
sudo wget https://seoz.ml/tor/cron.sh
#no for tryhackme
#sudo wget https://bootstrap.pypa.io/get-pip.py
sleep 3
sudo apt-get install python3-pip -y #python3 get-pip.py  -y 
sleep 4
sudo apt-get install torbrowser-launcher -y
sleep 5
torbrowser-launcher %u
sleep 7
sudo apt-get install xvfb -y
sleep 3
wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
sleep 10
sudo tar -xvf geckodriver-v0.28.0-linux64.tar.gz
sleep 4
sudo cp geckodriver /usr/local/bin/
sleep 3
#seulment run une fois
sed -i '94,97d' /root/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/start-tor-browser
torbrowser-launcher %u
sudo service tor restart
pip3 install pyvirtualdisplay
pip3 install tbselenium
#seulment run une fois  for ubuntu
#sudo echo "*/5 * * * * /root/cron.sh" >> /etc/crontab
#selement run une fois for debian
crontab -l | { cat; echo "*/5 * * * * /root/cron.sh"; } | crontab -
sudo chmod +x cron.sh
#for ubuntu update cron command is service cron restart
#service cron restart
sudo /etc/init.d/cron restart
sh cron.sh
sleep 15
