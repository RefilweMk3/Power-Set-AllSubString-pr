string = input("Enter string: ")

substrings = []
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        substrings.append(string[i:j])

for substring in substrings:
    print(substring)