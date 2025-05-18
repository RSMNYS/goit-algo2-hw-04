from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Знаходить найдовший спільний префікс для всіх слів у масиві.
        
        Args:
            strings (list): Масив рядків.
            
        Returns:
            str: Найдовший спільний префікс або порожній рядок, якщо
                 спільного префіксу немає.
                 
        Raises:
            TypeError: Якщо параметр не є масивом рядків.
        """
        # Перевірка вхідних даних
        if not isinstance(strings, list):
            raise TypeError("Input must be a list of strings")
            
        if not strings:
            return ""
        
        if not all(isinstance(s, str) for s in strings):
            raise TypeError("All elements must be strings")
        
        if len(strings) == 1:
            return strings[0]
        
        # Використовуємо перше слово як базове
        prefix = ""
        first_word = strings[0]
        
        for i, char in enumerate(first_word):
            # Перевіряємо, чи всі слова мають цей префікс
            for s in strings:
                if i >= len(s) or s[i] != char:
                    return prefix
            
            prefix += char
        
        return prefix


if __name__ == "__main__":
    # Тести
    print("Тестування функції find_longest_common_word:")
    
    # Тест 1
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    result = trie.find_longest_common_word(strings)
    print(f"Тест 1: {strings} -> '{result}' (очікується 'fl')")
    assert result == "fl", f"Помилка у тесті 1: отримано '{result}', очікувалося 'fl'"

    # Тест 2
    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    result = trie.find_longest_common_word(strings)
    print(f"Тест 2: {strings} -> '{result}' (очікується 'inters')")
    assert result == "inters", f"Помилка у тесті 2: отримано '{result}', очікувалося 'inters'"

    # Тест 3
    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    result = trie.find_longest_common_word(strings)
    print(f"Тест 3: {strings} -> '{result}' (очікується '')")
    assert result == "", f"Помилка у тесті 3: отримано '{result}', очікувалося ''"

    # Тест 4 - порожній масив
    trie = LongestCommonWord()
    strings = []
    result = trie.find_longest_common_word(strings)
    print(f"Тест 4: {strings} -> '{result}' (очікується '')")
    assert result == "", f"Помилка у тесті 4: отримано '{result}', очікувалося ''"

    # Тест 5 - один елемент
    trie = LongestCommonWord()
    strings = ["apple"]
    result = trie.find_longest_common_word(strings)
    print(f"Тест 5: {strings} -> '{result}' (очікується 'apple')")
    assert result == "apple", f"Помилка у тесті 5: отримано '{result}', очікувалося 'apple'"

    # Тест 6 - некоректні вхідні дані
    trie = LongestCommonWord()
    try:
        strings = ["apple", 123, "banana"]
        trie.find_longest_common_word(strings)
        print("Помилка у тесті 6: не викинуто виняток TypeError")
    except TypeError as e:
        print(f"Тест 6: Правильно оброблено помилку типу: {e}")

    # Тест 7 - не масив
    trie = LongestCommonWord()
    try:
        strings = "not a list"
        trie.find_longest_common_word(strings)
        print("Помилка у тесті 7: не викинуто виняток TypeError")
    except TypeError as e:
        print(f"Тест 7: Правильно оброблено помилку типу: {e}")

    print("\nВсі тести завершено!")