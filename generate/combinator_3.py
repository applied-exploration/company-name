from itertools import chain, combinations

things_human_philosophy = ["catch", "leap", "upstream","sense", "idealism", "intuition", "realm","razor", "narrative", "theory of", "atlas","fiction", "verve", "phenomena", "life", "spirit", "intellect", "time",  "beginning", "positivism", "empiricism", "Renaissance", "principle"]
things_human_attribute = ["ignorance", "collective", "soul", "ego",  "essence"]
things_human_relationship = ["outsiders", "accord", "club", "closeness", 'family', "fondness", "passion", "sentiment"]
things_human_food = ["cake", "beacon", "coffee", "beans", "pulp"]
things_human_travel = ["movement", "park", "harmony", "nature", "Ahoy"]
things_human_animal = ["creature", "monkeys"]
things_human_activities = ["tale", "dance", "touch", "feeling", "walk", "desire", "darts", "canvas", "pieces"]
things_human_music = ["tempo", "tunes", "melody"]
things_human_cultural = ["modernist", "culture", "squeeze"]
things_human_nature = ["flow", "current", "ocean", "people", "midnight", "sunrise", "sunset", "moon"]
things_human_thinking = ["manifesto", "explorers", "magic", "thoughts", "conjectures"]
things_human_playful = ["genie", "play", "dreams", "-semi", "-ultra", "-alpha", "-beta",]
things_human_abstract = ["human", "illusion", "unknown", "almost", "imagination", "secret"]

things_human = things_human_abstract + things_human_philosophy + things_human_attribute + things_human_relationship + things_human_food + things_human_travel + things_human_animal + things_human_activities + things_human_music + things_human_cultural + things_human_nature + things_human_thinking + things_human_playful

things_tech_experimental = ["exploration", "adventures", "future", "frontier", "phenomena"]
things_tech_intelligence = ["elegance", "shortcuts", "complexity", "hypotheses"]
things_tech_algorithm = ["buttons", "recurrence","clusters", "algorithms", "function", "evolution","decisions", "randomness"]
things_tech_computing = ["code", "structure", "compute", "engima", "logic", "machines", "byte", "engine"]
things_tech_scientific = ["rays", "fluid", "liquid", "atoms", "particles", "paradox", "epoch", "control", "equivalence", "unity", "exponential", "paradigm", "shift", "landscape", "Equilibrium", "joint", "friction", "synthesis", "manifold", "vectors", "zeros", "discrete", "dimensions", "sequence", "factor",  "sphere", "fraction",   "effect", "theories", "calculus", "vertices", "matrices", "isometric", "negative"]
things_tech_abstract = ["loop"]
things_tech_audacious = ["force", "world", "universe", "the sound of "]

things_tech = things_tech_experimental + things_tech_intelligence + things_tech_algorithm + things_tech_computing + things_tech_scientific + things_tech_abstract + things_tech_audacious


things_company_suffixes = ["factory", "labs", "& Co", "works", "club"]
suffixes = ["-where", "-hood", "-less"]
prefixes = ["co-", "over-"]
verbs = ["poke"]

things_all = things_tech + things_human + things_company_suffixes + suffixes + verbs

def tuple_to_str(tuple):
    return " ".join(tuple)

word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(things_all, [thing] * len(things_all))) for thing in things_all])]

import pprint
pprint.pprint(word_combos)
