def strStr(haystack: str, needle: str) -> int:
    haystack = haystack.lower()
    needle = needle.lower()
    if len(haystack) < len(needle):
        return -1
    elif needle not in haystack:
        return -1

    index = -1
    letterTracker = 1
    for letter in haystack:
        index += 1
        if letter == needle[0]:
            for word in range(len(needle)):
                if needle[word] != haystack[index + word]:
                    letterTracker = 1
                    break

                elif haystack[index + word] == needle[word] and letterTracker == len(needle):
                    return index

                letterTracker += 1
            
    return index


print(f"Test 1: {strStr('sadbutsad', 'sad')}, Answer:0\n")
print(f"Test 2: {strStr('yessirplease', 'sir')}, Answer:3\n")
print(f"Test 3: {strStr('sssssssssssssssam', 'sam')}, Answer:14\n")
print(f"Test 4: {strStr('Yaouzayshdesheddaeiugnojer', 'shed')}, Answer:11\n")
print(f"Test 5: {strStr('sdinfkaoekf', 'lint')}, Answer:-1\n")
print(f"Test 6: {strStr('leetcode', 'leeto')}, Answer:-1\n")
print(f"Test 7: {strStr('mississippi', 'issipi')}, Answer:-1\n")
print(f"Test 8: {strStr('mississippi', 'sippi')}, Answer:6\n")