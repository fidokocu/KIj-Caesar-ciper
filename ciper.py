def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            char_code += shift
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

# Meminta input dari pengguna
message = input("Masukkan pesan yang akan dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran (angka bulat): "))

encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("Pesan Asli:", message)
print("Pesan Terenkripsi:", encrypted_message)
print("Pesan Terdekripsi:", decrypted_message)
