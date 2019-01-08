from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='obliquestrategies',
      version='0.2',
      description='Over One Hundred Worthwhile Dilemmas',
      long_description=readme(),
      url='https://github.com/FdelMazo/obliquestrategies',
      author='FdelMazo',
      packages=['obliquestrategies'],
      scripts=['script/obliquestrategies'],
      classifiers=[
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ]
      )
