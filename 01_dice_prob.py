 # What is the probability that the sum of the dice equals to seven

dice = { (i,j):i+j for i in range(1, 7) for j in range(1, 7) }

prob_seven = [ i for i in  dice.keys() if dice.get(i) == 7 ]

print ('Total possible outcome: {}'.format(len(dice)))

print('Possible outcome of having seven in two dices')
print(prob_seven)

print('Probability that the sum of the two dices equal to seven is {}/{} : {}%'.format(len(prob_seven), len(dice), round(len(prob_seven)/len(dice), 2)*100))
