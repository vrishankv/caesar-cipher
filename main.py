alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_decrypt(dir, text, shift):
    end_text = ""
    if dir == "decrypt":
        shift *= -1
    
    for char in text:
        if char in alphabet:
            pos = alphabet.index(char)
            end_text += alphabet[pos + shift]
        else:
            end_text += char
    print(f"Here's the {dir}ed result: {end_text}")

should_end = False
while not should_end:
    dir = input("Encrypt or decrypt:\n").lower()
    text = input("Type message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    encrypt_decrypt(dir, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if restart == "no":
        should_end = True
        print("Goodbye")

