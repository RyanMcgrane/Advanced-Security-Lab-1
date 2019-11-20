#C16419862
#Ryan McGrane
#DT 228/4 - Advanced Security 1
#09-10-19

#alphabet for the english letters & special charcters
SPECIAL = " ,.-;:_?!="
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counter = 0
	
with open('question_1.txt', 'r') as file:
    message1 = file.read().replace('\n', '')
with open('question_6.txt', 'r') as file:
    message3 = file.read().replace('\n', '')
		
def decrypt(cipher_text, key):

    # Decrypts the parameter cipher text using the key and returns the now decryped plain text.
    plain_text = ""
    
	for character in cipher_text:
        
		# If statement to remove any special characters defined above
        if character in SPECIAL:
            plain_text += character
            continue
        
		index = CHARACTERS.find(character.upper())
        number = index + key
        new_index = number - (26*(number//26))
        plain_text += CHARACTERS[new_index]
		
    print("\n*****The decrypted message*****\n")
    return plain_text
	

def decrypt_option(counter):
    if counter == 0:
        print('\n***** Would you like to use your own key or to find a key? ***** \n Press 1 for your own key \n Press 2 to find the key')
        key_option = int(input(""))
        
		if key_option == 1:
            print('\n***** Great!! ***** \nEnter in your chosen key')
            key2 = int(input(""))
            print(decrypt(message, key2))
            counter = 1

        if key_option == 2:
            print(key(message, 0))
            counter = 1

        return counter

    else:
        return	


def key(plaintext, key):

    while key < 26:
        plain_text = decrypt(plaintext, key)
        print("using the key : " + str(key))
        print(plain_text)
        key += 1


def question(option):
    if option == 1:
        message = message1
    elif option == 6:
        message = message3
    else:
        print("ERROR")
    return message



option = int(input("\n******************Welcome!******************\n\nPick which question you want to decrypt so we can read in that file!!\n\nPress 1 for Question 1 ||| Press 6 for Question 6 \n \nPress 3 to exit at any time\n"))

while option == 1 or option == 6:
    counter = 0
    user_input = 2
    message = question(option)
    
	print('\n***** You are ready for decryption ***** \nPress 1 to decrypt the message \nPress 5 to exit')
    user_input = int(input("Enter choice:"))

    while user_input != 5 and user_input != 4:
        if user_input == 1:
            counter = decrypt_option(counter)
            option = 1
            user_input = 4

    if user_input == 5:
        option = 3


if option == 3:
    print("\n\t Thank you for using this service\n")

else:
    print("\nPlease enter a valid entry")
