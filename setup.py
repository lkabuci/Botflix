# TODO: configure the setup script

import setuptools

setuptools.setup(
   name='stream-cli',
   version='0.1',
   install_requires=["requests", "BeautifulSoup4", "prettytable"], 
   scripts=['stream-cli']
)

