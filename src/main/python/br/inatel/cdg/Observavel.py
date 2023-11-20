from typing import List, Callable

# Classe do assunto Observável
class WordCounter:
    def _init_(self):
        self.observers = []
        self.world_list = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.world_list)

    def process_input(self, input_text):
        self.world_list = input_text.split()
        self.notify_observer()