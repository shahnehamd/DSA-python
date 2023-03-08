# Q) to find the colors ussed in the css code given (only includes those that are part of the coding and not the output text)
import re
# multiline string
s = '''<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:#ffffff;">..#addddd.</h1>

<h1 style="background-color:#234;">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">#000000</h1>'''

l=0
arr = []
while l != len(s)-1:
    f = s.find('<')
    l = s.find('>')
    r = re.findall('#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}', s[f:l])
    s = s[l+1:]
    arr += r
print(arr)
