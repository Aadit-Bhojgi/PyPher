class Cipher:
    def __init__(self, data='', password=''):
        self.data = str(data)
        self.password = str(password)
        self.size = len(self.data)
        self.cipher_data = ''

    def cipher(self):
        index = 1
        for i in self.password:
            self.cipher_data += str(ord(i) + index) + '%'
            index += 1
        self.cipher_data += '*/*/'
        for i in self.data:
            self.cipher_data += str(ord(i) + self.size) + '@'
            self.size -= 1
        self.cipher_data += '@*@' + str(len(self.data))
        return self.cipher_data


if __name__ == '__main__':
    pass
