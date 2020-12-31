import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    H_T = []
    for i in range(100):
      H_T.append(random.randint(0, 1))

    streak=0
    for flip in range(1,len(H_T)):
      if H_T[flip-1] == H_T[flip]:
        streak += 1
      else:
        if streak==6:
          numberOfStreaks+=1
        streak=0


    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))