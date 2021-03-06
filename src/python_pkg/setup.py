#
#   Copyright 2009 HPGL Team
#   This file is part of HPGL (High Perfomance Geostatistics Library).
#   HPGL is free software: you can redistribute it and/or modify it under the terms of the BSD License.
#   You should have received a copy of the BSD License along with HPGL.
#

from setuptools import *
setup(
    name = "HPGL-BSD",
    version = "0.9.6",
    #scripts = ['geo.py'],
	include_package_data = True,
	#package_dir = {'': 'package'},
	packages = ['geo'],
	package_data = {'geo': ['*.py'], 'geo':['*.dll'],'geo':['*.pyd'],'geo':['*.pdb']},

    # metadata for upload to PyPI
    author = "Vladimir Savichev, Artur Muharlyamov, Andrew Bezrukov, Konstantin Barsky, Dina Nasibullina",
    author_email = "muharlyamovar@ufanipi.ru, barskykd@ufanipi.ru, bezrukovav@ufanipi.ru, nasibullinads@ufanipi.ru, savichevvi@ufanipi.ru",
    description = "HPGL: High Perfomance Geostatistical Library (BSD Release)",
    license = "Commercial",
    keywords = ["geostatistics"],
    url = "http://hpgl.sourceforge.net/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
