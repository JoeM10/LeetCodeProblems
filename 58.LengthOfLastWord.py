# Original solution
def lengthOfLastWord(s: str) -> int:
    length = 0
    for letter in s[::-1]:
        if letter == " " and length > 0:
            return length
        
        elif letter != " " and len(s) == 1:
            length += 1
            return length

        elif letter == " ":
            pass
        
        else:
            length += 1
    return length

# Much better solution
# def lengthOfLastWord(s: str) -> int:
#     return len(s.strip().split(" ")[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("    fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("a"))