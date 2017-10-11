Python and Machine Learning: How to clusterize a malware dataset ?
======================================

This repository is the summary of the workshop at Hack.lu 2017 about machine learning and malwares

Setup your environment
======================

* Install python 3.5

* Install redis database

* Create a virtual env

`virtualenv --python=/usr/bin/python3.5 <destination_path>`

* activate your virtualenv

`source <destination_path>/bin/activate`

* Install dependencies

`pip install -r requierments.txt`

`git clone https://github.com/sebdraven/pe-parse.git`

`cd pe-parse/python`

`python3.5 setup.py install`

`git clone https://github.com/sebdraven/petojson.git`

`cd petojson`

`python3.5 setup.py install`

Install the dataset
===================

* clone theZoo malware dataset
`git clone https://github.com/ytisf/theZoo.git`


* Unzip all .zip
`cd theZoo`
`find . -name '*.zip' -exec sh -c 'unzip -P infected -o -d "${0%.*}" "$0"' '{}' ';'`


Run your environment
====================

`git clone https://github.com/sebdraven/hack_lu_2017.git`

`cd hack_lu_2017`

`ipython notebook`



 
