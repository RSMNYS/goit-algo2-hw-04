class TrieNode:
    def __init__(self):
        self.children = {}  # Словник для зберігання дочірніх вузлів
        self.is_end_of_word = False  # Флаг, що позначає кінець слова
        self.value = None  # Значення, пов'язане зі словом


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Кореневий вузол дерева
        self._size = 0  # Лічильник кількості слів у дереві

    def put(self, key, value):
        """Додає слово в Trie з відповідним значенням."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        # Якщо це новий кінець слова, збільшуємо розмір
        if not current.is_end_of_word:
            self._size += 1

        current.is_end_of_word = True
        current.value = value

    def get(self, key):
        """Повертає значення, пов'язане зі словом, якщо воно є в дереві."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]

        return current.value if current.is_end_of_word else None

    def contains(self, key):
        """Перевіряє, чи є слово в дереві."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        current = self.root
        for char in key:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.is_end_of_word

    def size(self):
        """Повертає кількість слів у дереві."""
        return self._size

    def delete(self, key):
        """Видаляє слово з дерева, якщо воно там є."""
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        def _delete(node, key, depth):
            # Якщо досягли кінця ключа
            if depth == len(key):
                # Якщо це кінець слова, відзначаємо його як не кінець
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    node.value = None
                    self._size -= 1
                    return len(node.children) == 0  # Повертаємо True, якщо вузол може бути видалений
                return False  # Не видаляємо, якщо це не кінець слова

            char = key[depth]
            if char not in node.children:
                return False  # Слово не знайдено
            
            # Рекурсивно видаляємо дочірній вузол
            should_delete_child = _delete(node.children[char], key, depth + 1)
            
            # Якщо дочірній вузол можна видалити
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False

        _delete(self.root, key, 0)

    def get_all_with_prefix(self, prefix):
        """Повертає всі слова з заданим префіксом."""
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")

        result = []
        current = self.root

        # Знаходимо вузол, який відповідає префіксу
        for char in prefix:
            if char not in current.children:
                return result  # Префікс не знайдений
            current = current.children[char]

        # Збираємо всі слова, починаючи з цього вузла
        def collect_words(node, current_prefix):
            if node.is_end_of_word:
                result.append((current_prefix, node.value))
            
            for char, child in node.children.items():
                collect_words(child, current_prefix + char)

        collect_words(current, prefix)
        return result