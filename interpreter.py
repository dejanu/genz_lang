#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Interpreter for the GenZ programming language
import sys
from parser import Parser
from lexer import lexer, TOKEN_TYPES

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def interpret(self):
        print("Abstract Syntax Tree (AST):")
        print(self.ast)
        print("\nExecution Output:")
        self.visit(self.ast)

    def visit(self, node):
        method_name = f'visit_{node.type.lower()}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{node.type.lower()} method')

    def visit_program(self, node):
        for child in node.children:
            self.visit(child)

    def visit_statement_list(self, node):
        for child in node.children:
            self.visit(child)

    def visit_print(self, node):
        value = self.visit(node.value)
        print(value)

    def visit_assign(self, node):
        identifier = node.value
        value = self.visit(node.children[0])
        self.variables[identifier] = value

    def visit_if(self, node):
        condition = self.visit(node.value)
        if condition:
            self.visit(node.children[0])
        else:
            self.visit(node.children[1])

    def visit_number(self, node):
        return int(node.value)

    def visit_identifier(self, node):
        return self.variables.get(node.value, 0)

    def visit_string(self, node):
        return node.value.strip('"')

    def visit_plus(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        return left + right

    def visit_minus(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        return left - right

    def visit_multiply(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        return left * right

    def visit_divide(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        return left / right

# Main function to run the interpreter
def main():
    if len(sys.argv) != 2:
        print("Usage: genz <file>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        code = file.read()

    tokens = lexer(code)
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter(ast)
    interpreter.interpret()

if __name__ == "__main__":
    main()
