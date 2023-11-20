import unittest
from io import StringIO
from unittest.mock import patch
from src.Observador import TotalWordObserver, EvenLengthWordObserver, CaptalizedWordObserver
from src.Observavel import WordCounter

class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordCounter()

    def test_total_word_observer(self):
        total_word_observer = TotalWordObserver()
        self.word_counter.add_observer(total_word_observer)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.word_counter.process_input("Isso é um teste")
            expected_output = "Total de palavras: 4\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_even_length_word_observer(self):
        even_length_word_observer = EvenLengthWordObserver()
        self.word_counter.add_observer(even_length_word_observer)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.word_counter.process_input("Palavras com tamanhos pares")
            expected_output = "Palavras com quantidade par de caracteres: 2\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_capitalized_word_observer(self):
        capitalized_word_observer = CaptalizedWordObserver()
        self.word_counter.add_observer(capitalized_word_observer)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.word_counter.process_input("Começadas com Maiúsculas")
            expected_output = "Palavras começadas com maiúsculas: 2\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if _name_ == '_main_':
    unittest.main()