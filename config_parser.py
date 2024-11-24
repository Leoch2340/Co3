import re
import sys


class ConfigParser:
    def __init__(self, debug=False):
        self.variables = {}
        self.debug = debug  # Флаг для отладки

    def parse(self, input_text):
        lines = input_text.splitlines()
        xml_output = "<config>\n"

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Отладочный вывод, если debug=True
            # if self.debug:
            #     print(f"Обрабатываем строку: {line}")  # Уберите или закомментируйте

            # Пропускаем комментарии
            if line.startswith('%'):
                i += 1
                continue

            # Обработка определения константы (define)
            match_define = re.match(r'\(define (\w+) (.+)\)', line)
            if match_define:
                name = match_define[1]
                value = self.evaluate(match_define[2])
                if value is not None:
                    self.variables[name] = value
                i += 1
                continue

            # Обработка структуры (struct) с многострочной поддержкой
            match_struct = re.match(r'struct \{', line)
            if match_struct:
                struct_content = self.handle_struct(lines, i)
                xml_output += struct_content  # Добавляем в итоговый XML
                # Перемещаем i после закрывающей скобки
                while i < len(lines) and '}' not in lines[i]:
                    i += 1
                i += 1
                continue

            # Ошибка синтаксиса
            print(f"Ошибка синтаксиса: некорректная строка '{line}'", file=sys.stderr)
            return None

        xml_output += "</config>\n"

        # Отладочный вывод, если debug=True
        # if self.debug:
        #     print(f"Генерация XML: {xml_output}")  # Уберите или закомментируйте

        return xml_output

    def handle_struct(self, lines, start_index):
        struct_content = ''
        i = start_index
        while i < len(lines):
            line = lines[i].strip()
            if '}' in line:
                break
            if '=' in line:
                struct_content += line + '\n'
            i += 1
        return self.handle_dict(struct_content)

    def handle_dict(self, dict_content):
        xml = ""
        items = dict_content.split(',')
        for item in items:
            item = item.strip()
            match = re.match(r'(\w+) = (.+)', item)
            if match:
                key = match[1]
                value = self.evaluate(match[2])
                if value is not None:
                    xml += f"  <{key} value=\"{value}\" />\n"
            else:
                print(f"Ошибка синтаксиса: некорректная пара ключ-значение '{item}'", file=sys.stderr)
                return None
        return xml

    def evaluate(self, expression):
        # Проверка на число
        if re.match(r'^\d+$', expression):
            return int(expression)

        # Проверка на строку
        match_str = re.match(r"'(.*)'", expression)
        if match_str:
            return match_str[1]

        # Если это переменная, пытаемся получить её значение
        if expression in self.variables:
            return self.variables[expression]

        # Проверка на вычисление выражений |+ a b| и |- a b|
        match_op = re.match(r'\|([\+\-]) (\w+) (\w+)\|', expression)
        if match_op:
            operator = match_op[1]
            var1 = match_op[2]
            var2 = match_op[3]
            if var1 in self.variables and var2 in self.variables:
                if operator == '+':
                    return self.variables[var1] + self.variables[var2]
                elif operator == '-':
                    return self.variables[var1] - self.variables[var2]
            else:
                print(f"Ошибка: переменные '{var1}' или '{var2}' не определены", file=sys.stderr)
                return None

        # Проверка на вызов функции chr
        match_chr = re.match(r'chr\((\w+)\)', expression)
        if match_chr:
            var_name = match_chr[1]
            if var_name in self.variables:
                return chr(self.variables[var_name])
            else:
                print(f"Ошибка: переменная '{var_name}' не определена", file=sys.stderr)
                return None

        print(f"Ошибка: не удалось вычислить выражение '{expression}'", file=sys.stderr)
        return None


def main():
    input_text = sys.stdin.read()
    #print(f"Входные данные: {input_text}")  # Отладочный вывод
    parser = ConfigParser(debug=False)  # Включение отладки
    output_xml = parser.parse(input_text)

    if output_xml:
        sys.stdout.write(output_xml)  # Вывод XML
    else:
        print("Ошибка в парсере. Выходной XML пуст.")


if __name__ == "__main__":
    main()

# python3 config_parser.py < input.txt