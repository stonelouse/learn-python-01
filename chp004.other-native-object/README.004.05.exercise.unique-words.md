# 4. Other Native Objects

- [4. Other Native Objects](#4-other-native-objects)
  - [4.5 Application: Unique Words](#45-application-unique-words)
  - [Exercise 4.5.1.1](#exercise-4511)
  - [Exercise 4.5.1.2 - `collections.Counter()`](#exercise-4512---collectionscounter)

## 4.5 Application: Unique Words

- continued see [hartl](../README.md#hartl) p.116

- see [`p004.05.count-unique-words.py`](./p004.05.count-unique-words.py)

- Result

  ``` plain text
  {'Let': 1, 'me': 2, 'not': 4, 'to': 4, 'the': 4, 'marriage': 1, 'of': 2, 'true': 1, 'minds': 1, 'Admit': 1, 'impediments': 1, 'Love': 3, 'is': 4, 'love': 1, 'Which': 1, 'alters': 2, 'when': 1, 'it': 3, 'alteration': 1, 'finds': 1, 'Or': 1, 'bends': 1, 'with': 2, 'remover': 1, 'remove': 1, 'O': 1, 'no': 2, 'an': 1, 'ever': 2, 'fixed': 1, 'mark': 1, 'That': 1, 'looks': 1, 'on': 1, 'tempests': 1, 'and': 4, 'never': 2, 'shaken': 1, 'It': 1, 'star': 1, 'every': 1, 'wand': 1, 'ring': 1, 'bark': 1, 'Whose': 1, 'worth': 1, 's': 4, 'unknown': 1, 'although': 1, 'his': 3, 'height': 1, 'be': 2, 'taken': 1, 'time': 1, 'fool': 1, 'though': 1, 'rosy': 1, 'lips': 1, 'cheeks': 1, 'Within': 1, 'bending': 1, 'sickle': 1, 'compass': 1, 'come': 1, 'brief': 1, 'hours': 1, 'weeks': 1, 'But': 1, 'bears': 1, 'out': 1, 'even': 1, 'edge': 1, 'doom': 1, 'If': 1, 'this': 1, 'error': 1, 'upon': 1, 'proved': 1, 'I': 1, 'writ': 1, 'nor': 1, 'man': 1, 'loved': 1}
  ```

## Exercise 4.5.1.1

- see [p004.05.count-unique-words.ex-4-5-1-1.py](./p004.05.count-unique-words.ex-4-5-1-1.py)

- Result

  ``` plain text
  {'Let': 1, 'me': 2, 'not': 4, 'to': 4, 'the': 4, 'marriage': 1, 'of': 2, 'true': 1, 'minds': 1, 'Admit': 1, 'impediments': 1, 'Love': 2, 'is': 4, 'love': 1, 'Which': 1, 'alters': 2, 'when': 1, 'it': 3, 'alteration': 1, 'finds': 1, 'Or': 1, 'bends': 1, 'with': 2, 'remover': 1, 'remove': 1, 'O': 1, 'no': 2, 'an': 1, 'ever': 2, 'fixed': 1, 'mark': 1, 'That': 1, 'looks': 1, 'on': 1, 'tempests': 1, 'and': 4, 'never': 2, 'shaken': 1, 'It': 1, 'star': 1, 'every': 1, "wand'ring": 1, 'bark': 1, 'Whose': 1, "worth's": 1, 'unknown': 1, 'although': 1, 'his': 3, 'height': 1, 'be': 2, 'taken': 1, "Love's": 1, "time's": 1, 'fool': 1, 'though': 1, 'rosy': 1, 'lips': 1, 'cheeks': 1, 'Within': 1, 'bending': 1, "sickle's": 1, 'compass': 1, 'come': 1, 'brief': 1, 'hours': 1, 'weeks': 1, 'But': 1, 'bears': 1, 'out': 1, 'even': 1, 'edge': 1, 'doom': 1, 'If': 1, 'this': 1, 'error': 1, 'upon': 1, 'proved': 1, 'I': 1, 'writ': 1, 'nor': 1, 'man': 1, 'loved': 1}
  ```

## Exercise 4.5.1.2 - `collections.Counter()`

- see [p004.05.count-unique-words.ex-4-5-1-2.py](./p004.05.count-unique-words.ex-4-5-1-2.py)

- see <https://docs.python.org/3/library/collections.html#collections.Counter>

- Result

  ``` plain text
  Counter({'not': 4, 'to': 4, 'the': 4, 'is': 4, 'and': 4, 'it': 3, 'his': 3, 'me': 2, 'of': 2, 'Love': 2, 'alters': 2, 'with': 2, 'no': 2, 'ever': 2, 'never': 2, 'be': 2, 'Let': 1, 'marriage': 1, 'true': 1, 'minds': 1, 'Admit': 1, 'impediments': 1, 'love': 1, 'Which': 1, 'when': 1, 'alteration': 1, 'finds': 1, 'Or': 1, 'bends': 1, 'remover': 1, 'remove': 1, 'O': 1, 'an': 1, 'fixed': 1, 'mark': 1, 'That': 1, 'looks': 1, 'on': 1, 'tempests': 1, 'shaken': 1, 'It': 1, 'star': 1, 'every': 1, "wand'ring": 1, 'bark': 1, 'Whose': 1, "worth's": 1, 'unknown': 1, 'although': 1, 'height': 1, 'taken': 1, "Love's": 1, "time's": 1, 'fool': 1, 'though': 1, 'rosy': 1, 'lips': 1, 'cheeks': 1, 'Within': 1, 'bending': 1, "sickle's": 1, 'compass': 1, 'come': 1, 'brief': 1, 'hours': 1, 'weeks': 1, 'But': 1, 'bears': 1, 'out': 1, 'even': 1, 'edge': 1, 'doom': 1, 'If': 1, 'this': 1, 'error': 1, 'upon': 1, 'proved': 1, 'I': 1, 'writ': 1, 'nor': 1, 'man': 1, 'loved': 1})
  ```
