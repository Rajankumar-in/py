# list : list is a set of the container to store any kind of data type in a container. list is a mutable data type in
#  python. list is defined by using square brackets [].

friends = ["orange", "rahul", 5 , 4.23, False ,  "rohan", "ramesh", "rajesh"]
print(friends[0])

#sort method is used to sort the list in ascending order. sort method is only applicable for the list which contains same data type.
numbers = [1, 5, 3, 4, 2]
numbers.sort()
print(numbers)      
#reverse method is used to reverse the list. it will reverse the list in descending order.
numbers.reverse()
print(numbers)          
#append method is used to add the element at the end of the list.
numbers.append(6)           
print(numbers)  
#insert method is used to add the element at the given index of the list.
numbers.insert(2, 7)
print(numbers)  
#remove method is used to remove the element from the list.
numbers.remove(7)
print(numbers)      
#pop method is used to remove the last element from the list.
numbers.pop()
print(numbers)  
#clear method is used to remove all the elements from the list.
numbers.clear()
print(numbers)  

