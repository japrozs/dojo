# Dojo
Dojo is a programming language that is loosely based off of the [Python](https://python.org) which uses the Python compiler and also uses it own Lexer, Parser, Compiler and Token Generator
Some features of Dojo are as given below:
- Function declaration
- Variable Declaration
- Basic Arithmetic
- Executing Files

Basic Grammar of the DOJO Programming Language:
- All keywords are in Capital
- FUN = Used to declare a function
- FOR = used to start a for loop
- PRINT = return something to the screen
- RETURN = return something
- VAR = declare a variable
- IF = if statement
- ELIF = elif statement
- ELSE = else statement 
- `#` = Declare a comment 

- A Function declaration
```python
FUN greet(int, string)
  FOR i = 0 TO int THEN
    PRINT(string)
  END
END

greet(10, "Hello from Dojo")
```
```python
tokens = []
APPEND(tokens, "first_element")

# tokens/0 = "first_element"
# instead of tokens[i] you have to use tokens/i to access the i'th element
PRINT(tokens/0)
```
# Single line:
* Functions
```python
FUN greet(string) -> PRINT(string)
```
* If else statements
```python
IF a = True THEN
  PRINT("TRUE")
ELIF a = False THEN
  PRINT("FALSE")
ELSE THEN
```
* While statements
```python
WHILE True THEN
  PRINT("HELLO")
 END
 ```
