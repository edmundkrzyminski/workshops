# Text Adventure Builder
# Mission: Create an interactive story where the player makes choices!

# Step 1: Story Variables
# Create variables for your story elements
# Hint: Use descriptive names with snake_case
player_name = input("What is your character's name villager? ")
player_score = 0
has_magic_sword = False
print(f"Welcome, {player_name} a local villager sent you on a path to adventure! and you find yourself at the entrance of a mysterious cave. Your score starts at {player_score}.")
# TODO: Add your variables here
# Example: story_title = "The Enchanted Forest"

# Step 2: Ask the Player's Name
# Use input() to get the player's character name

# TODO: Ask for the player's name here


# Step 3: Story Opening
# Use print() and f-strings to display your story's beginning

# TODO: Display your story opening here


# Step 4: First Choice
# Use input() to ask the player to make a choice
# Use if/else to create different paths
done=False 
while not done:
  choice = input("Do you enter the cave (1) or walk around it (2)? ")
  if choice == "1":
      print(f"{player_name} bravely enters the cave.")
      player_score = player_score + 10
      has_magic_sword = False
      print("You found a magic ring! Your score increases by 10.")
  else:
      print(f"{player_name} decides to walk around the cave.")
      player_score = player_score + 0
      print("You found a hidden lake! Your score increases by 1.")
      choice = input("Do you swim in the lake (1) or keep walking (2)? ")
      if choice == "1":
          print(f"{player_name} swims in the lake and finds a treasures!")
          player_score = player_score + 10
          has_magic_sword = False
          print("Your score increases by 10.")
      else:
          print(f"{player_name} keeps walking and finds a destroyed castle!")
          player_score = player_score + 0
          has_magic_sword = False
          print("Your score increases by 0.")
          choice = input("Do you explore the castle (1) or keep walking (2)? ")
          if choice == "1":
              print(f"{player_name} explores the castle and finds a magic sword!but then is attacked by a oger and almosted died!")
              player_score = player_score + 90
              has_magic_sword = True
              print("Your score increases by 90.")
          else:
              print(f"{player_name} keeps walking and finds a mad dragon!")
              player_score = player_score + -10
              has_magic_sword = False
              print("Your score increases by -10.")
              choice = input("Do you fight the dragon (1) or run away (2)? ")
              if choice == "1":
                  if has_magic_sword:
                      print(f"{player_name} fights the dragon with the magic sword and wins!")
                      player_score = player_score + 50
                  else:
                      print(f"{player_name} fights the dragon without a sword and loses!")
                      player_score = player_score - 20
              else:
                  print(f"{player_name} runs away from the dragon.")
                  player_score = player_score - 5

# TODO: Ask the player a question and respond based on their answer
# Example:
# choice = input("Do you go left or right? ")
# if choice == "left":
#     print("You found a treasure chest!")
# else:
#     print("You found a friendly dragon!")


# Step 5: Story Ending
# Use your variables and the player's choices to create a personalized ending

# TODO: Create your ending here


# Extension Challenges:
# - Add more choices with elif
# - Track a score that changes based on choices
# - Ask for more user inputs throughout the story
# - Create multiple endings based on different choices
# - Use .lower() on input to handle capitalization
