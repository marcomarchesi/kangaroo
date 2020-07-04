'''
testing kangaroo
'''

from kangaroo import Kangaroo

app = Kangaroo('kangaroo-test')
app.update_version('1.0.2')
app.show_build()