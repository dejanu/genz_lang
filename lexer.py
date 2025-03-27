import re

# Token types
TOKEN_TYPES = {
    'BET': 'BET',
    'CAP': 'CAP',
    'SUS': 'SUS',
    'NOSUS': 'NOSUS',
    'IDENTIFIER': 'IDENTIFIER',
    'NUMBER': 'NUMBER',
    'STRING': 'STRING',
    'OPERATOR': 'OPERATOR',
    'PAREN': 'PAREN',
    'BRACE': 'BRACE',
    'EQUAL': 'EQUAL',
    'WHITESPACE': 'WHITESPACE',
    'UNKNOWN': 'UNKNOWN',
    'COMPARISON': 'COMPARISON'  # Add a new token type for comparison operators
}

# Token regex patterns
TOKEN_REGEX = [
    (r'BET', TOKEN_TYPES['BET']),
    (r'CAP', TOKEN_TYPES['CAP']),
    (r'SUS', TOKEN_TYPES['SUS']),
    (r'NOSUS', TOKEN_TYPES['NOSUS']),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', TOKEN_TYPES['IDENTIFIER']),
    (r'\d+', TOKEN_TYPES['NUMBER']),
    (r'"[^"]*"', TOKEN_TYPES['STRING']),
    (r'[+\-*/]', TOKEN_TYPES['OPERATOR']),
    (r'[()]', TOKEN_TYPES['PAREN']),
    (r'[{}]', TOKEN_TYPES['BRACE']),
    (r'=', TOKEN_TYPES['EQUAL']),
    (r'\s+', TOKEN_TYPES['WHITESPACE']),
    (r'==|!=|>=|<=|>|<', TOKEN_TYPES['COMPARISON'])  # Add regex for comparison operators
]

class Token:
    def __init__(self, type, value):
        """
        Initialize a new instance of the class.

        Args:
            type (str): The type of the token.
            value (str): The value of the token.
        """
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

# Update the lexer to handle comments
def lexer(input_code):
    """
    Tokenizes the given input code into a list of tokens.

    Args:
        input_code (str): The source code to be tokenized.

    Returns:
        list: A list of Token objects representing the tokenized input code.

    The function uses regular expressions defined in TOKEN_REGEX to match
    patterns in the input code and classify them into different token types.
    Whitespace tokens are ignored. If no match is found for a segment of the
    input code, it is classified as an UNKNOWN token.
    """
    tokens = []
    lines = input_code.splitlines()
    for line in lines:
        if '#' in line:
            line = line.split('#', 1)[0]  # Remove everything after the `#` symbol
        tokens.extend(tokenize_line(line))
    return tokens

def tokenize_line(line):
    # Tokenize a single line of code
    tokens = []
    while line:
        match = None
        for token_regex, token_type in TOKEN_REGEX:
            regex = re.compile(token_regex)
            match = regex.match(line)
            if match:
                value = match.group(0)
                if token_type != TOKEN_TYPES['WHITESPACE']:
                    tokens.append(Token(token_type, value))
                line = line[len(value):]
                break
        if not match:
            tokens.append(Token(TOKEN_TYPES['UNKNOWN'], line[0]))
            line = line[1:]
    return tokens

# Example usage
if __name__ == "__main__":
    code = 'BET "Hello, World!" CAP x = 42 SUS x { BET "x is 42" } NOSUS { BET "x is not 42" }'
    tokens = lexer(code)
    for token in tokens:
        print(token)
