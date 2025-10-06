import string_utils
user_input = input("enter a phrase: ")
r = string_utils.reverse_string(user_input)
t = string_utils.is_palindrome(user_input)
j = {string_utils.count_word(user_input)}