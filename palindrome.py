phrase = input("Enter a phrase: ")
sanitized_phrase = phrase.replace(" ", "")

if sanitized_phrase == sanitized_phrase[::-1]:
    print("'%s' is a palindrome!" % phrase)
else:
    print("'%s' isn't that exciting." % phrase)
