#!/bin/bash
# Create texmf and change into folder
mkdir -p ~/texmf
cd ~/texmf

# Download University of Freiburg Corporate Design (access restricted to university IP range):
curl -L http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd.tds.zip -o ufcd.tds.zip
curl -L http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-uni.tds.zip -o ufcd-logo-uni.tds.zip
curl -L http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-iif.tds.zip -o ufcd-logo-iif.tds.zip
curl -L http://www.zuv.uni-freiburg.de/service/cd/download/latext/ufcd-logo-imtek.tds.zip -o ufcd-logo-imtek.tds.zip

unzip ufcd.tds.zip
unzip ufcd-logo-uni.tds.zip
unzip ufcd-logo-iif.tds.zip
unzip ufcd-logo-imtek.tds.zip

# Make the corporate design files available to latex
texhash ~/texmf
