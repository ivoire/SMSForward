from setuptools import setup

setup(name='SMSForward',
      version='0.1',
      description='Forward some message over SMS',
      author='Remi Duraffort',
      author_email='remi.duraffort@gmail.com',
      url='https://github.com/ivoire/SMSForward',
      scripts=['SMSForward.py'],
      packages=['providers'],
      install_requires=['requests']
     )
