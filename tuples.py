# list are mutable : list me koi bhi value ko change kar sakte hai. list me duplicate value ko store kar sakte hai. 
# list me different data type ko store kar sakte hai. 
# list me indexing and slicing ka use kar sakte hai. 
# list me append, insert, remove, pop, clear, sort, reverse function ka use kar sakte hai.
# tuples are immutable : tuple me koi bhi value ko change nahi kar sakte hai. 
# tuple me duplicate value ko store kar sakte hai.  

a = (1, 2, 3, 4, 5 ,False , "rajan", 3.5)
print(type(a))
print(a)
#a.count(3) #tuple me 3 kitni baar hai ye count karega.
print(a.count(3))
print("tuple me 3 ka index kya hai -->", a.index(3)) #tuple me 3 ka index kya hai ye print karega.
print(a.index(3)) #tuple me 3 ka index kya hai ye print karega.
print(a*5) #tuple me 5 baar repeat karega.
