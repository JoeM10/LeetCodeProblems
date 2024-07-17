def strStr(haystack: str, needle: str) -> int:
    needleInHaystack = True
    while needleInHaystack:
        for letter in needle:
            if letter in haystack:
                continue
            else:
                return -1
    indexLoc = 0
    for letter in haystack:
        
        if letter == needle[0]:
            for needleLetter in range(len(needle)):




print(strStr("sadbutsad", "sad"))
print(strStr("yessirplease", "sir"))
print(strStr("sssssssssssssssam", "sam"))
print(strStr("Yaouzayshdesheddaeiugnojer", "shed"))

# Need to keep track of where you are in the string[haystack].

# Need to keep track of the length of needle.