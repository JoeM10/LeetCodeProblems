def longestCommonPrefix(strs: list[str]):
  strs.sort()
  prefix = ""
  for letter in range(len(strs[0])):
    if strs[0][letter] != strs[-1][letter]:
      return prefix
    elif strs[0][letter] == strs[-1][letter]:
      prefix += strs[0][letter]
  return prefix

print(longestCommonPrefix(["flower","flow","flight"]))