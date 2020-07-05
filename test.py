'''
testing kangaroo
'''

from kangaroo import Kangaroo

app = Kangaroo('kangaroo')
app.show_build()

# update the version number on setup.py
app.update_setup_py()