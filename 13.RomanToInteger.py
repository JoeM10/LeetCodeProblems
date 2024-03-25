def romanToInt(s: str):
  romanDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
  }
  previousValue = 0
  value = 0
  for letter in s:
    if romanDict[letter] > previousValue:
      value -= previousValue
      value += (romanDict[letter] - previousValue)
      previousValue = romanDict[letter]
    elif letter in romanDict:
      value += romanDict[letter]
      previousValue = romanDict[letter]
  return value

print(romanToInt("III"))