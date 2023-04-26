# Создаем таблицу алфавита
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# Создаем функцию для создания таблицы шифрования
def create_vigenere_table(key):
    vigenere_table = []
    for i in range(len(alphabet)):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        row = []
        for j in range(len(alphabet)):
            row.append(shifted_alphabet[j])
        vigenere_table.append(row)
    return vigenere_table

# Создаем функцию для шифрования сообщения
def encrypt_vigenere(message, key):
    # Приводим ключ к нужной длине
    key_sequence = (key * (len(message) // len(key) + 1))[:len(message)]
    # Создаем таблицу шифрования
    vigenere_table = create_vigenere_table(key)
    # Шифруем сообщение
    encrypted_message = ""
    for i in range(len(message)):
        row_index = alphabet.index(key_sequence[i])
        col_index = alphabet.index(message[i])
        encrypted_message += vigenere_table[row_index][col_index]
    return encrypted_message

# Создаем функцию для расшифрования сообщения
def decrypt_vigenere(message, key):
    # Приводим ключ к нужной длине
    key_sequence = (key * (len(message) // len(key) + 1))[:len(message)]
    # Создаем таблицу шифрования
    vigenere_table = create_vigenere_table(key)
    # Расшифровываем сообщение
    decrypted_message = ""
    for i in range(len(message)):
        row_index = alphabet.index(key_sequence[i])
        col_index = vigenere_table[row_index].index(message[i])
        decrypted_message += alphabet[col_index]
    return decrypted_message

# Создаем функцию для анализа частотности символов
def analyze_frequency(message):
    frequency = {}
    for char in message:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Создаем исходные сообщения и ключ
initiator_message = "привет"
responder_message = "мир"
merged_message = initiator_message + responder_message
key = "секрет"

# Шифруем сообщение
encrypted_message = encrypt_vigenere(merged_message, key)

# Расшифровываем сообщение
decrypted_message = decrypt_vigenere(encrypted_message, key)

# Анализируем частотность символов в зашифрованном сообщении
frequency = analyze_frequency(encrypted_message)

# Выводим результаты
print("Исходное сообщение инициатора:", initiator_message)
print("Исходное сообщение ответчика:", responder_message)
print("Слияние сообщений:", merged_message)
print("Зашифрованное сообщение:", encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
print("Частотность символов в зашифрованном сообщении:")
for char, count in frequency.items():
    print(char, count)