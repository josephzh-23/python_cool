#the following asks to sort by the 2nd element in the index

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)

# [('apple', '10', '200'), ('baby', '20', '300'), ('candy', '30', '100')]


