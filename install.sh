#!/bin/bash

meeting requirements
echo "$(tput setaf 4)Installing Requirements"
npm install webtorrent-cli -g
git clone https://github.com/redelka00/stream-cli && cd stream-cli
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

#setting default player
echo "$(tput setaf 6)Setting MPV as Default Player, Change it later"
touch player.txt
echo -n "mpv" > player.txt

#creating bin
echo "$(tput setaf 4)Creating bin file:"
touch stream-cli
chmod 777 stream-cli
mainpath=$PWD

echo "
#!/bin/bash
cd $mainpath
python main.py

" > stream-cli

sudo cp stream-cli /usr/bin/
