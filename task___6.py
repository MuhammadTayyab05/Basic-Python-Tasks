# Q21
num = int(input("Enter time (in 24-hour format, e.g., 4 for 4 AM, 16 for 4 PM): "))
if num >= 4 and num <= 7:
    print("Good Morning")
elif num >= 12 and num <= 16:
    print("Good afternoon")
elif num >= 17 and num <= 20 :
    print("Good evening")
else:
    print("Good Night")

# Q22 finding prime number
i=2
while i <= 100:
    i+=1
    j=2
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i)
    i+=1

# Q23
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a < b+c and b < a+c and c < a+b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# LOOPS QUESTIONS
# 24 using for loop print even numbers 1 to 100
for i in range(0,102,2):
    print(i)

# Q25
i=10
while i >= 1:
    print(i)
    i-=1

# Q26
total=0
for i in range(1,51):
    total+=i
print(total)

# Q27
num=int(input("Enter number: "))
product=1
counter=1
while counter <= num:
    product*=counter
    counter+=1
print(product)

# Q28
var1= input(str("enter the string :"))
V=0
for i in var1:
    
    if i in ('AEIOUaeiou'):
        V +=1

print('there is vovels in the string',{V} )

# Q29
var1 = input("Enter the string: ")
var2 = reversed(var1)
print("".join(var2))
