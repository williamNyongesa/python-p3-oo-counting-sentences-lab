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
        sentences = re.split(r'[.!?]', self.value)
        # Filter out empty strings and whitespace-only strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
