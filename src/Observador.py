from typing import List, Callable

# Classes dos Observadores
class TotalWordObserver:
    def update(self, word_list):
        total_words = len(word_list)
        print(f'Total de palavras: {total_words}')

class EvenLengthWordObserver:
    def update(self, word_list):
        even_lenght_words = [word for word in word_list if len(word) % 2 == 0]
        print(f'Palavras com quantidade par de caracteres: {len(even_lenght_words)}')

class CaptalizedWordObserver:
    def update(self, word_list):
        captalized_words = [word for word in word_list if word.istitle()]
        print(f'Palavras começadas com maiúsculas: {len(captalized_words)}')