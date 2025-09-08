
# Q5 using boolean value in variable
is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("no umeralla needed")

# Conditional Statements Questions
# Q6 check number is negative or positive
num1=float(input("enter number:"))
if num1 > 0:
    print("Positive")
elif num1 < 0:
    print("Negative")
else:
    print("zero")

# Q7 check user is adult or minor
age=float(input("enter number:"))
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Q8 in two numbers check which one is greater
num1=float(input("enter number:"))
num2=float(input("enter number:"))
if num1 > num2:
    print("num1 is Greater:",num1)
else:
    print("num2 is Greater:",num2)

# Q9 check value is vowel or consonant
value=(input("enter number:"))
if len(value) == 1 and value in 'AEIOUaeiou':
    print("VALUE IS VOWEL") 
else:
    print("value is consonant")

# Q10 check the wheater is hot or cold
num=float(input("enter temperatrue:"))
if num > 30:
    print("Hot")
elif num >= 20 and num < 30 :
    print("Moderate")
else:
    print("Cold")

# Q11 check year is leaf year
num=float(input("enter Year:"))
if num % 400 == 0:
    print("The Year is Leap Year")
elif num % 4 == 0:
    print("The Year is Leap Year")
elif num % 100 == 0:
    print("Normal Year")
else:
    print("Normal Year")

# Q12 print the smallest number
num1=float(input("enter number:"))
num2=float(input("enter number:"))
num3=float(input("enter number:"))
if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num3:
    print(num2)
else:
    print(num3)

# Q13 check password is weak or strong
while True:
    password=(input("enter number:"))
    if len(password) < 8:
        print("Weak Password")
        continue
    else:
        print("strong password")
    break

# Q14 check number is divisible with 5 or 7
num=float(input("enter number:"))
if num % 5 == 0 and num % 7 == 0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is not divisible by both 5 and 7.")

# Q15 check the grades of student
marks=float(input("Marks of Student: "))
if(marks>=90):
    grade="A"
elif(marks>=70 and marks < 89):
    grade="B"
elif(marks>=50 and marks <= 69):
    grade="C"
else:
    grade="F"

print("grade of the student :",grade)

# Q16 check number is in the range of 100-200
num=float(input("Enter number: "))
if num >= 100 and num < 200:
    print("The number is within the range 100-200.")
else:
    print("The number is not within the range 100-200.")

# Q17check letter is in the upper or lowercase
str=input("Enter string: ")
if str.isupper():
    print("UPPERCASE")
elif str.islower():
    print("lowercase")
else:
    print("Mixed case")

# Q18 check the number is three digit or not
num=str(input("Enter number: "))
if len(num) == 3 :
    print("3 number digit")
elif len(num) > 3 :
    print("greater than 3 digits")
else:
    print("less than 3 digits")

# Q19 check both strings are equal
val1=str(input("Enter string: "))
val2=str(input("Enter string: "))
if val1 == val2 :
    print("both strings are equal")
else:
    print("both strings are not equal")

# Q20 check number is end with 5
num=(input("Enter number: "))
if num.endswith('5'):
    print("Ends with 5")
else:
    print("Does not end with 5")
