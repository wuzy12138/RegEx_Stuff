import re

info = "my phone number is 123-545-6758"

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex)
mo = phoneNumRegex.search(info)
print(mo)
print(mo.group())