import string

from load_check_words import load_words, get_story_string, get_num_valid_words

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text

    def build_shift_dict(self, shift):
        def shift_func(letter_list, shift):
            letter_list_rotate = letter_list[shift:] + letter_list[:shift]
            ans = {}
            for k, v in zip(letter_list, letter_list_rotate):
                ans[k] = v  
            return ans

        assert shift >= 0 and shift < 26, 'Error: shift should be in [0, 26), but is {}'.format(shift)
        self.shift_dict = shift_func(list(string.ascii_lowercase), shift)
        self.shift_dict.update(shift_func(list(string.ascii_uppercase), shift))

    def apply_shift(self, shift):
        self.build_shift_dict(shift)
        ans = ''
        for x in self.message_text:
            if x in string.ascii_letters:
                ans += self.shift_dict[x]
            else:
                ans += x
        return ans

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        super().__init__(text)
        self.shift = shift

    def get_message_text_encrypted(self):
        self.message_text_encrypted = self.apply_shift(self.shift)
        return self.message_text_encrypted


class CiphertextMessage(Message):
    def __init__(self, text):
        super().__init__(text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        max_valid_words = 0
        best_shift = 0
        decrypted_message_text = ''
        for shift in range(26):
            text = self.apply_shift(shift)
            num_valid_words = get_num_valid_words(text, self.valid_words)

            if max_valid_words < num_valid_words:
                max_valid_words = num_valid_words
                best_shift = shift
                decrypted_message_text = text

        return (best_shift, decrypted_message_text)


if __name__ == '__main__':
   plaintext = PlaintextMessage('hello', 2)
   print('Expected Output: jgnnq')
   print('Actual Output:', plaintext.get_message_text_encrypted())

   ciphertext = CiphertextMessage('jgnnq')
   print('Expected Output:', (24, 'hello'))
   print('Actual Output:', ciphertext.decrypt_message())

    # test to decrypt story text
   story = get_story_string()
   print('\nEncrypted story:\n', story)
   
   cipher_story = CiphertextMessage(story)
   print('\nDecrypted story: \n', cipher_story.decrypt_message())
