
# Q26 printing the all elements of list
list_1=[2,4,6,7,6,6,8,10]
index=0
while index<(len(list_1)):
    print(list_1[index])
    index+=1

# 27 reverse all the tuple
tup=(1,2,3,4,5,6)
for i in tup:
    i=0
print(tuple(reversed(tup)))

# 28 sum the all value of dictionary
dic={'harry' :81,
     'tayyab':61,
     'hassan':87
    }
for i in dic:
    val=dic.values()
print(sum(val))

# Q 29 print only number greater than 10
set={5, 12, 7, 20, 3}
i=0
for i in set:
    if i > 10:
        print(i)
        i+=1

# Q 30 convert to upper case
lst = ['harry','sam','stark']
for name in lst:
    print(name.upper())

# Q31 fabaonacci series
n = int(input("Enter a numbers: "))
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()

# Q32 print the greater value in dictionary
dic={'harry' :81,
     'tayyab':61,
     'hassan':87
    }
for i in dic:
    val=dic.values()
print(i,max(val))

# Q33 print only 7 numbers
list_1=[2,4,6,7,6,6,8,10]
print(list_1[0:7])

# Q34 check that element is present in given tuple
tup=('banana','apple','mango','grapes')
val=(input("Enter a numbers: "))
if val in tup:
    print('True')
else:
    print('false')

# Q35 remove one digit
set={5, 12, 7, 20, 3}
set1=set.remove(5)
print(set)

# Q36 average of list
list_1=[2,4,6,7,6,6,8,10]
for i in list_1:
    ave=(sum(list_1))/len(list_1)
print(ave)

# Q37 print both value and key
dic={'harry' :81,
     'tayyab':61,
     'hassan':87
    }
print(dic.items())

# Q38 show length of sentence
val=(input("Enter a numbers: "))
print(len(val))

# Q39 giving ASCII
val = "TAYYAB"
for el in val:
    print(el,ord(el))
