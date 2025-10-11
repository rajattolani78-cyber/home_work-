# it take input of word from the user :-]
w = str(input("enter a word to count: "))
# deploy a empty zero variable :-}
vowel_count = 0
# it reapeat the user input to check the variable 
for r in (w):
    if r =='a':#it ckeck for the word "a" in the input and add +1 to the empty variable
        vowel_count+=1
    elif r=='e':#it ckeck for the word "e" in the input and add +1 to the empty variable
        vowel_count+=1
    elif r=='i':#it ckeck for the word "i" in the input and add +1 to the empty variable
        vowel_count+=1
    elif r=='o':#it ckeck for the word "o" in the input and add +1 to the empty variable
        vowel_count+=1
    elif r=='u':#it ckeck for the word "u" in the input and add +1 to the empty variable
        vowel_count+=1   
print (vowel_count)