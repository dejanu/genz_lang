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
        value_type = node.children[0].data_type
        # Store the variable with its resolved type
        self.variables[identifier] = {'value': value, 'type': value_type}

    def visit_if(self, node):
        condition = self.visit(node.value)
        if condition:
            self.visit(node.children[0])
        else:
            self.visit(node.children[1])

    def visit_number(self, node):
        return int(node.value)

    def visit_identifier(self, node):
        if node.value not in self.variables:
            raise Exception(f"Undefined variable '{node.value}'")
        # Resolve the type of the identifier
        node.data_type = self.variables[node.value]['type']
        return self.variables[node.value]['value']

    def visit_string(self, node):
        return node.value.strip('"')

    def visit_plus(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        if node.value.data_type != node.children[0].data_type:
            raise Exception("Type mismatch in addition")
        return left + right

    def visit_minus(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        if node.value.data_type != node.children[0].data_type:
            raise Exception("Type mismatch in subtraction")
        return left - right

    def visit_multiply(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        if node.value.data_type != node.children[0].data_type:
            raise Exception("Type mismatch in multiplication")
        return left * right

    def visit_divide(self, node):
        left = self.visit(node.value)
        right = self.visit(node.children[0])
        if node.value.data_type != node.children[0].data_type:
            raise Exception("Type mismatch in division")
        return left / right

    def visit_comment(self, node):
        # Comments are ignored during interpretation
        pass

    def visit_comparison(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[1])
        operator = node.value
        # Ensure both sides are numbers for comparison
        if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
            raise Exception(f"Invalid comparison between incompatible types: {type(left)} and {type(right)}")
        if operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        elif operator == ">":
            return left > right
        elif operator == "<":
            return left < right
        elif operator == ">=":
            return left >= right
        elif operator == "<=":
            return left <= right
        else:
            raise Exception(f"Unknown comparison operator: {operator}")

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
