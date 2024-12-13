# Define variables
input_letters = ['m','i','n','o','z','a','t']
key_letter = 'o'
with open('words.txt', 'r') as file:
  english_words = [line.strip() for line in file if len(line) > 4]

# Define functions
def check_words(letters, key, words):
  # Find words that are made up only of letter
  valid_words = []
  
  for word in words:
    valid = True
    for letter in word.lower():
      if letter not in letters:
        valid = False
        break
    if valid and key in word:
      valid_words.append(word) 
    valid = True
    
  return valid_words
    
valid_words = check_words(input_letters, key_letter, english_words)
for word in valid_words:
  print(word)