from token import STAR


class WordsFinder:
    """
    Класс для работы с текстовыми файлами, позволяющий искать и подсчитывать слова в нескольких файлах.

    Атрибуты:
        file_names (tuple): Кортеж имён файлов, с которыми работает класс.

    Методы:
        get_all_words(): Извлекает все слова из заданных файлов и возвращает их в виде словаря.
        find(word): Находит первое вхождение слова в каждом файле.
        count(word): Подсчитывает количество вхождений слова в каждом файле.
    """

    def __init__(self, *file_names):
        """
        Инициализация объекта с указанными файлами.

        Аргументы:
            *file_names (str): Имена файлов, которые будут обрабатываться.
        """
        self.file_names = file_names

    def get_all_words(self):
        """
        Извлекает все слова из заданных файлов.

        Возвращает:
            dict: Словарь, где ключ — имя файла, значение — список всех слов из файла.
        """
        all_words = {}
        
        for file_name in self.file_names:
            with open(file_name) as file:
                
                text = file.read().lower()
                
                # Замена символов на пробелы
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(char, ' ')
                    
                words = text.split()
                all_words[file_name] = words
                
        return all_words

    def find(self, word):
        """
        Находит первое вхождение слова в каждом файле.

        Аргументы:
            word (str): Слово для поиска.

        Возвращает:
            dict: Словарь, где ключ — имя файла, значение — позиция первого вхождения (или None, если слово не найдено).
        """
        position = None
        find_position_word = {}
        
        for file_name, words in self.get_all_words().items():
            for posit, wor in enumerate(words, start=1):
                if word.lower() == wor:
                    position = posit
                    break
                
            find_position_word[file_name] = position
            
        return find_position_word

    def count(self, word):
        """
        Подсчитывает количество вхождений слова в каждом файле.

        Аргументы:
            word (str): Слово для подсчёта.

        Возвращает:
            dict: Словарь, где ключ — имя файла, значение — количество вхождений слова.
        """
        word = word.lower()
        counts = {}

        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word.lower())

        return counts

        
    






































