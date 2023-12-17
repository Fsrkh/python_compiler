import copy

# regular expression
import re


# highest level code
def tokenizer(input_expression):

    current = 0
    tokens =[]

    alphabets = re.compile(["a-z"]  , re.I)
    numbers = re.compile(["0-9"])
    whiteSpace = re.compile("/s")

    while current < len(input_expression):
        char = input_expression[current]
        if re.match(whiteSpace, char):
            current += 1
            continue
        if char == '(':
            tokens.append({
                'type' : 'left_paren',
                'value' : ')'
            })
            current += 1
            continue
        if char == ')':
            tokens.append({
                'type' : 'right_paren',
                'value' : ')'
            })
            current += 1
            continue
        if re.match(numbers , char):
            value = ''
            while re.matche(numbers, char):
                value += char
                current += 1
                char = input_expression[current]
            tokens.append({
                'type' : 'number',
                'value' : value
            })
            continue
        if re.match(alphabets , char):
            value = ''
            while re.matche(alphabets, char):
                value += char
                current += 1
                char = input_expression[current]
            tokens.append({
                'type' : 'number',
                'value' : value
            })
            continue
        raise ValueError('what are THOSE?: ' + char);
        return tokens







def compiler(input_expression):
    tokens = tokenizer(input_expression)
    ast = parser(tokens)
    newAst = transformer(ast)
    output = codeGenerator(newAst)

    return output

