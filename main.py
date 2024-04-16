print("By first method")
a = int( input("Please enter value for A: "))  
b = int( input("Please enter value for B: "))  
temp = a 
a = b  
b = temp  
print ("The Value of A after swapping: ", a)  
print ("The Value of B after swapping: ", b)  
print("By second method")
P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
P, Q = Q, P 
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  








num = int (input ("Enter a number: " ))
if (num % 2) == 0:
    print ("The number is even")
else:
    print ("The number is odd")








num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   n = temp % 10
   sum += n ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")








n = int(input("Enter number of terms: "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1








file = open("abc.txt", "r")
while True:
	content=file.readline()
	if not content:
		break
	print(content)
file.close()







f = open("data.txt","a")
f.write("College: Dronacharya College of Engg. \n")
f = open("data.txt","r")
print(f.read())
f.close()







name = "Python"
print(name)
message = "I love Python."
print(message)







L = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0
for i in L:
	count += i
avg = count/len(L)
print("sum = ", count)
print("average = ", avg)








List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 
List.insert(2, 10087) 
print(List)
List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
List1.extend(List2) 
print(List1) 
print(sum(List2)) 
List3 = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List2.count(1))  
print(len(List3)) 
print(List3.index(2)) 
print(List3.index(2, 2)) 
List2.reverse()  
print(List2)
print(List2.pop()) 
del List2[0] 
print(List2)







d = {'Name': 'Himanshu', 'Age': '19', 'Country': 'India'} 
d2 = {'Name': 'Shivam', 'Age': '20'} 
print(d)
print(d.get('Name')) 
print(d.get('Gender'))
print(list(d.keys()))
print(list(d.values()))
d.pop('Age') 
print(d)
print(list(d.items())[1][0]) 
print(list(d.items())[1][1])
d.update(d2) 
print(d)
d.popitem() 
print(d) 
d.popitem() 
print(d)








num = int (input ("Enter a number: "))
flag = False
if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print ("The number entered is not a prime number")
else:
    print ("The number entered is a prime number")







dic={ 'a':455, 'b':223, 'c':300, 'd':908 }
print("Dictionary: ", dic)
print("sum: ",sum(dic.values()))






list = [2, 4, 6, 8, 10]
for i in list:
  print(i)







def insert(name, num): 
	print("Hello from ", name + ', ' + num) 

insert("Himanshu", "19")









rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()







num1 = 48
num2 = 72
a = num1
b = num2
while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1
print("GCD of", a, "and", b, "is", num1)







def linearSearch(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
n = len(arr)
result = linearSearch(arr, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)









def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, x)
if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")