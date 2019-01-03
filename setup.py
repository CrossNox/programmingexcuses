from setuptools import setup


setup(name='programmingexcuses',
      version='0.1',
      description='Tired of making up your own excuses?',
      url='https://github.com/crossnox/programmingexcuses',
      author='CrossNox',
      packages=['programmingexcuses'],
      scripts=['script/programmingexcuse'],
      install_requires=['requests', 'bs4']
    )
