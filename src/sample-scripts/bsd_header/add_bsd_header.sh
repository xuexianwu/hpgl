#!/bin/sh

find -iname "*.h" | xargs -I {} -n 1 python add_header.py hpgl_bsd_header.txt {}
find -iname "*.cpp" | xargs -I {} -n 1 python add_header.py hpgl_bsd_header.txt {}
find -iname "*.INC" | xargs -I {} -n 1 python add_header.py hpgl_bsd_header_for_INC.txt {}
find -iname "*.py" | xargs -I {} -n 1 python add_header.py hpgl_bsd_header_python.txt {}
