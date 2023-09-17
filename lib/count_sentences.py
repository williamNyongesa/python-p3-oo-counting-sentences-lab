class MyString:
    def __init__(self, value=""):
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [s.strip() for s in self.value.split('.') if s.strip()]
        sentences += [s.strip() for s in self.value.split('?') if s.strip()]
        sentences += [s.strip() for s in self.value.split('!') if s.strip()]

        if not isinstance(self.value, str):
            print("The value must be a string.")

        return len(sentences)
