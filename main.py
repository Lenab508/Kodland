import random
facts = []
x = int(input('Ile faktow chcesz dodać?'))
for i in range(x):
    fact = input('Dodaj fakt:')
    facts.append(fact)
print('Twój losowy fakt to:' , random.choice(facts))
