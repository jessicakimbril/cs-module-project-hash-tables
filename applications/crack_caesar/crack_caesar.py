# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

en_alpha = 'abcdefghijklmnopqrstuvwxyz'
first_letter = ord(en_alpha[0])

def to_number(letter):
    number = ord(letter)
    return number - first_letter

def count_letters(message):
    letter_count = 0 * len(en_alpha)

    for letter in message:
        if letter in en_alpha:
            position = to_number(letter)
            letter_count[position] += 1

    return letter_count

f = open('cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt', 'r')
message = f.read()
# print(message)

plain_letter_count = count_letters(message)
print(plain_letter_count)
