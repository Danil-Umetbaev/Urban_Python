class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = (file.read().lower().replace(',', '').replace('.', '')
                        .replace('=', '').replace('!', '').replace('?', '')
                        .replace(';', '').replace(':', '').replace(' - ', ''))
                list_words = text.split()
                all_words[file_name] = list_words
        return all_words

    def find(self, word):
        word_l = word.lower()
        for name, words in self.get_all_words().items():
            if word_l in words:
                return {name: words.index(word_l)+1}
        return None
    def count(self, word):
        word_l = word.lower()
        for name, words in self.get_all_words().items():
            if word_l in words:
                return {name: words.count(word_l)}
        return None

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего