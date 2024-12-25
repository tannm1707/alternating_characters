def alternating_characters(s):
    prev = ''
    count = 0
    for letter in s:
        if prev == '':
            prev = letter
            continue
        if prev != letter:
            prev = letter
        else:
            count += 1
    return count

# Input for the string `s`
s = input("Enter the string: ")
print(alternating_characters(s))