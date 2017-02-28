#
# Enigma Simulation
# Maddie Zug
# Cryptography
# Harvey Mudd College
#
# Start with a changing wiring
import re
import collections

#Configure rotors
rotor_notches = list("amhe")
rotor1 = list("abcdefghijklmnopqrstuvwxyz")
rotor1_wiring = [18, 1, 23, 16, 2, 22, 3, 11, 12, 24, 25, 4, 17, 5, 19, 13, 6, 7, 15, 8, 21, 0, 14, 9, 20, 10]
rotor2 = list("mdaogcbityequknjswxzflhpvr")
rotor2_wiring = [23, 16, 2, 22, 24, 7, 15, 8, 21, 0, 14, 9, 20, 10, 18, 1, 25, 4, 17, 5, 19, 13, 6, 3, 11, 12]
rotor3 = list("hzctuqgldwxjfaybveimpsrkno")
rotor3_wiring = [18, 4, 14, 5, 15, 8, 21, 19, 13, 1, 23,  11, 12, 24, 25, 6, 7, 0, 17, 9, 20, 16, 2, 22, 3, 10]
rotor4 = list("esxtukmaopgijwbnczlydqrfvh")
rotor4_wiring = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def resetRotors(rotor_notches):
	global rotor1
	global rotor2
	global rotor3
	global rotor4
	while (rotor1[0] != rotor_notches[0]):
		rotor1 = rotor1[1:]+[rotor1[0]]
	while (rotor2[0] != rotor_notches[1]):
		rotor2 = rotor2[1:]+[rotor2[0]]
	while (rotor3[0] != rotor_notches[2]):
		rotor3 = rotor3[1:]+[rotor3[0]]
	while (rotor4[0] != rotor_notches[3]):
		rotor4 = rotor4[1:]+[rotor4[0]]

def enterMessage(message):
	global rotor1
	global rotor2
	global rotor3
	global rotor4
	#count the number of rotor cycles
	cycle_count = 0
	cipher_text = ""
	for c in list(message):
		#Encipher/Decipher a char c

		index1 = rotor1.index(c)
		char2 = rotor2[rotor1_wiring[index1]]

		index2 = rotor2.index(char2)
		char3 = rotor3[rotor2_wiring[index2]]

		index3 = rotor3.index(char3)
		char4 = rotor4[rotor3_wiring[index3]]

		index4 = rotor4.index(char4)
		char5 = rotor4[rotor4_wiring[index4]]

		#Reverse directions

		index5 = rotor4.index(char5)
		char6 = rotor3[rotor3_wiring.index(index5)]

		index6 = rotor3.index(char6)
		char7 = rotor2[rotor2_wiring.index(index6)]

		index7 = rotor2.index(char7)
		cipher_char = rotor1[rotor1_wiring.index(index7)]


		cipher_text += cipher_char


		#cycle rotors
		cycle_count += 1

		rotor1 = rotor1[1:]+[rotor1[0]]
		if cycle_count%26==0:
			rotor2 = rotor2[1:]+[rotor2[0]]
		if cycle_count%(26*26)==0:
			rotor3 = rotor3[1:]+[rotor3[0]]
		#if cycle_count%(26*26*26)==0:
			#rotor4 = rotor4[1:]+[rotor4[0]]

	return cipher_text


def main():
	#Retrieve plaintext and sanitize to remove all non-alphabet characters
	f = open('enigma.txt', 'r')
	plaintext = f.read()
	plaintext = plaintext.lower()
	regex = re.compile('[^a-zA-Z]')
	sanitized_plaintext = regex.sub('', plaintext)

	ciphertext = enterMessage(sanitized_plaintext)
	print("Ciphertext = "+ciphertext)
	resetRotors(rotor_notches)
	plaintext = enterMessage(ciphertext)
	print("Plaintext = "+plaintext)


	out_file = open("ciphertext.txt", "w")
	out_file.write(ciphertext)
	out_file.close()

if __name__ == '__main__':
	main()
