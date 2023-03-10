'''#program to add two numbers
inpt1 = int(input("Enter 1st number :"))
inpt2 = int(input("Enter 2nd number :"))

print("Your answer is ",inpt1+inpt2)'''


'''#prgrm to calculate str length
inpt = input("Enter Your string :")
print(len(inpt))'''

'''#write a prgrm to test weather it is int
#to_cheack = "str"
to_cheack = 10
a = type(to_cheack)
if a == int:
    print ("yes its a integer")
else :
    print("no its not an integer ")'''

'''#prgrm to concadinate two dict
dict1 = {1:2}
dict2 = {4:5}
dict3 = {3:6}

ans = {**dict1, **dict2, **dict3}
print(ans)'''

'''#write a program to count repetative number in a string
usr_inpt = input("Enter a string : ")'''

'''#write a python program to cheack if a list is empty or not
list1 = []
if len(list1) == 0:
    print("list is empty")
else:
    print("list is not empty ")'''


'''#write a prgrm to remove duplicate from list with typecasting
list1 = [12,12,12,1,2,1,2,3,4,5,6,55,43,43,23]
#print(set(list1))

print("orginal list",list1)
ans = []
[ans.append(x) for x in list1 if x not in ans]
print ("The list after removing duplicates : "
	+ str(ans))'''

'''#prgrm to count repetative words
a= input("Enter your string: ")
out = {}
for i in a :
	if i not in out:
		c=1
		out.update({i:c})
	else:
		c += 1
		out.update({i:c})
print(out)'''