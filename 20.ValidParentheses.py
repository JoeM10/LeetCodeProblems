def isValid(s: str) -> bool:
  parenthesisCompliments = {
    ")": "(",
    "}": "{",
    "]": "[",
  }

  charStack = []
  closingParenthesis = parenthesisCompliments.keys()
  openingParenthesis = parenthesisCompliments.values()

  for char in s:
    if len(charStack) == 0 and char in closingParenthesis:
      return False
    elif char in openingParenthesis:
      charStack.append(char)
    elif char in closingParenthesis:
      if parenthesisCompliments[char] != charStack.pop():
        return False
  return len(charStack) == 0

# Valid Parenthesis Test Cases
print(isValid("())")) # false
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("[()]{}")) # true
print(isValid("([]{})")) # true
print(isValid("([)]")) # false