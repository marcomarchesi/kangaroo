# Kangaroo ![build](https://github.com/marcomarchesi/kangaroo/workflows/build/badge.svg)



A simple build tracker.  

Install with `pip install kangaroo-build`

Basic usage:  

```python
from kangaroo import Kangaroo

app = Kangaroo('project-name')

# to show the version and build number
app.show_build()

# to update the version into setup.py
app.update_setup_py()
```
