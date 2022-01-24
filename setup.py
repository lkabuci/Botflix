# TODO: configure the setup script

import setuptools

setuptools.setup(
   name='itstreams',
   version='0.1',
   install_requires=["requests", "BeautifulSoup4", "prettytable", "subprocess"], 
   scripts=['itstreams']
)

