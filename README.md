# genZ: Overview

GenZ is a simple interpreted programming language designed for educational purposes. It features basic constructs for printing, variable assignment, and conditional statements.

## Purpose
The purpose of GenZ is to provide a minimalistic language that can be used to demonstrate the fundamental concepts of language design, lexical analysis, parsing, and interpretation.

## Language Features

* Interpreted language (tree-walk interpreter)
* Static typed (var must be declared as a specific type)
* Strongly typed (no implicit conversions)
* Define Grammar (instructions on how to write statements for the programming language)

## Programming language 101 (a programming language has 3 core parts)

- Lexer (Tokenizer): breaks code in tokens (meaningful pieces)
- Parser: analyze token structure and builds a syntax tree
- Interpreter/Compiler: **Interpreter** (executes code directly) or a **compiler** (translates it to bytecode or machine code).

## Flow

The first step is scanning, also known as lexing, or lexical analysis. A scanner (or lexer) takes in the linear stream of characters and chunks them together into a series of something more akin to “words” (tokens) .The next step is parsing. This is where our syntax gets a grammar—the ability
to compose larger expressions and statements out of smaller parts.

## Language Constructs

### Print Statement
The `BET` statement is used to print expressions to the console.
```
BET "Hello, World!"
```

### Assignment Statement
The `CAP` statement is used to assign values to variables.
```
CAP x = 10
```

### Conditional Statement
The `SUS` and `NOSUS` statements are used for conditional execution.
```
SUS x {
    BET "x is true"
} NOSUS {
    BET "x is false"
}
```

## Running Unit Tests

To ensure the correctness of the implementation, unit tests are provided. Follow these steps to run the tests:

1. Navigate to the project directory:
   ```bash
    cd path/to/your/genz_lang
   ```

2. Run the tests using the `run_tests.py` script:
   ```bash
   python run_tests.py
   ```

This will execute all test files matching the pattern `test_*.py` in the project directory.