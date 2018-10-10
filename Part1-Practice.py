

#  Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
a = input("a large number:")
x = []
y = []
for i in a:
    if a.count(i) > 1:
        if i not in x:
                x.append(i)
if x != y:
    print ("the duplicate number is/are:", (x))
else:
    print ("the numbers are distinct")
print("")
print("")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

# Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.

a= int (input("please enter a large positive number: "))
b = 0

while (a > 0):
    r = a % 10
    b += r
    a = a // 10

print ( " sum of the digits is : ",(b))
print("")
print("")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------


# Write a Python program to find the digits which are absent in a given mobile number

a = input("Please enter your mobile number: ")

x = str(1234567890)
y = []
for i in a:
    for j in x:
        if a.count(j) == 0:
            if j not in y:
                y.append(j)
        
print(" the digits that are not present in your mobile number are:", (y))
print("")
print("")

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

# Write a Python program to find common divisors between two numbers in a given pair.

print ("please enter a set of number 'a' and 'b'")
a= int(input("a="))
b= int(input("b="))
y=[]
i = 1
while(i<=a and i<=b):
    if (a%i==0 and b%i==0):
        y.append(i)
    i+=1

print("the common divisors of", (a), "and ", (b), "are", (y))
print("")
print("")

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
