class Decipher:
    def __init__(self, data='', password=''):
        self.data = data
        self.password = password
        self.result = False

    def decipher_password(self):
        # For authentication(Deciphering your password)..
        helper = self.data.split('*/*/')
        count, separator, compare, helper_list = 1, '', '', []
        for i in helper[0]:
            if i == '%':
                helper_list.append(int(separator) - count)
                count += 1
                separator = ''
                continue
            separator += i
        for i in helper_list:
            compare += chr(i)
        if compare == self.password:
            self.result = True
        return self.result, helper

    def decipher_message(self, helper):
        # Deciphering your message
        helper_list = []
        helper_msg = helper[1].split('@*@')
        message = str(helper_msg[0])
        size = int(helper_msg[1])
        separator, deciphered = '', ''
        for i in message:
            if i == '@':
                helper_list.append(int(separator) - size)
                size -= 1
                separator = ''
                continue
            separator += i
        for i in helper_list:
            deciphered += chr(i)
        return deciphered


if __name__ == '__main__':
    pass
