import string

alphabet = string.ascii_lowercase

def vigenere_cipher(text:str, key:str, modo:bool):
    text_final = ''
    text = text.lower()
    index_key = 0

    for letter  in text: 
        if letter in alphabet:
            index = alphabet.index(letter)
            if modo:
                index = (index + alphabet.index(key[index_key%len(key)]))%26
            elif not modo:
                index = index - alphabet.index(key[index_key%len(key)])
            else:
                pass
            text_final += alphabet[index]
            index_key += 1
        else:
            text_final += letter
    return text_final
