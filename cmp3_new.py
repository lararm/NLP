import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


#sample_text = "robots are cool" #state_union.raw("2006-GWBush.txt")

train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

phrases = []
from itertools import permutations
i=1

for group in permutations(['robots', 'are', 'cool'], 3):
 print(' '.join(group))  
 #Getting a list with all possible phrases
 phrase = " ".join(group)
 sample_text= phrase
 phrases.append(phrase)
 tokenized = custom_sent_tokenizer.tokenize(sample_text)
 def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))	
 process_content()

print(phrases)
 
tokenized = custom_sent_tokenizer.tokenize(sample_text) 
