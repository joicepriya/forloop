#EXAMPLE1

n=20
for i in range(1,n):
    print(i)

#EXAMPLE2

given_num=100
for i in range(given_num):
    if i%2==0:
        print(i)

#EXAMPLE3:

given_number=10
sum=0
for i in range(1,given_number+1):
    sum+=i
    print(sum)


#EXAMPLE4:

given_range=20
sum=0
for i in range(given_range):
    if i%2!=0:
        sum+=i
print(sum)

#EXAMPLE5

num=5
for i in range(11):
    print(num,"X",i,"=",i*5)

#EXAMPLE6:
list=[12,34,56,78,90,80,63,39]
for i in list:
    print(i)

#EXAMPLE7:
number=1234567890
number=str(number)
count=0
for i in number:
    count+=1
print(i)

#EXAMPLE8:
given_string="santhosh kumar"
revers_string=""
for i in given_string:
    revers_string=i+revers_string
if (given_string==revers_string):
    print(f"The string {given_string} is a Palindrome.")
else:
    print(f"The string {given_string} is not a Palindrome.")

#EXAMPLE9:
string=input("enter the string")
revers=""
for i in string:
    revers=i+revers
print(revers)

#EXAMPLE10

list=[12,33,44,56,67,89,23,45]
for i in list:
    if i%2==0:
        print(f"{i} is even number")

    else:
        print(f"{i} is odd number")



