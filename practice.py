# Question 1: Implement a function is_balanced(expression) that takes a string 
# containing parentheses, curly braces, and square brackets,and determines whether 
# the expression is balanced. 

# An expression is considered balanced if each opening bracket has a corresponding closing 
# bracket in the correct order.

# sample input = 

# expression1 = "([]{})"
# expression2 = "([)]"
# print(is_balanced(expression1))  # Output: True
# print(is_balanced(expression2))  # Output: False 


def is_balanced(string):
    stack_list = []

    opening_symbols = {"{", "(", "["}
    closing_symbols = {"}", ")", "]"}
    symbol_mapping = {')': '(', '}': '{', ']': '['}

    

    for char in string:
        if char in opening_symbols:
            stack_list.append(char)
        elif char in closing_symbols:
            if not stack_list or stack_list[-1] != symbol_mapping[char]: 
                return False  # Unbalanced if no matching opening symbol on stack
            stack_list.pop()  # Remove the matching opening symbol from the stack
    
    return len(stack_list) == 0  # If the stack is empty, the string is balanced

# Test cases
print(is_balanced("()"))  # True
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False
print(is_balanced("([)]"))  # False


# Question 2: Write a function remove_duplicates(sequence) that takes a 
# sequence (list or tuple) and returns a new sequence with duplicates 
# removed while maintaining the original order of elements. 

# sample input = 

# input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
# result = remove_duplicates(input_sequence)
# print(result)  # Output: [2, 3, 4, 5, 6, 7]

def remove_duplicates(sequence):
    sequence_list = []    

    for i in sequence:
        if i not in sequence_list:
         sequence_list.append(i)       
           
    return tuple(sorted(sequence_list))

print(remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5]))


# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 

# sample input = 

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)

def word_frequency(sentence):
    count = {}

    a = sentence.lower().replace(".", " ").split()
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
   
    return count

print(word_frequency("This is a test sentence. This sentence is a test."))
