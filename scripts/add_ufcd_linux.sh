#!/bin/bash
# Create texmf and change into folder
mkdir ~/texmf
cd ~/texmf

# Download University of Freiburg Corporate Design (access restricted to university IP range):
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-uni.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-iif.tds.zip
wget http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-imtek.tds.zip

unzip ufcd.tds.zip
unzip ufcd-logo-uni.tds.zip
unzip ufcd-logo-iif.tds.zip
unzip ufcd-logo-imtek.tds.zip

# Make the corporate design files available to latex
texhash ~/texmf
