i = input("enter a phase: ")
#-------------------------------
def reverse_string(s):
    r = print(f"reversed: {s[::-1]}")
    return r 
reverse_string(i)
#--------------------------------
def is_palindrome(s):
    t = i.lower()
    first = i[0]
    last  = i[-1]
    if first == last:
        print(f"Is palindrome: {True}")
    else:
        print(f"Is palindrome: {False}")
is_palindrome(i)
#--------------------------------
def count_word(s):
    t = len(s)
    print(f"word count: {t}")
    return t 
count_word(i)

    