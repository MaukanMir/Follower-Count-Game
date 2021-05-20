from art import logo, vs
from game_data import data
import random
import os



def format_data(account):
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return (f"{account_name}, a {account_description}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")

  print(vs)

  print(f"Compare B: {format_data(account_b)}")

  guess = input("Who has more followers? A or B?: ").lower()

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  os.system('clear') 
  print(logo)

  if is_correct:
    score += 1
    print(f"You're right! Current Score is {score}")
  else:
    game_should_continue = False
    print(f"Sorry, thats wrong.Your final score is {score}")
