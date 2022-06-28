from itertools import chain

words_applied_experimental = ["questions", "evidence", "boundaries", "science", "exploration", "frontier", "future"]
words_intelligence = ["shortcuts", "creativity", "complexity", "reason", "brain", "nerve", "spark", "mind"]
words_algorithm = ["algorithms", "function", "evolution","deterministic","decision", "random"]
words_computing = ["compute", "processing", "closure", "engima", "logic", "machines", "byte", "engine", "kernel"]
words_thinking = ["magic", "thoughts", "conception", "conjectures", "hunch"]
words_scientific = ["synthesis", "projection", "morphology", "hypersphere", "manifold", "vector", "zero", "x", "discrete", "indiscrete", "dimension", "sequence", "factor",  "sphere", "ripple", "fraction", "precision", "scope",  "effect", "theory", "calculus", "exo", "vertex", "nano", "isometric", "continuous", "squared", "negative"]
words_abstract = ["alpha", "beta", "zeta",  "Rewind", "loop"]
words_audacious = ["force", "world", "explosion", "tide", "universe", "upward", "forward", "no limit", "jungle"]
words_honest = ["tinkering"]
words_playful = ["play", "dream"]

things = words_applied_experimental + words_intelligence + words_algorithm + words_computing + words_thinking + words_scientific + words_abstract + words_audacious + words_honest + words_playful


words_adj_applied_experimental = ["scientific", "exploratory", "frontier"]
words_adj_algorithm = ["unknown", "algorithmic", "rapid", "auto-","genetic","deterministic", "unresolved", "random"]
words_adj_nature = ["hot", "cold"]
words_adj_audacious = ["ingenious", "audacious", "force", "incredible", "mastery", "world", "explosion", "tide", "universal", "upward", "forward", "no limit", "jungle", "powerful", "dangerous", "broken"]
words_adj_opposite = ["opposite","impossible", "vain", "absurd", "wild", "undoable", "unreasonable"]
words_adj_inventive = ["inventive", "original", "invention", "fertile", "virtuoso", "imaginative", "future", "spark", "wunder", "unique", "magical", "smart"]
words_adj_honest = ["tiny", "genuine", "candid", "sincere", "loyal", "pure", "nude", "honest", "natural", "mindful", "easy", "compact", "almost", "strange", "simple"]
words_adj_scientific = ["infinite", "discrete", "indiscrete", "high-dimensional", "parallel", "absolute", "relative", "quantum", "super-",  "exo", "nano", "isometric", "continuous", "singular", "squared", "negative"]
words_adj_abstract = ["indescribable", "invariant", "Intangible", "Impalpable", "Undecidable", "Ethereal", "Spectral", "recursive", "meta"]
words_adj_antropomorphism = ["talking", "dancing", "playing", "human", "midnight", "wicked", "lucky", "sweet", "angry", "beautiful", "handsome", "hungry", "brave"]
words_adj_playful = ["playful", "rendezvous", "joyful", "joyous", "cheerful", "jubilant", "exuberant", "spirited", "delightful", "upside-down", "ease of mind", "bouncy", "nuts", "thrilled", "euphoric", "affectionate", "wonder", "pleasant", "pleasing", "enchanted", "fascinating", "charismatic", "delightful", "youthful", "youth", "generation", "misplaced", "furry", "express", "improvised", "play", "silly", "curious"]
words_adj_colors = ["yellow", "blue", "red", "black", "violet", "orange", "turquoise"]

def tuple_to_str(tuple):
    return " ".join(tuple)

adjs = words_adj_applied_experimental + words_adj_algorithm + words_adj_audacious + words_adj_opposite + words_adj_inventive + words_adj_honest + words_adj_scientific + words_adj_abstract + words_adj_antropomorphism + words_adj_playful + words_adj_colors
adjs_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(adjs, [thing] * len(adjs))) for thing in things])]

words_ending = ["-ious", "-ism", "-ess", "-ist", "-orium"]
ending_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip([thing] * len(words_ending), words_ending)) for thing in things])]

things_and_adjs = things + adjs
of_the_words = ["algorithms", "world", "engima", "logic", "machines", "play", "dream", "universe", "theories", "future", "loop", "mind"]
things_combined_word_combos = [combo[0] + " of the " + combo[1] for combo in chain.from_iterable([list(zip([thing] * len(things_and_adjs), things_and_adjs)) for thing in of_the_words])]


# titles = [""]

word_combos = adjs_word_combos + ending_word_combos + things_combined_word_combos


import pprint
pprint.pprint(word_combos)
