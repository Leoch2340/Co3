# Вариант 28

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

Этот проект реализован на Python, и для его работы необходимо установить Python 3.x. Для работы с проектом достаточно клонировать репозиторий и запустить скрипт.

### Установка и запуск

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://example.com/config_parser.git
    cd config_parser
    ```

2. **Запустите скрипт**:
    Пример запуска парсера:
    ```bash
    python3 config_parser.py < input.txt
    ```

    В данном случае `input.txt` — это файл с конфигурационными данными, который будет обработан скриптом. Результатом выполнения будет XML-выход, который будет выведен в стандартный поток вывода.

### Пример работы с отладочным выводом

Чтобы включить отладочный вывод, нужно установить флаг `debug=True` при создании экземпляра парсера. Например:

```python
parser = ConfigParser(debug=True)
output_xml = parser.parse(input_text)
