#String var
my_string = "Hello, world!"
reversed_string = my_string[::-1]
string_length = len(my_string)
char_list = []
for char in my_string:
    char_list.append(char)
new_list = char_list[2::3]
result = '|'.join(new_list)

print(my_string)
print(reversed_string)
print(string_length)
print(char_list)
print(result)


#With count
def key_list(s):
    key_list = {}
    for char in s:
        key_list[char] = s.count(char)
    return key_list


#Without count
def key_list2(s):
    key_list2 = {}
    for char2 in s:
        if char2 in key_list2:
            key_list2[char2] += 1
        else:
            key_list2[char2] = 1
    return key_list2


#Longest string
def long_str(strings):
    max_length = 0
    longest = ''
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest = string
    return longest


#divide_and_glue
def divide_and_glue(words, symbol):
    words_list = words.split(symbol)
    words_list.sort()
    return symbol.join(words_list)


#Convert
def convert_to_ascii(numbers):
    chars = [chr(num) for num in numbers]
    return ''.join(chars)
