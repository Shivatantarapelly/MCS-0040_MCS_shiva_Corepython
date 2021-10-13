a = 10
b = 10
print(id(a))
print(id(b))
if a is b:
    print('ok')
'''
7. bitwise operator(&,|,~,^,<<,>>) 
'''
a=10
b=8
c = a&b     #a value in binary 1010 and b is 1000 besing in and, or operations a&b is 8 and a|b is 10
print(c)
c = a|b
print(c)
print(~a)
'''
1. ~compliment operator
~a value is -11 as value of a in bit wise is 00001010=> 1's compliment=> 11110101
-11 in bitwise is 00001011=> 1' compliment=> 11110100=>2'compliment=>11110101
hence both are eqaul
2. &operator 
comparing both bitwise values if both are 1 then the value is counted
3. | pipe operator is like or operator
4. ^ is XOR operator works if there are any odd no.of 1's like(1 0 ,0 1)
5. << left shift add two zeros at right side of bitvalue like for 10 1010=>adding two 0's=>101000=>40
6. >> right shift deletes two numbers from left like for 10 1010=>deleting two positions=>10=>2
'''

