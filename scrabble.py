# Dictionaries

# Scrabble 

# To process data from a group playing scrabble. Use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# The letter_to_points dictionary that can handle lowercase inputs 
letters += [
  letter.lower()
  for letter
  in letters
]
points *= 2

# Build Point Dictionary
# Use a list comprehension and zip to create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.

letter_to_points = {
  key: value
  for key, value 
  in zip(letters, points)
}
# Ensure letters list takes into account blank tiles
letter_to_points[" "] = 0
print(letter_to_points)

# Score a Word
# function takes in a word and returns the number of points that word is worth.

def score_word(word):
# loop goes through the letters in word and adds the point value of each letter to point_total

  point_total = 0
  for letter in word:
# Obtain point value from the letter_to_points dictionary. If the letter being checked is not in letter_to_points, add 0 to the point_total
    point_total += letter_to_points.get(letter, 0)
  return point_total

# test score_word function
brownie_points = score_word("BROWNIE")
print(brownie_points)
# output 15
# (B + R + O + W + N + I + E)
# (3 + 1 + 1 + 4 + 4 + 1 + 1) = 15

# Score a Game
# map players to a list of the words they have played.
player_to_words = {
  "Homer Simpson": ["IMMATURE", "LAZY","UNPROFESSIONAL"],
  "Marge Simpson": ["MATRIARCH", "MORAL","OPTIMIST"],
  "Bart Simpson": ["MISCHIEVEOUS", "REBELLIOUS","PRANKS"],
  "Mr Burns": ["BILLIONAIRE", "BOSS","EVIL"]
}

player_to_points = {}

# function called any time a word is played
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()
print(player_to_points)

# function takes in a player and a word, and adds that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player].append(word)
  update_point_totals()

play_word("Homer Simpson", "D'OH")
print(player_to_words)
print(player_to_points)
