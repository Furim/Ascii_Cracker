import hashlib
import random 

LSC0 = ["A", "E", "I", "O", "U", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z", "W", "Y", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



#for now only ASCII cracker works with the one word at a time.


print(" what u want to to do crack(crc) validate hash(vah) ")

CHC0 = input("")



#hash example 18f5384d58bcb1bba0bcd9e6a6781d1a6ac2cc280c330ecbab6cb7931b721552

if CHC0 == "crc":
    print("Your hash u want encode")
    ASCP0 = input("")
    #ASCP0 = hashlib.sha256(ASC0).hexdigest()
    print("your u want to encode is " + ASCP0)
    while True:   
        PSC0 = random.choice(LSC0).encode("utf-8")
        LSCH0 = hashlib.sha256(PSC0).hexdigest()
        print(ASCP0)
        print(PSC0)
        print(LSCH0)
        if ASCP0 == LSCH0:
            print("hash found:")
            print(PSC0)
            break
if CHC0 == "vah":
    print("give me hash that u got to validate them")
    HSH0 = input("")
    HSH1 = input("")
    if HSH0 == HSH1:
        print("hash is valid :)")


print()








