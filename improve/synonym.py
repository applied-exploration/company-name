
import nltk
import timeit
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn

def get_synonyms():
    for word in ['love', 'castle', 'stupid', 'brother', 'fat', 'follower', 'football', 'sun']:
        for ss in wn.synsets(word): # Each synset represents a diff concept.
            print(ss.lemma_names())
        
timeit.timeit(get_synonyms, number=1000)