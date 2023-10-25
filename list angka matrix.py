import os
os.system('cls')

data = range(0,10,2) #start stop step(lompat brp)
print(data)
datalist= list(data)
print(datalist)

#list dengan for
list_make_for = [i**2 for i in range (0,10)] #** pangkat
print(list_make_for)

#list dengan for dengan if
list_make_for = [i for i in range (0,10) if i != 5] # != tidak sama dengan
print(list_make_for)


list_make_for = [i for i in range (0,10) if i%2 ==0] # ==0 untuk genap [==1] unutk ganjil/ [!=] bisa juga)
print(list_make_for)