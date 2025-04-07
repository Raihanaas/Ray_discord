# x = [1,23,4,45,7]
import random
def pw():
    karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    panjang_sandi = int(input("Panjang kata sandi :"))
    sandi = ""
    # Minimal karakter 6, no ID, Simbol, Number, Capslock
    for i in range(panjang_sandi):
        sandi += random.choice(karakter)
    print(sandi)
pw()