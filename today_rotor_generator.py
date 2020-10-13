from random import shuffle
from pickle import dump

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = "abcdefghijklmnopqrstuvwxyz._@#$%&[]{},;^!~123456789"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.+-=_@#$%&[]{},;^!~123456789"

r1 = list(alphabet)
shuffle(r1)
r1 = "".join(r1)


r2 = list(alphabet)
shuffle(r2)
r2 = "".join(r2)

r3 = list(alphabet)
shuffle(r3)
r3 = "".join(r3)

file = open("./todays_rotor_state.enigma","wb")
dump((r1, r2, r3), file)
file.close()
