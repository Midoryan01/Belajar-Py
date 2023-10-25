import os
os.system('cls')

sisi = int(input("Masukan panjang sisi :"))
panjang = 1
count = 1
while True:

    if (count < sisi):
        print((panjang*"*").center(sisi+1))
        count += 2
        panjang += 2
    else:
        print((panjang*"*").center(sisi+1))
        panjang -= 2
    
    if panjang < 1:
        break #BUAT BERHENTI
print(f'Anjay Jadi')


#Buat segitiga
sisi = int(input(f'Masukan angka  : '))

print('awal segitiga for')
count = 1
for i in range(sisi):
    print('*'*count)
    count+= 1

print('akhir segitiga for')

print('awal segitiga while')
count = 1
while True:
    print('*'*count)
    count += 1

    if count > sisi:
        break
print('akhir segitiga while')

print('awal segitiga sama sisi while')

count = 1
while True:
    
    if (count%2):
        #Print jika ganjil
        print('*'*count)
        count += 1
   
    else:
        count += 1
        continue 
    #akan break jika count melebihi sisi
    if count > sisi:
        break






