import random 
import art
import game_data

USER_SCORE = 0


def compare_celebrities(figureA, figureB):
  USER_SCORE = 0
  #Celebrity A Credentials 
  fig_A_Name = figureA["name"]
  fig_A_Description = figureA["description"]
  fig_A_Country = figureA["country"]

  #Celebrity B Credentials 
  fig_B_Name = figureB["name"]
  fig_B_Description = figureB["description"]
  fig_B_Country = figureB["country"]
  
  print(f"Compare A: {fig_A_Name}, a {fig_A_Description}, from {fig_A_Country}.")
  print(art.vs)
  print(f"Against B: {fig_B_Name}, a {fig_B_Description}, from {fig_B_Country}.")
  user_guess = input("Who has more followers? Type 'A' or 'B': ")

  if figureA["follower_count"] > figureB["follower_count"]:
    answer = 'A'
  else:
    answer = 'B'

  if user_guess != answer:
    
    print(f"Sorry, thats wrong. Final Score: {USER_SCORE}.")
 
  else: 
    USER_SCORE += 1
    print(f"You're right! Current Score: {USER_SCORE}.")

def clear_console():
    print("\033c", end="")

 
bool = True

while bool:
  clear_console()
  print(art.logo)
  #Generates 2 Random People
  person_A = random.choice(game_data.data)
  person_B = random.choice(game_data.data)
  compare_celebrities(person_A,person_B)
  







