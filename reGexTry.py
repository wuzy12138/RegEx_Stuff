#!/bin/python
import re
info = "my phone number is 123-545-6758"


# re.VERBOSE : This flag allows you to write regular expressions that
# look nicer and are more readable by allowing you to visually 
# separate logical sections of the pattern and add comments.
phoneRegex = re.compile(r'''
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
''', re.VERBOSE)

mo = phoneRegex.search(info)
print(mo)
print(mo.group())