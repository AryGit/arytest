#! /usr/bin/env python

import os

RUTA_PYTHON = 'C:\Python27\python'
#RUTA_PYTHON = '/usr/bin/env python'
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

os.chdir(PROJECT_PATH)

os.system(RUTA_PYTHON + ' ' + 'manage.py runserver')
