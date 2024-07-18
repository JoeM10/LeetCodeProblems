def strStr(haystack: str, needle: str):
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
    searching = True
    while searching:
        index = 0
        for letter in haystack:
            if letter == needle[0]:
                index = haystack.index(letter)
                print(index)
                for word in range(len(needle)-1):
                    print(f"haystack[index + word]= {haystack[index + word]}")
                    print(f"needle[word]= {needle[word]}")
                    if haystack[index + word] == needle[word]:
                        continue
                    else:
                        break
        return index






print(f"Test 1: {strStr('sadbutsad', 'sad')}, Answer:0\n")
print(f"Test 2: {strStr('yessirplease', 'sir')}, Answer:3\n")
print(f"Test 3: {strStr('sssssssssssssssam', 'sam')}, Answer:14\n")
print(f"Test 4: {strStr('Yaouzayshdesheddaeiugnojer', 'shed')}, Answer:11\n")
print(f"Test 5: {strStr('sdinfkaoekf', 'lint')}, Answer:-1\n")





# Need to keep track of where you are in the string[haystack].
    # indexLoc = -1
    # indexForNeedle = -1
    # for letter in haystack:
    #     print(f"letter= {letter}")
    #     print(f"indexForNeedle= {indexForNeedle}")
    #     if letter == needle[0]:
    #         for needleLetter in range(len(needle)-1):
    #             print(f"haystack[indexForNeedle]= {haystack[indexForNeedle]}")
    #             if haystack[indexForNeedle] == needle[needleLetter]:
    #                 print(f"needleLetter= {needleLetter}")
    #                 print(f"needle[needleLetter]= {needle[needleLetter]}")
    #                 indexForNeedle += 1
    #             else:
    #                 indexForNeedle = indexLoc
    #                 break
            
    #     indexLoc += 1
    #     indexForNeedle += 1
    # return indexLoc

# Need to keep track of the length of needle.