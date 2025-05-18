from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Підраховує кількість слів, що закінчуються заданим суфіксом.
        
        Args:
            pattern (str): Суфікс для пошуку.
            
        Returns:
            int: Кількість слів із заданим суфіксом.
            
        Raises:
            TypeError: Якщо pattern не є рядком.
        """
        if not isinstance(pattern, str):
            raise TypeError("Suffix pattern must be a string")
        
        if pattern == "":
            return self.size()  # Порожній суфікс є у всіх словах
        
        # Зберемо всі слова з дерева
        words = []
        
        def collect_words(node, prefix):
            if node.is_end_of_word:
                words.append(prefix)
            
            for char, child in node.children.items():
                collect_words(child, prefix + char)
        
        collect_words(self.root, "")
        
        # Підрахуємо кількість слів із заданим суфіксом
        count = 0
        for word in words:
            if word.endswith(pattern):
                count += 1
        
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Перевіряє, чи є слова з заданим префіксом.
        
        Args:
            prefix (str): Префікс для перевірки.
            
        Returns:
            bool: True, якщо є хоча б одне слово з цим префіксом, 
                 False в іншому випадку.
                 
        Raises:
            TypeError: Якщо prefix не є рядком.
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True  # Знайшли весь префікс


if __name__ == "__main__":
    # Тести для методів count_words_with_suffix та has_prefix
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print("\nТестування count_words_with_suffix:")
    print(f"Слова з суфіксом 'e': {trie.count_words_with_suffix('e')} (очікується 1)")
    print(f"Слова з суфіксом 'ion': {trie.count_words_with_suffix('ion')} (очікується 1)")
    print(f"Слова з суфіксом 'a': {trie.count_words_with_suffix('a')} (очікується 1)")
    print(f"Слова з суфіксом 'at': {trie.count_words_with_suffix('at')} (очікується 1)")
    print(f"Слова з суфіксом 'le': {trie.count_words_with_suffix('le')} (очікується 1)")
    print(f"Слова з суфіксом 'z': {trie.count_words_with_suffix('z')} (очікується 0)")
    
    # Перевірка некоректних даних
    try:
        trie.count_words_with_suffix(123)
        print("Помилка: має бути викинуто виняток TypeError для неправильного типу суфікса")
    except TypeError as e:
        print(f"Правильно оброблено помилку типу суфікса: {e}")

    # Перевірка наявності префікса
    print("\nТестування has_prefix:")
    print(f"Префікс 'app': {trie.has_prefix('app')} (очікується True)")
    print(f"Префікс 'bat': {trie.has_prefix('bat')} (очікується False)")
    print(f"Префікс 'ban': {trie.has_prefix('ban')} (очікується True)")
    print(f"Префікс 'ca': {trie.has_prefix('ca')} (очікується True)")
    print(f"Префікс 'appl': {trie.has_prefix('appl')} (очікується True)")
    print(f"Префікс 'z': {trie.has_prefix('z')} (очікується False)")
    
    # Перевірка некоректних даних
    try:
        trie.has_prefix(123)
        print("Помилка: має бути викинуто виняток TypeError для неправильного типу префікса")
    except TypeError as e:
        print(f"Правильно оброблено помилку типу префікса: {e}")
    
    # Перевірка за допомогою assert
    print("\nПеревірка за допомогою assert:")
    try:
        assert trie.count_words_with_suffix("e") == 1, "Помилка для суфікса 'e'"
        assert trie.count_words_with_suffix("ion") == 1, "Помилка для суфікса 'ion'"
        assert trie.count_words_with_suffix("a") == 1, "Помилка для суфікса 'a'"
        assert trie.count_words_with_suffix("at") == 1, "Помилка для суфікса 'at'"
        assert trie.count_words_with_suffix("z") == 0, "Помилка для суфікса 'z'"
        
        assert trie.has_prefix("app") == True, "Помилка для префікса 'app'"
        assert trie.has_prefix("bat") == False, "Помилка для префікса 'bat'"
        assert trie.has_prefix("ban") == True, "Помилка для префікса 'ban'"
        assert trie.has_prefix("ca") == True, "Помилка для префікса 'ca'"
        assert trie.has_prefix("z") == False, "Помилка для префікса 'z'"
        
        print("Всі тести пройдено успішно!")
    except AssertionError as e:
        print(f"Помилка при перевірці: {e}")