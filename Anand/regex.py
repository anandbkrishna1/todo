# import re
# s="cat mat pat sat rat"
# x=re.findall(r'[cpr]at',s)
# print(x)

# import re
# s="abd abcd abccd abcccd abed"
# x=re.findall(r'ab.c+d',s)
# print(x)

# import re
# s="abd abcd abccd abcccd abed"
# x=re.findall(r'ab.*d',s)
# print(x)

# import re
# s="abd abcd abccd abcccd abed"
# x=re.findall(r'ab.?d',s)
# print(x)

# import re
# s="abd abcd abccd abcccd abed"
# x=re.findall(r'ab.{3}d',s)
# print(x)

# import re
# s="1 12 123 1234 12345"
# x=re.findall(r'123.+5',s)
# print(x)

# import re
# url="http://www.washingtonpost.com/news/ww/2016/09/02"
# x=re.findall(r'2016.+2',url)
# print(x)

import re
s="the quick brown frog jumps over the lazy dog"
x=re.split("\s",s)
for i in x:
    if len(i)==3 or len(i)==4:
       print(i)
     