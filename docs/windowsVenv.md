### <div align='center'>Stream-CLI</div>

#### Instructions to setup Stream-CLI on windows:
*For windows 10 and 11 users, It's highly recommended to use [Windows WSL], cause many of the tutorials for Python are written for Linux environments.*

1. Open PowerShell or Windows Command Prompt (cmd).
2. type the following command `wsl --install`.
3. After the installation is complete restart your machine.
4. Check wsl version `wsl -l -v`.

> You can use this documentation of how to complete the [setup]

1. Install pip `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
2. run this in the same folder you run the curl in it `python3 get-pip.py`
3. clone the repo if you aren't already `git clone https://github.com/redelka00/stream-cli` and `cd stream-cli`.
4. create venv `virtualenv venv`.
5. Activate virtualenv `.\venv\Scripts\activate.bat`

Once you setup the virtual environment successfully go back to the [README]


<!-- Links -->
[Windows WSL]: https://docs.microsoft.com/en-us/windows/wsl/
[setup]: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/
[README]: https://github.com/redelka00/stream-cli
