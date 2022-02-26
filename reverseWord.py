# Example 1
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# Example 2
import re

def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)

# Example 3
def reverse_words(str):
  #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)

# Example 4
import re

def reverse_words(str):
  return ''.join(word[::-1] for word in re.split(r'(\s+)', str))
