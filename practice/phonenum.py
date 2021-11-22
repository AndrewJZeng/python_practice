import re

message = 'My name is Andrew Zeng. My mom\'s phone number is (832)531-1809. My dad\'s phone number is (217)721-2146.'

Phonepattern = re.compile('Andrew')
mo = Phonepattern.findall(message)
print (mo)