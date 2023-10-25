import os
os.system('cls')

print(10*'=')
print("kalkulator Sederhana")
print(10*'=' + "\n")

angka1 = float(input('masukan anga 1 ='))
operator = input('operator (+,-,x,/) : ')
angka2 = float(input('masukan anga 2 ='))

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya {hasil}")
elif operator == "x" or operator == '*':
    hasil = angka1 * angka2
    print(f"hasilnya {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"hasilnya {hasil}")
else:
    print('Mikir aja sendiri')

print("thx")