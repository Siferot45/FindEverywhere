from WordsFinder import WordsFinder


# Создание объекта WordsFinder для одного файла
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Получение всех слов из файла
print(finder2.find('TEXT'))     # Поиск первого вхождения слова 'TEXT'
print(finder2.count('teXT'))    # Подсчёт вхождений слова 'teXT'
print()

# Анализ текста "Mother Goose - Monday’s Child"
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())  # Получение всех слов
print(finder1.find('Child'))    # Поиск слова 'Child'
print(finder1.count('Child'))   # Подсчёт слова 'Child'
print()

# Анализ текста "Rudyard Kipling - If"
finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())  # Получение всех слов
print(finder1.find('if'))       # Поиск слова 'if'
print(finder1.count('if'))      # Подсчёт слова 'if'
print()

# Анализ текста "Walt Whitman - O Captain! My Captain!"
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())  # Получение всех слов
print(finder1.find('captain'))  # Поиск слова 'captain'
print(finder1.count('captain')) # Подсчёт слова 'captain'
print()

# Анализ нескольких файлов одновременно
finder1 = WordsFinder(
    'Walt Whitman - O Captain! My Captain!.txt',
    'Rudyard Kipling - If.txt',
    'Mother Goose - Monday’s Child.txt'
)
print(finder1.get_all_words())  # Получение всех слов из всех файлов
print(finder1.find('the'))      # Поиск слова 'the'
print(finder1.count('the'))     # Подсчёт слова 'the'

