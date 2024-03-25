def countCharacters(words: list[str], chars: str) -> int:
  sumOfLengths = 0
  
  for word in words:
    characters = [character for character in chars]
    wordLength = len(word)
    goodLetterCount = 0
    for letter in word:
      if letter in characters:
        characters.remove(letter)
        goodLetterCount += 1
      else:
        pass
    if wordLength == goodLetterCount:
      sumOfLengths += wordLength
  return sumOfLengths

print(countCharacters(["cat","bt","hat","tree"], "atach"))
print(countCharacters(["hello","world","leetcode"], "welldonehoneyr"))