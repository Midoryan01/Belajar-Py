import os
os.system("cls")

import random

print('-'*50)
print('             Batu Gunting Kertas             ')
print('-'*50)


print('cara bermain')
print(""" Ketik lah dari salah satu pilihan dibawah
      Batu / Gunting / kertas 
      """)


        
        
player = input('tentukan pilihanmu!\nBatu/Gunting/Kertas = ').title()
Bot = random.choice(['batu', 'gunting' ,' kertas']).title()

print('Kamu : ' + player) 
print('Bot  : ' + Bot)

if player == Bot :
    print("seri")
elif (player == 'Batu' and Bot == 'Gunting')  or (player == 'Gunting' and Bot =='Kertas')  or (player == 'Kertas'and Bot =='Batu'):
    print('kamu menang hoki doang !!!!')
else :
    print('HAHA KAMU BODOH')






