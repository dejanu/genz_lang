import unittest
from lexer import Token

class TestToken(unittest.TestCase):
    def test_token_initialization(self):
        token = Token(type="IDENTIFIER", value="x")
        self.assertEqual(token.type, "IDENTIFIER")
        self.assertEqual(token.value, "x")

    def test_token_representation(self):
        token = Token(type="NUMBER", value="42")
        self.assertEqual(repr(token), "Token(NUMBER, 42)")

if __name__ == '__main__':
    unittest.main()