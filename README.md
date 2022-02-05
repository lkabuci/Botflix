<h1 align="center"><u>Stram-Cli</u></h1>
####Stream-Cli application that allow you to play your favorite movies from the terminal.

## Installation:
* First let's install nodejs and npm in the machine.
*it depends on your distro* .
	* Archlinux: `sudo pacman -S nodejs npm`
	* Ubuntu: `sudo apt install nodejs npm`
	* Fedora: `sudo dnf install nodejs  npm`

* Install  [webtorrent](https://github.com/webtorrent/webtorrent).
`npm install webtorrent-cli -g`

* Make sure that you have [MPV](https://mpv.io/) media player installed
 	* Archlinux: `sudo pacman -S mpv`
 	* Fedora: `sudo dnf mpv`
 	* Ubuntu: `sudo apt install mpv`

* Stream-cli is builted with python 3.8 make sure to have the same version or higher:
`python --version`

* Download the Github Repo.
`git clone https://www.github.com/red-elka/stream-cli ~/.stream-cli`

* First you need to install the python requirements.
`sudo python ~/.stream-cli/setup.py install`

* Add the run permission to the file.
`sudo chmod +x ~/.stream-cli/stream-cli`

* Add an alias to your `~/.bashrc` or `~/.zshrc`
bash : `echo "alias stream-cli='~/.stream-cli/stream-cli'" >> ~/.bashrc`
zsh: `echo "alias stream-cli='~/.stream-cli/stream-cli'" >> ~/.zshrc`

## How it works:
* Run from the command line `stream-cli`
* Type the movie that you want to watch
* Select the choosen one and type the episode number
* Bring Some Popcorn, Enjoy😉