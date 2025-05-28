alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift):
    """Codifica un mensaje usando el cifrado César con un desplazamiento dado."""
    new_word = ""
    for m in list(message):
        if m in alphabet:
            alphabet_index = alphabet.index(m)
            new_index = (alphabet_index + shift) % len(alphabet)
            new_letter = alphabet[new_index]
            new_word += new_letter
        else:
            new_word += m
    print(f"Encoded word: {new_word}")
    return new_word

def decode(message, shift):
    """Decodifica un mensaje usando el cifrado César con un desplazamiento dado."""
    decoded_word = ""
    for m in list(message):
        if m in alphabet:
            alphabet_index = alphabet.index(m)
            new_index = (alphabet_index - shift) % len(alphabet)
            new_letter = alphabet[new_index]
            decoded_word += new_letter
        else:
            decoded_word += m
    print (f"Decoded word: {decoded_word}")

def main():
    """Función principal que maneja la interacción con el usuario para codificar o decodificar mensajes."""
    encoded_word = ""
    close_run = False
    while not close_run:
        direction = input("Type 'encode' to encrypt or 'decode'  to decrypt: \n").lower()

        message = input("Type your message: \n").lower()

        shift = int(input("Type shift number: \n"))
        if direction == 'encode':
            encoded_word = encode(message, shift)
        elif direction == 'decode':
            decode(encoded_word, shift)
        else:
            print("Direccion incorrecta")
        close_run_str = input("Close activity? Y/N: ").lower()
        if close_run_str == "y":
            close_run = True

if __name__ == "__main__":
    main()