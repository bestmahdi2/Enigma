from pickle import load


alphabet = "abcdefghijklmnopqrstuvwxyz._@#$%&[]{},;^!~123456789"

f = open("./todays_rotor_state.enigma","rb")
r1, r2, r3 = load(f)
f.close()

def reflector(char):
	return alphabet[len(alphabet)-alphabet.rfind(char)-1]

def enigma_one_char(char):
	c1 = r1[alphabet.rfind(char)]
	c2 = r2[alphabet.rfind(c1)]
	c3 = r3[alphabet.rfind(c2)]
	reflected = reflector(c3)
	c3 = alphabet[r3.rfind(reflected)]
	c2 = alphabet[r2.rfind(c3)]
	c1 = alphabet[r1.rfind(c2)]

	return c1

def rotate_rotors():
	global r1, r2, r3

	r1 = r1[1:] + r1[0]

	if state % 26:
		r2 = r2[1:] + r2[0]
	if state % (26*26):
		r3 = r3[1:] + r3[0]

plain = "hihihihi"
cipher = ""
state = 0

for char in plain:
	state += 1
	cipher += enigma_one_char(char)
	rotate_rotors()


print(cipher)