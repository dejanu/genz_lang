from lexer import lexer, Token, TOKEN_TYPES

class ASTNode:
    def __init__(self, type, value=None, data_type=None):
        self.type = type
        self.value = value
        self.data_type = data_type  # Add data_type to enforce strong typing
        self.children = []

    def __repr__(self):
        return f'ASTNode({self.type}, {self.value}, {self.children})'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.symbol_table = {}  # Add a symbol table to track variable types

    def parse(self):
        return self.program()

    def program(self):
        node = ASTNode('PROGRAM')
        while self.current_token_index < len(self.tokens):
            statement = self.statement()
            if statement is not None:
                node.children.append(statement)
        return node

    def statement(self):
        token = self.current_token()
        if token.type == TOKEN_TYPES['BET']:
            return self.print_statement()
        elif token.type == TOKEN_TYPES['CAP']:
            return self.assignment_statement()
        elif token.type == TOKEN_TYPES['SUS']:
            return self.conditional_statement()
        elif token.type == TOKEN_TYPES['UNKNOWN']:
            # Ignore comments or unknown tokens
            self.eat(TOKEN_TYPES['UNKNOWN'])
            return None
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
        # Store the type of the variable in the symbol table
        self.symbol_table[identifier] = expr.data_type
        node = ASTNode('ASSIGN', identifier, expr.data_type)
        node.children.append(expr)
        return node

    def conditional_statement(self):
        self.eat(TOKEN_TYPES['SUS'])
        condition = self.comparison()
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
            statement = self.statement()
            if statement is not None:
                node.children.append(statement)
        return node

    def expression(self):
        node = self.term()
        while self.current_token().type in (TOKEN_TYPES['OPERATOR'],):
            token = self.current_token()
            if token.value in ('+', '-'):
                self.eat(TOKEN_TYPES['OPERATOR'])
                right = self.term()
                if node.data_type != right.data_type:
                    self.error("Type mismatch in expression")
                node = ASTNode(token.value, node, node.data_type)
                node.children.append(right)
        return node

    def term(self):
        node = self.factor()
        while self.current_token().type in (TOKEN_TYPES['OPERATOR'],):
            token = self.current_token()
            if token.value in ('*', '/'):
                self.eat(TOKEN_TYPES['OPERATOR'])
                right = self.factor()
                if node.data_type != right.data_type:
                    self.error("Type mismatch in term")
                node = ASTNode(token.value, node, node.data_type)
                node.children.append(right)
        return node

    def factor(self):
        token = self.current_token()
        if token.type == TOKEN_TYPES['NUMBER']:
            self.eat(TOKEN_TYPES['NUMBER'])
            return ASTNode('NUMBER', token.value, 'NUMBER')
        elif token.type == TOKEN_TYPES['IDENTIFIER']:
            self.eat(TOKEN_TYPES['IDENTIFIER'])
            # Resolve the type of the identifier from the symbol table
            data_type = self.symbol_table.get(token.value, 'UNKNOWN')
            return ASTNode('IDENTIFIER', token.value, data_type)
        elif token.type == TOKEN_TYPES['PAREN'] and token.value == '(':
            self.eat(TOKEN_TYPES['PAREN'])
            node = self.expression()
            self.eat(TOKEN_TYPES['PAREN'])
            return node
        elif token.type == TOKEN_TYPES['STRING']:
            self.eat(TOKEN_TYPES['STRING'])
            return ASTNode('STRING', token.value, 'STRING')
        else:
            self.error(f"Unexpected token: {token}")

    def comparison(self):
        left = self.expression()
        token = self.current_token()
        if token.type == TOKEN_TYPES['COMPARISON']:  # Use the correct token type
            self.eat(TOKEN_TYPES['COMPARISON'])
            right = self.expression()
            # Allow comparisons only between compatible types
            if left.data_type != right.data_type:
                if not (left.data_type == 'NUMBER' and right.data_type == 'NUMBER'):
                    self.error(f"Type mismatch in comparison: {left.data_type} vs {right.data_type}")
            node = ASTNode('COMPARISON', token.value)
            node.children.append(left)
            node.children.append(right)
            return node
        else:
            self.error(f"Expected comparison operator, but got {token.value}")

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
