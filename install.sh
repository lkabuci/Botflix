# TODO:
# Add instructions installation script that include windows
# More flexible (ask the user about the default player for example)
# Add it to aur

READ='\e[31m%s\e[0m'
GREEN='\e[32m%s\e[0m'
YELLOW='\e[33m%s\e[0m'
BLUE='\e[34m%s\e[0m'

sudo npm install webtorrent-cli -g
python -m venv venv
source venv/bin/activate
clear

#printf "Green" "Successfully created a VE"
echo -n mpv > player.txt
printf $BLUE "mpv is now your default player change it latter"

# Create an executable file
mainpath=$PWD
echo """
cd $mainpath
source venv/bin/activate
python main.py
""" > botflix
chmod +x botflix

# move the executable file to path
sudo cp botflix /usr/bin/botflix
