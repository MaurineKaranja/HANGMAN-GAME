import random
from hangman_stages import hangman_stages
word_list = ["apples", "bananas", "oranges", "grapes", "pears", "strawberries"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
display=[]
for i in range(len(chosen_word)):
  display+="_"
print(display)
end_of_game=False
while not end_of_game:
  guess=input("Guess a letter: ").lower()
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
      display[position]=letter
  if guess not in chosen_word:
    lives-=1
    if lives==0:
      end_of_game=True
      print("You lose!!")
  print(display)
  if "_" not in display:
    end_of_game=True
    print("You win!!")
  print(hangman_stages[lives])
    
    