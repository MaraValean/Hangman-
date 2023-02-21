class Validator:
    @staticmethod
    def validate_sentence(sentence):
        sentence = sentence.strip()
        words = sentence.split()
        for word in words:
            word = word.strip()
            if len(word)<3:
                return False
        return True
