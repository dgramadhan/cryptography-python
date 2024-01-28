key = 'testencrypt123'

def enc_subtitution (n, plaintext) :
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def dec_subtitution(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result

originaltext = 'we try to encryption this text'
ciphertext = enc_subtitution(13, originaltext)
plaintext = dec_subtitution(13, ciphertext)

print(originaltext)
print(ciphertext)
print(plaintext)