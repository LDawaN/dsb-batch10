import random
hand_com = ["Hammer", "scissors", "paper"]
com = 0
player = 0
tie =0
print("Wellcom to the Pao Ying Chup Game")
while True:
  hand_p = input(f"Hammer, Scissors, Paper or Quit").strip().lower()
  if hand_p == "quit":
    break

  hand_c = random.choice(hand_com).lower()
  print(f"computer chose: {hand_c}")

  if hand_p == hand_c:
    tie +=1
    print("Tie")
  elif (hand_p == "hammer" and hand_c == "scissors") or \
   (hand_p == "scissors" and hand_c == "paper") or \
    (hand_p == "paper" and hand_c == "hammer"):
    player +=1
    print("player Win")
  else :
    com += 1
    print("Computer Win")
if player > com:
  print(f"Player Win the game score:{player}:{com}")
elif com > player:
  print(f"Computer Win the game score:{com}:{player}")
else:
  print(f"Player and Computer Tie")
