def strStr(haystack: str, needle: str) -> int:
    haystack = haystack.lower()
    needle = needle.lower()
    # Checks to see if all the letters of needle are in haystack.
    needleInHaystack = True
    while needleInHaystack:
        for letter in needle:
            if letter in haystack:
                continue
            else:
                return -1
        needleInHaystack = False
    # Checks to see if all the letters of needle  are in the right order
    # starting from the first letter of needle in haystack.
    indexLoc = 0
    indexForNeedle = 0
    for letter in haystack:
        print(f"This is letter: {letter}")
        print(f"This is indexForNeedle: {indexForNeedle}")
        if letter == needle[0]:
            for needleLetter in range(len(needle)-1):
                if haystack[indexForNeedle] == needle[needleLetter]:
                    print(f"This is needleLetter: {needleLetter}")
                    print(f"This is needle[needleLetter]: {needle[needleLetter]}")
                    indexForNeedle += 1
                else:
                    indexForNeedle = indexLoc
        indexLoc += 1
        indexForNeedle += 1
    return indexLoc



print(f"Test 1: {strStr('sadbutsad', 'sad')}, Answer:0")
print(f"Test 2: {strStr('yessirplease', 'sir')}, Answer:3")
print(f"Test 3: {strStr('sssssssssssssssam', 'sam')}, Answer:14")
print(f"Test 4: {strStr('Yaouzayshdesheddaeiugnojer', 'shed')}, Answer:11")
print(f"Test 5: {strStr('sdinfkaoekf', 'lint')}, Answer:-1")

# Need to keep track of where you are in the string[haystack].

# Need to keep track of the length of needle.