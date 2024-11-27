import unittest
from config_parser import ConfigParser


class TestConfigParser(unittest.TestCase):

    def setUp(self):
        # Создаем экземпляр парсера перед каждым тестом
        self.parser = ConfigParser(debug=False)

    def test_config1(self):
        input_text = """
% Конфигурация для теста
(define a 10)
(define b 20)
struct {
    sum = |+ a b|,
    difference = |- a b|
}
"""
        expected_output = """
<config>
  <sum value="30" />
  <difference value="-10" />
</config>
"""
        result = self.parser.parse(input_text.strip())
        self.assertEqual(result.strip(), expected_output.strip())

    def test_config2(self):
        input_text = """
% Конфигурация маршрутизатора
(define router_name 'Router1')
(define ip_address '192.168.1.1')
(define subnet_mask '255.255.255.0')
struct {
    hostname = router_name,
    ip = ip_address,
    subnet = subnet_mask
}
"""
        expected_output = """
<config>
  <hostname value="Router1" />
  <ip value="192.168.1.1" />
  <subnet value="255.255.255.0" />
</config>
"""
        result = self.parser.parse(input_text.strip())
        self.assertEqual(result.strip(), expected_output.strip())

    def test_config3(self):
        input_text = """
% Конфигурация базы данных
(define db_name 'my_database')
(define db_user 'admin')
(define db_password 'securepassword')
(define db_host 'localhost')
(define db_port 5432)
struct {
    database = db_name,
    user = db_user,
    password = db_password,
    host = db_host,
    port = db_port
}
"""
        expected_output = """
<config>
  <database value="my_database" />
  <user value="admin" />
  <password value="securepassword" />
  <host value="localhost" />
  <port value="5432" />
</config>
"""
        result = self.parser.parse(input_text.strip())
        self.assertEqual(result.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
