phrases = []
from itertools import permutations
i=1

for group in permutations(['robots', 'are', 'cool'], 3):
 print(' '.join(group))  
 #Getting a list with all possible phrases
 phrase = " ".join(group)
 phrases.append(phrase)

print(phrases)
 
 