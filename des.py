from Crypto.Cipher import DES

#создаем ключ, добиваем его до 8 символов если он короче
k = str(input("key:"))
key = bytes(k, 'utf-8')
while len(key) % 8 != 0:
    key += b' '

# функция приведения строки в битовый вид- с добавлением нехватающих элементов до 8символов
def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text
    
#встроенный метод des
des = DES.new(key, DES.MODE_ECB)

a = str(input("message:"))

#str->bytes
b = bytes(a, 'utf-8')
padded_text = pad(b)

#encrypt
encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

#decrypt
data = des.decrypt(encrypted_text)
print(data)
