import re
info = "my phone number is 123-545-6758"

phoneRegex = re.compile(r'''(\d{3}|\(\d{3}\))?
(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?''', re.VERBOSE)

mo = phoneRegex.search(info)
print(mo)
# print(mo.group())