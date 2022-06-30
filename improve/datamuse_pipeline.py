from dataclasses import dataclass
from datamuse import Datamuse
from typing import List, Callable
import pandas as pd
from utils import random_sleep

api = Datamuse()


max_results = 5    
limit_db = -1

options = dict(
    # synonym = lambda worda, wordb: api.words(rel_syn=wordb, max=max_results),
    alliterate = lambda worda, wordb: api.words(rel_syn=wordb, sp=worda[0]+'*', max=max_results),
    # approximate_rhyme = lambda worda, wordb: api.words(rel_syn=wordb, rel_nry=worda, max=max_results),
    # rhyme = lambda worda, wordb: api.words(rel_syn=wordb, rel_rhy=worda, max=max_results)
)

def test_api():
    print(api.words(rel_rhy='ninth', max=5))  # words that rhyme with "ninth"
    print(api.words(rel_rhy='orange', max=5))  # words that rhyme with "orange"
    print(api.words(rel_jja='yellow', max=5))  # things often described as "yellow"
    print(api.suggest(s='foo', max_results=10))  # completion suggestions for "foo"
    print(api.words(trg='frontier', max_results=5)) 
    api.words(rel_jjb='frontier', topics='startup', max=5)


def call_api(worda:str, wordb:str, type:Callable) -> List[dict]:
    random_sleep()
    return type(worda, wordb)


def improve_word(composite_word: str, type:Callable) -> str:
    """
    Given a name, return a better name.
    """

    words_split = composite_word.split(" ")
    
    if len(words_split) == 2:
        worda, wordb = words_split
    else:
        print("🟡 Pattern doesn't match " + composite_word)
        return ""
    
    res = call_api(worda, wordb, type)

    if len(res) > 0:
        new_suggestions = ' | '.join([' '.join([worda, res_one['word'].capitalize()]) for res_one in res])
        print('✅ Improvement found for ' + composite_word + ' -> '  + new_suggestions)
        return new_suggestions
    else:
        print('❌ No improvement found for ' + composite_word)
        print('| Trying with reverse words...')
        res = call_api(wordb, worda, type)
        if len(res) > 0:
            new_suggestions = ' | '.join([' '.join([res_one['word'].capitalize(), wordb]) for res_one in res])
            print('✅ Improvement found for ' + composite_word + ' -> '  + new_suggestions)
            return new_suggestions
        else: 
            print('❌ No improvement found for ' + composite_word)
            return ""


def improve():
    for key, type in options.items():
        print(f"--- type is: {key} ---")
        
        df = pd.read_csv('data/generated/words.csv')[:limit_db]
        df['improved'] = df.apply(lambda row: improve_word(row['names'], type), axis=1)
        df.to_csv(f'data/improved/words_improved_{key}.csv', index=False)

if __name__ == '__main__':
    improve()

# rel_jja	Popular nouns modified by the given adjective, per Google Books Ngrams	gradual → increase
# rel_jjb	Popular adjectives used to modify the given noun, per Google Books Ngrams	beach → sandy
# rel_syn	Synonyms (words contained within the same WordNet synset)	ocean → sea
# rel_trg	"Triggers" (words that are statistically associated with the query word in the same piece of text.)	cow → milking
# rel_ant	Antonyms (per WordNet)	late → early
# rel_spc	"Kind of" (direct hypernyms, per WordNet)	gondola → boat
# rel_gen	"More general than" (direct hyponyms, per WordNet)	boat → gondola
# rel_com	"Comprises" (direct holonyms, per WordNet)	car → accelerator
# rel_par	"Part of" (direct meronyms, per WordNet)	trunk → tree
# rel_bga	Frequent followers (w′ such that P(w′|w) ≥ 0.001, per Google Books Ngrams)	wreak → havoc
# rel_bgb	Frequent predecessors (w′ such that P(w|w′) ≥ 0.001, per Google Books Ngrams)	havoc → wreak
# rel_rhy	Rhymes ("perfect" rhymes, per RhymeZone)	spade → aid
# rel_nry	Approximate rhymes (per RhymeZone)	forest → chorus
# rel_hom	Homophones (sound-alike words)	course → coarse
# rel_cns	Consonant match	sample → simple
# sl sounds like
# ml means like
# sp spelled like