## genx
demo

* Best Use: The most creative and impactful use of ... to accelerate development workflows. Show us how ... boosts your productivity, enhances code quality, and supports innovative problem-solving throughout your project. 

# Language Features

* Interpreted language (tree-walk interpreter)
* Static typed (var must be declared as a specific type)
* Strongly typed (no implicit conversions)
* Define Grammar (instructions on how to write statements for the programming language)

```bash
Statements (printing, assignments, conditions, loops)
Expressions (mathematical & logical expressions)
Blocks (indented or bracketed code blocks)
```

## Programming language 101 (a programming language has 3 core parts)

- Lexer (Tokenizer): breaks code in tokens (meaningful pieces)
- Parser: analyze token structure and builds a syntax tree
- Interpreter/Compiler: **Interpreter** (executes code directly) or a **compiler** (translates it to bytecode or machine code).

## Flow

The first step is scanning, also known as lexing, or lexical analysis. A scanner (or lexer) takes in the linear stream of characters and chunks them together into a series of something more akin to “words” (tokens)

The next step is parsing. This is where our syntax gets a grammar—the ability
to compose larger expressions and statements out of smaller parts