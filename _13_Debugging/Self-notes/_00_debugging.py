'''
Debugging:
Debugging is a process of locating  and rectifying the errors or bugs in the program.
with debugging process we can actually see the flow of execution.
after replicating the issue we perform root cause analysis by using this debugging process we can find the
issue causing error and then we can fix the issue and then testing the whole code once again.

debugging can be done in two ways:
using breakpoint technique
by importing pdb module

breakpoint technique:
keeping the points at starting line and ending line which you want to debug and can see the flow of execution
line by line

pdb module:
import pdb module before the line where you want to start to debug
and after end line we would write pdb.set_trace() upto where we want to debug the program

commmads:
 n --> execute next line
 c --> complete execution
 l --> list 3 lines before and after current line
 s --> step into function call
 b --> show list of break points
 b[int] --> set break point at line number
 b[func] --> break at function name
 cl --> clear all break points
 cl[int] --> clear break point at line number
 p --> print()

'''


import pdb

l = []
l2 = []
for i in range(0,20):
    if i%2 == 0:
        l.append(i)
    else:
        l2.append(i)
pdb.set_trace()
print(l,l2)


import pdb
l = [10,20,60,43]
for i in l:
    if i%2 == 0:
        print(i)
pdb.set_trace()

s = str(input('enter a string:'))  # Debugging using break point technique


def ctn_word(s1):
    cnt = 1
    for i in s:
        if i == ' ':
            cnt += 1
    return cnt


print('the count of words in string', ctn_word(s))
