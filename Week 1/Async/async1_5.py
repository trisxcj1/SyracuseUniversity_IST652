# Activity 1
## Suppose there exists a list of strings such that some strings have only one or two characters, and others have more.
## Write a loop which prints out all the strings with greater than two characters.

samples = [
    'he', 'him', 'i', 'eye', 'hey',
    'hello', 'hey there, how are you?', 'a', 'z', 'q'
    ]

print("Strings with greater than 2 characters: ")
for string in samples:
    if (len(string) > 2):
        print(string)

# Activity 2
## Suppose there exists a list of strings such that some strings have only one or two characters, and others have more.
## Write a loop which prints out all the strings with greater than two characters and less than 5 characters.

### Using the same list as before
print("Strings with greater than 2 characters and fewer than 5 characters: ")
for string in samples:
    if ((len(string) > 2) and (len(string) < 5)):
        print(string)
