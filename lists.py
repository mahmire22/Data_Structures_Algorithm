

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")




# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)





mylist = ['a','b', 'c', 'd', 'e', 'f']

mylist.pop(2)   #O(1)

del mylist[2:4] #will remove c,e  #O(n)

myList.remove('e') #O(n)

print(myList)


#Space complexity O(1) for all operations above





#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]



#Using in operator

if 100 in myList:
    print(myList.index(20))#..................O(n)
else:
    print('The value does not exist in the list')


#Linear Search

def searchinList(list, value):
    for i in list:#,,,,,,,,,,,,O(n)
        if i == value:#,,,,,,,,,,,,,O(1)
            return list.index(value)#,,,,,,,,O(1)
    return 'The value does not exist in the list'

#Time complexity O(n)
#Space complexity O(1)

print(searchinList(myList, 20))
print(searchinList(myList, 100))


#  List operations / functions

#split function
a = 'spam-spam1-spam2'
delimiter = 'a'
b = a.split(delimiter)
print(b)

#joint function
print(delimiter.join(b))

total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
					
print('Average:', average)



numlist = list() 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
					
average = sum(numlist) / len(numlist) 
print('Average:', average)


'''
Time and space complexity of lists:



Time complexity:

*Creating a list --------------------------------O(1)
*Inserting a value in a list ------------------- O(1)/O(n)
*Traversing a given list ------------------------O(n)
*Accessing a given cell -------------------------O(1)
*Searching a given value ------------------------O(n)
*Deleting a given value -------------------------O(1)/O(n)



Space complexity:

*Creating a list --------------------------------O(n)
*Inserting a value in a list ------------------- O(1)
*Traversing a given list ------------------------O(1)
*Accessing a given cell -------------------------O(1)
*Searching a given value ------------------------O(1)
*Deleting a given value  ------------------------O(1)

'''