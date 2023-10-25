import os
os.system('cls')

#data    0(-3),  1(-2),   2(-1)
data = ["ucup","otong", "utung"]

# mengambil data
data_0= data[0]
print(data_0)

# mengambil info jumlah data
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data

#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")#

#nambah di awal
data.insert(1,"Udin")
print(f"data sesudah ditambah = \n {data}")

#appent untuk nambah data di akhir
data.append("asep")
print(f"data sesudah ditambah = \n {data}")

#menambahkan list dengan list
data_baru = ["Ujang","Usep","Dedeng"]
data.extend(data_baru)
print(f"data sesudah ditambah = \n {data}")

#merubah data

data[2]= "Michael"
print(f"data rubah= \n {data}")

#hapus data
data.remove("utung")
print(f"data remove= \n {data}")

#hapus data paling belakang

data_akhir= data.pop()# pop untuk paling belakang
print(f"data akhir")













