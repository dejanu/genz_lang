# genZ: Overview

GenZ is a simple interpreted programming language designed for educational purposes. It features basic constructs for printing, variable assignment, and conditional statements.

## Purpose
The purpose of GenZ is to provide a minimalistic language that can be used to demonstrate the fundamental concepts of language design, lexical analysis, parsing, and interpretation.

## Language Features

* Interpreted language (tree-walk interpreter)
* **Statically typed** (variables must be declared with a specific type)
* **Strongly typed** (no implicit type conversions)
* Define Grammar (instructions on how to write statements for the programming language)

## Typing System

GenZ enforces a **strong typing system** to ensure type safety and prevent runtime errors caused by implicit type conversions. Below are the key aspects of the typing system:

1. **Static Typing**:
   - Variables are assigned a type at the time of their first assignment.
   - The type of a variable cannot change after it is assigned.

2. **Strong Typing**:
   - Operations between mismatched types (e.g., adding a string to a number) are not allowed.
   - Type mismatches result in a parse or runtime error.

3. **Supported Types**:
   - **NUMBER**: Represents integer values.
   - **STRING**: Represents text enclosed in double quotes (e.g., `"Hello"`).

4. **Type Enforcement**:
   - During assignment, the type of the value being assigned is checked against the variable's type.
   - Arithmetic operations (`+`, `-`, `*`, `/`) are only allowed between `NUMBER` types.
   - Concatenation or other operations on `STRING` types must be explicitly defined.

### Example of Type Safety
```genz
CAP x = 42
CAP y = "Hello"

BET x + 10
BET y + " World"

CAP x = "Oops"
```

## Programming language 101 (a programming language has 3 core parts)

- Lexer (Tokenizer): breaks code in tokens (meaningful pieces)
- Parser: analyze token structure and builds a syntax tree
- Interpreter/Compiler: **Interpreter** (executes code directly) or a **compiler** (translates it to bytecode or machine code).

## Flow

The first step is scanning, also known as lexing, or lexical analysis. A scanner (or lexer) takes in the linear stream of characters and chunks them together into a series of something more akin to “words” (tokens). The next step is parsing. This is where our syntax gets a grammar—the ability
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

### Comments
GenZ supports single-line comments. Any text following the `#` symbol on a line is treated as a comment and ignored during execution.
```
# This is a comment
CAP x = 42 # Assign 42 to x
BET x # Print the value of x
```

## Running a `.genz` File

To run a `.genz` file, use the GenZ interpreter. Follow these steps:

1. Navigate to the project directory:
   ```bash
   cd /Users/dej/Desktop/Git_projects/genz_lang
   ```

2. Run the interpreter with the `.genz` file as an argument:
   ```bash
./interpreter.py examples/var_instantiation.genz
   ```

This will execute the code in the specified `.genz` file and display the output in the console.

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