# Вариант 29

## 1. Общее описание

Этот проект реализует парсер для обработки текстовых конфигурационных файлов. Конфигурация описана с использованием определённых структур и выражений. Парсер анализирует текстовые данные, извлекает переменные, вычисляет выражения и генерирует XML-выход. Процесс парсинга включает обработку следующих конструкций:

- Определение переменных с помощью `(define)`.
- Структуры с множественными параметрами, представленные через `struct { ... }`.
- Выражения, включающие арифметические операции и вызовы функций, таких как `chr()`.

Парсер также поддерживает отладочный режим для вывода промежуточных шагов обработки.

## 2. Описание всех функций и настроек

### Классы и методы

#### `ConfigParser`

Класс парсера конфигурации.

- **Методы**:
  - `__init__(self, debug=False)`:
    Конструктор класса. Инициализирует парсер с возможностью отладки. Принимает флаг `debug`, который контролирует вывод отладочной информации.
  
  - `parse(self, input_text)`:
    Основной метод для парсинга текста конфигурации. Принимает на вход текст в виде строки и возвращает строку с XML-выходом. Пропускает комментарии, обрабатывает определения переменных и структуры.
  
  - `handle_struct(self, lines, start_index)`:
    Обрабатывает структуру (структуры данных), начиная с указанной строки. Возвращает XML-представление содержимого структуры.
  
  - `handle_dict(self, dict_content)`:
    Преобразует содержимое структуры в XML-формат. Проверяет корректность пар ключ-значение.
  
  - `evaluate(self, expression)`:
    Оценивает выражения. Поддерживает:
    - Цифры
    - Строки в одинарных кавычках
    - Переменные
    - Арифметические операции (`+`, `-`)
    - Вызовы функции `chr()`

### Прочие параметры и настройки:

- **debug**: флаг для включения/выключения отладочного режима. Включение этого флага выводит дополнительную информацию о процессе парсинга и генерации XML.

## 3. Описание команд для сборки проекта

 **Запустите скрипт**:
    Пример запуска парсера:
    ```
    python3 config_parser.py < input.txt
    ```

    Также есть файлы input2.txt и input3.txt

### Пример работы с отладочным выводом

Чтобы включить отладочный вывод, нужно установить флаг `debug=True` при создании экземпляра парсера. Например:

```python
parser = ConfigParser(debug=True)
output_xml = parser.parse(input_text)
```

## 4. Примеры использования в виде скриншотов, желательно в анимированном/видео формате, доступном для web-просмотра.

![изображение](https://github.com/user-attachments/assets/3ea420eb-a918-4319-b66f-d5fabf823c72)


Выполнение команды python3 config_parser.py < input.txt

![изображение](https://github.com/user-attachments/assets/78bd55a1-4a91-4ee7-9b93-55c88cdf9fca)

Выполнение команды python3 config_parser.py < input2.txt 

![изображение](https://github.com/user-attachments/assets/733f9b8c-c79c-4571-bab8-ce1358b62604)

Выполнение команды python3 config_parser.py < input3.txt 

## 5. Результаты прогона тестов 

![изображение](https://github.com/user-attachments/assets/a14619be-1247-4074-8183-004c2ff50340)

