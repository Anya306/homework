
class Atbash:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self):
        lowercase_code = {x: y for x, y in zip(self.alphabet, self.alphabet[::-1])}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, self.alphabet[::-1])}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])


cipher = Atbash()
line = input()
while line != '.':
    print(cipher.encode(line))
    line = input()


class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {x: y for y, x in self._encode.items()}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


key = int(input('Введите ключ:'))
cipher = Caesar(key)
line = input()
while line:
    print(cipher.decode(line))
    line = input()


class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # TODO

    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {x: y for y, x in self._encode.items()}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, text):
        return ''.join([self._decode.get(char, char) for char in text])


s = input()
s = s.lower()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_dict = dict()
for i in alphabet:
    alphabet_dict.setdefault(i, 0)
for j in range(len(s)):
    if s[j] in alphabet:
        alphabet_dict[s[j]] += 1
print(alphabet_dict)
sorted_dict = dict(sorted(alphabet_dict.items(), key=lambda x: x[1]))
print(sorted_dict)
mas = list(sorted_dict.keys())
print(list(sorted_dict.keys()))
dict_nb = {'а': 3, 'б': 21, 'в': 9, 'г': 19, 'д': 13, 'е': 2, 'ё': 33, 'ж': 25, 'з': 20, 'и': 4, 'й': 23, 'к': 11,
           'л': 10, 'м': 12, 'н': 5, 'о': 1, 'п': 14, 'р': 8, 'с': 7, 'т': 6, 'у': 15, 'ф': 31, 'х': 24, 'ц': 28,
           'ч': 22, 'ш': 26, 'щ': 29, 'ъ': 32, 'ы': 17, 'ь': 18, 'э': 30, 'ю': 27, 'я': 16}
key = []
for z in alphabet:
    key.append(mas[-dict_nb[z]])
cipher = Monoalphabet(key)
line = input()
while line:
    print(cipher.encode(line))
    line = input()
