from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='programmingexcuses',
      version='0.1',
      description='Tired of making up your own excuses?',
      long_description=readme(),
      url='https://github.com/crossnox/programmingexcuses',
      author='CrossNox',
      packages=['programmingexcuses'],
      scripts=['script/programmingexcuse'],
      install_requires=['requests', 'bs4'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ]
      )
