def strStr(haystack: str, needle: str) -> int:
    haystack = haystack.lower()
    needle = needle.lower()
    if len(haystack) < len(needle):
        return -1
    # Checks to see if all the letters of needle are in haystack.
    needleInHaystack = True
    while needleInHaystack:
        for letter in needle:
            if letter in haystack:
                continue
            else:
                return int(-1)
        needleInHaystack = False
    # Checks to see if all the letters of needle  are in the right order
    # starting from the first letter of needle in haystack.

    index = -1
    for letter in haystack:
        index += 1
        if letter == needle[0]:
            print(index)
            for word in range(len(needle)):
                print(f"haystack[index + word]= {haystack[index + word]}")
                print(f"needle[word]= {needle[word]}")
                if haystack[index + word] == needle[word] and haystack[index + word] == needle[-1]:
                    print("Should be returning index")
                    return int(index)
                
                elif haystack[index + word] == needle[word]:
                    print(f"haystack[index + word] = {haystack[index + word]}")
                    print(f"index = {index}")
                    print(f"word = {word}")
                    continue

                else:
                    break
    return -1


print(f"Test 1: {strStr('sadbutsad', 'sad')}, Answer:0\n")
print(f"Test 2: {strStr('yessirplease', 'sir')}, Answer:3\n")
print(f"Test 3: {strStr('sssssssssssssssam', 'sam')}, Answer:14\n")
print(f"Test 4: {strStr('Yaouzayshdesheddaeiugnojer', 'shed')}, Answer:11\n")
print(f"Test 5: {strStr('sdinfkaoekf', 'lint')}, Answer:-1\n")