import string
import random

print("≠==============================≠") 
print("Generate Voucher Coca-Cola")
print("≠==============================≠")
print("\n")
jumlah = int(input("Butuh berapa ? : ")) 

# loop
N = 5
for i in range(jumlah):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    print("Kode : CCA2L"+ str(res))
    hasil = "CCA2L"+res
    of = open('voc.txt', 'a')
    of.write(hasil+'\n')
