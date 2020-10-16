from functools import reduce


class Encryption(object):

    def encrypt(self):
        pass

    def decrypt(self):
        pass


class Vigenere(Encryption):

    def __init__(self, key):
        '''
        :param key: string-type to shift/un-shift by
        '''
        if type(key) is not str:
            raise ValueError("Error. 'key' argument must be string-type")
        self.key = key

    def encrypt(self, plaintext):
        '''
        :param plaintext: string-type to encode/encrypt
        :return: string-type encrypted text
        '''
        if type(plaintext) is not str:
            raise ValueError("Error. 'plaintext' argument given is not of String type.")
        ciphertext = ''
        for letter in range(len(plaintext)):
            ciphertext += chr(ord(plaintext[letter]) + ord(self.key[letter % len(self.key)]))
        return ciphertext

    def decrypt(self, ciphertext):
        '''
        :param ciphertext: string-type to decode/decrypt
        :return: string-type decoded/decrypted text
        '''
        if type(ciphertext) is not str:
            raise ValueError("Error. 'ciphertext' argument given is not of String type.")
        plaintext = ''
        for letter in range(len(ciphertext)):
            plaintext += chr(ord(ciphertext[letter]) - ord(self.key[letter % len(self.key)]))
        return plaintext


class Caesar(Encryption):

    def __init__(self, key):
        '''
        :param key: int-type to shift/un-shift by
        '''
        if type(key) is not int:
            raise ValueError("Error. 'key' argument given is not of Integer type.")
        elif key < 1:
            raise ValueError("Error. 'key' argument given is 0 or negative.")
        self.key = key

    def encrypt(self, plaintext, key=None):
        '''

        :param plaintext: string-type to encode/encrypt
        :param key: int-type to shift-up by. User assignment is optional, self.key set as default.
        :return: string-type encoded/encrypted text

        '''
        if type(plaintext) is not str:
            raise ValueError("Error. 'plaintext' argument given is not of String type.")
        if type(key) is not None:
            key = self.key
        return convstring(list(map(lambda l: chr(ord(l) + key), list(plaintext))))

    def decrypt(self, ciphertext, key=None):
        '''

        :param ciphertext: string-type to decode/decrypt
        :param key: int-type to shift-down by.
        :return: string-type decoded/decrypted text

        '''
        if type(ciphertext) is not str:
            raise ValueError("Error. 'ciphertext' argument given is not of String type.")
        if type(key) is not None:
            key = self.key

        return convstring(list(map(lambda l: chr(ord(l) - key), list(ciphertext))))


def convstring(lst):
    '''
    :param lst: list-type of chars
    :return: string-type of connected 'lst' members.
    '''
    return reduce(lambda a, b: a + b, lst)
    return ''.join(lst)
    # note: check of which options above is more efficient
