from distutils.core import setup

setup(
  name = 'diptanu-test-pypi',
  packages = ['diptanu-test-pypi'],
  version = '0.1',
  license='MIT',
  description = 'An awesome package that print stuffs!',
  author = 'Diptanu Sarkar',
  author_email = 'diptanusarkar@hotmail.com',
  url = 'https://github.com/imdiptanu/diptanu-test-pypi',
  download_url = 'https://github.com/imdiptanu/diptanu-test-pypi/archive/refs/tags/0.2.tar.gz',
  keywords = ['TEST', 'FIRST', 'EXAMPLE'],
  install_requires=[
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',     
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
