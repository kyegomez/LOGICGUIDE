from setuptools import setup, find_packages

setup(
  name = 'logic_guide',
  packages = find_packages(exclude=['examples']),
  version = '0.0.1',
  license='APACHE',
  description = 'Logic Guide - HF',
  author = 'Kye Gomez',
  author_email = 'kye@apac.ai',
  url = 'https://github.com/kyegomez/LOGICGUIDE',
  long_description_content_type = 'text/markdown',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'transformers',
    'prompt engineering'
  ],
  install_requires=[
    'transformers',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)