# ProgrammingExcuses
Tired of making up your own excuses? Get them from http://programmingexcuses.com with python!

# Installing
`pip install programmingexcuses`

# Testing
```bash
$ programmingexcuse
Management insisted we wouldn't need to waste our time writing unit tests
```

# Usage
It's quite simple:  
```python
from programmingexcuses import get_excuse
print(get_excuse())
```

And, for convenience:
```python
from programmingexcuses import RandomExcuseError
try:
	...
except:
	raise RandomExcuseError()
```

Also, from a terminal:
```bash
programmingexcuse
```
