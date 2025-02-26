from lexer import lexer, Token, TOKEN_TYPES

class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def __repr__(self):
        return f'ASTNode({self.type}, {self.value}, {self.children})'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        return self.program()

    def program(self):
        node = ASTNode('PROGRAM')
        while self.current_token_index < len(self.tokens):
            node.children.append(self.statement())
        return node

    def statement(self):
        token = self.current_token()
        if token.type == TOKEN_TYPES['BET']:
            return self.print_statement()
        elif token.type == TOKEN_TYPES['CAP']:
            return self.assignment_statement()
        elif token.type == TOKEN_TYPES['SUS']:
            return self.conditional_statement()
        else:
            self.error(f"Unexpected token: {token}")

    def print_statement(self):
        self.eat(TOKEN_TYPES['BET'])
        expr = self.expression()
        return ASTNode('PRINT', expr)

    def assignment_statement(self):
        self.eat(TOKEN_TYPES['CAP'])
        identifier = self.current_token().value
        self.eat(TOKEN_TYPES['IDENTIFIER'])
        self.eat(TOKEN_TYPES['EQUAL'])
        expr = self.expression()
        node = ASTNode('ASSIGN', identifier)
        node.children.append(expr)
        return node

    def conditional_statement(self):
        self.eat(TOKEN_TYPES['SUS'])
        condition = self.expression()
        self.eat(TOKEN_TYPES['BRACE'])
        true_branch = self.statement_list()
        self.eat(TOKEN_TYPES['BRACE'])
        self.eat(TOKEN_TYPES['NOSUS'])
        self.eat(TOKEN_TYPES['BRACE'])
        false_branch = self.statement_list()
        self.eat(TOKEN_TYPES['BRACE'])
        node = ASTNode('IF', condition)
        node.children.append(true_branch)
        node.children.append(false_branch)
        return node

    def statement_list(self):
        node = ASTNode('STATEMENT_LIST')
        while self.current_token().type != TOKEN_TYPES['BRACE']:
            node.children.append(self.statement())
        return node

    def expression(self):
        node = self.term()
        while self.current_token().type in (TOKEN_TYPES['OPERATOR'],):
            token = self.current_token()
            if token.value in ('+', '-'):
                self.eat(TOKEN_TYPES['OPERATOR'])
                node = ASTNode(token.value, node)
                node.children.append(self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current_token().type in (TOKEN_TYPES['OPERATOR'],):
            token = self.current_token()
            if token.value in ('*', '/'):
                self.eat(TOKEN_TYPES['OPERATOR'])
                node = ASTNode(token.value, node)
                node.children.append(self.factor())
        return node

    def factor(self):
        token = self.current_token()
        if token.type == TOKEN_TYPES['NUMBER']:
            self.eat(TOKEN_TYPES['NUMBER'])
            return ASTNode('NUMBER', token.value)
        elif token.type == TOKEN_TYPES['IDENTIFIER']:
            self.eat(TOKEN_TYPES['IDENTIFIER'])
            return ASTNode('IDENTIFIER', token.value)
        elif token.type == TOKEN_TYPES['PAREN'] and token.value == '(':
            self.eat(TOKEN_TYPES['PAREN'])
            node = self.expression()
            self.eat(TOKEN_TYPES['PAREN'])
            return node
        elif token.type == TOKEN_TYPES['STRING']:
            self.eat(TOKEN_TYPES['STRING'])
            return ASTNode('STRING', token.value)
        else:
            self.error(f"Unexpected token: {token}")

    def eat(self, token_type):
        if self.current_token().type == token_type:
            self.current_token_index += 1
        else:
            self.error(f"Expected token type {token_type}, but got {self.current_token().type}")

    def current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return Token(TOKEN_TYPES['UNKNOWN'], '')

    def error(self, message):
        raise Exception(f"Parse error: {message}")

# Example usage
if __name__ == "__main__":
    code = 'BET "Hello, World!" CAP x = 42 SUS x { BET "x is 42" } NOSUS { BET "x is not 42" }'
    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
