1.
import re

def match_pattern(text):
    pattern = r'ab*'
    match = re.fullmatch(pattern, text)
    if match:
        return True
    else:
A        return False

#Пример
test_strings = ['a', 'ab', 'abb', 'abbb', 'abbbb', 'ac', 'bc', 'cba']

for string in test_strings:
    if match_pattern(string):
        print(f'"{string}" matches the pattern.')
    else:
        print(f'"{string}" does not match the pattern.')

2.

import re

def match_pattern(text):
    pattern1 = r'ab'
    pattern2 = r'abb'
    pattern3 = r'abbb'
    
    match = re.fullmatch(pattern1 + '|' + pattern2 + '|' + pattern3, text)
    if match:
        return True
    else:
        return False

#Пример
test_strings = ['a', 'ab', 'abb', 'abbb', 'abbbb', 'ac', 'bc', 'cba']

for string in test_strings:
    if match_pattern(string):
        print(f'"{string}" matches the pattern.')
    else:
        print(f'"{string}" does not match the pattern.')

3.
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

4.
import re

def find_sequences(text):
    pattern = r'\b[A-Z][a-z]+\b'
    sequences = re.findall(pattern, text)
    return sequences


text = "Hello my name Kobegen Baktiyar I'm from Kz"
result = find_sequences(text)
print("Sequences of one uppercase letter followed by lowercase letters:", result)

5.
import re

def match_pattern(text):
    pattern = r'a.*b$'
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False

# Test the function
test_strings = ['abc', 'abcb', 'acb', 'axb', 'abx']
for string in test_strings:
    if match_pattern(string):
        print(f'"{string}" matches the pattern.')
    else:
        print(f'"{string}" does not match the pattern.')

6.
import re

def replace_characters(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

text = "This is, a test. Hello World."
replaced_text = replace_characters(text)
print("Original text:", text)
print("After replacement:", replaced_text)

7.
def snake_to_camel(snake_case):
    components = snake_case.split('_')
    camel_case = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case

snake_case_string = "hello_world_example"
camel_case_string = snake_to_camel(snake_case_string)
print("Camel case:", camel_case_string)

8.
import re

def split_at_uppercase(text):
    split_text = re.findall('[A-Z][^A-Z]*', text)
    return split_text

text = "HelloWorldExample"
split_text = split_at_uppercase(text)
print("Split text:", split_text)

9.
import re

def insert_spaces(text):
    modified_text = re.sub(r'(?<!\s)([A-Z][a-z]+)', r' \1', text)
    return modified_text

text = "HelloWorldExample"
modified_text = insert_spaces(text)
print("Modified text:", modified_text)

10.
def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper() and snake_case:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case

camel_case_string = "HelloWorldExample"
snake_case_string = camel_to_snake(camel_case_string)
print("Snake case:", snake_case_string)

