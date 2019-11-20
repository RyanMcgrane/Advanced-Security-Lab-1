#C16419862
#Ryan McGrane
#DT 228/4 - Advanced Security 1
#10-10-19

#alphabet for the english letters & special charcters
SPECIAL = "() ,.-;:_?!="
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

with open('question_3.txt', 'r') as file:
    message2 = file.read().replace('\n', '')


def decrypt(cipher_text, key):
   
    plain_text = ""
    kpos = []
    i = 0

    for character2 in key:
        # Puts the key into the array kpos[]
        kpos.append(CHARACTERS.find(character2))
        # print(kpos) this is correct

    for character3 in cipher_text:
        if i == len(kpos):
            i = 0
        # If statement to remove any special characters defined above
        if character3 in SPECIAL:
            plain_text += character3
            continue
        if character3.isdigit():
            plain_text += character3
            continue
        position = CHARACTERS.find(character3.upper()) - kpos[i]
        if position < 0:
            position = position + 26
        plain_text += CHARACTERS[position]
        i += 1
    return plain_text


option = 1
while option == 1 or option == 2:
    print("\n******************Welcome to Vigenere Cipher!******************\nPress 1 to Decrypt a message"
	"\nPress 3 to exit")
    key = 'KISWAHILI'
    option = input("\n-->  Choice: ")
   
    if option == '1':
        cipher_text = message2

        plain_text = decrypt(cipher_text, key)
        print("\n*****The key used to decrypt this is:*****\n--> ", key)
        print("\n*****The decrypted message is:*****\n\n", plain_text)
        option = 2

if option == '3':
    print("\n\t Thank you for using this service\n")

else:
    print("Please enter a valid choice!")
