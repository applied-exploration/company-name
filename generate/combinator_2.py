from itertools import chain, combinations

def generate():
    things_human_philosophy = ["leap", "upstream","sense", "idealism", "intuition", "realm","razor", "narrative", "theory of", "atlas","fiction", "verve", "phenomena", "life", "spirit", "intellect", "time",  "beginning", "positivism", "empiricism", "Renaissance", "principle"]
    things_human_attribute = ["ignorance", "collective", "soul", "ego",  "essence"]
    things_human_relationship = ["accord", "club", "closeness", 'family', "fondness", "passion", "sentiment"]
    things_human_food = ["cake", "beacon", "coffee", "beans", "pulp"]
    things_human_travel = ["movement", "park", "harmony", "nature", "Ahoy"]
    things_human_animal = ["creature", "monkeys"]
    things_human_activities = ["touch", "feeling", "walk", "desire", "darts", "canvas", "pieces"]
    things_human_music = ["tempo", "tunes", "melody"]
    things_human_cultural = ["modernist", "culture", "squeeze"]
    things_human_nature = ["flow", "current", "ocean", "people", "midnight", "sunrise", "sunset", "moon"]
    things_human_thinking = ["manifesto", "explorers", "magic", "thoughts", "conjectures"]
    things_human_playful = ["genie", "play", "dreams", "-semi", "-ultra", "-alpha", "-beta",]

    things_human = things_human_philosophy + things_human_attribute + things_human_relationship + things_human_food + things_human_travel + things_human_animal + things_human_activities + things_human_music + things_human_cultural + things_human_nature + things_human_thinking + things_human_playful

    things_tech_experimental = ["adventures", "future", "frontier", "phenomena"]
    things_tech_intelligence = ["shortcuts", "complexity", "hypotheses"]
    things_tech_algorithm = ["flow", "clusters", "algorithms", "function", "evolution","decisions", "randomness"]
    things_tech_computing = ["structure", "compute", "engima", "logic", "machines", "byte", "engine", "algorithms"]
    things_tech_scientific = ["epoch", "control", "equivalence", "unity", "exponential", "paradigm", "Renaissance", "shift", "landscape", "volatility", "axion", "Equilibrium", "joint", "friction", "synthesis", "projection", "hypersphere", "manifold", "vectors", "zeros", "discrete", "dimensions", "sequence", "factor",  "sphere", "fraction",   "effect", "theories", "calculus", "vertices", "matrices", "isometric", "negative"]
    things_tech_abstract = ["loop", "amphetamine"]
    things_tech_audacious = ["force", "world", "universe"]

    things_tech = things_tech_experimental + things_tech_intelligence + things_tech_algorithm + things_tech_computing + things_tech_scientific + things_tech_abstract + things_tech_audacious

    adjs_human_food = ["deep fried", "grilled"]
    adjs_human_travel = ["exotic", "breathteaking", "guided"]
    adjs_human_philsophy = ["sublime", "beyond", "ephemeral", "intuitive", "conceptual", "platonic", "hedonistic", "stoic", "empirical"]
    adjs_human_relationship = ["cooperative", "likeminded", "connected", "solo", "rare", "generous", "tender", "archetypical", "quintessential", "mutual", "friendly"]
    adjs_human_antropomorphism = ["little big", "surfing", "secret", "thoughtful", "weird", "mysterious", "uncanny", "spark", "wunder", "unique",  "smart", "sharp", "imaginary", "original","magically", "perfect", "talking", "dancing", "human", "wicked", "lucky", "sweet", "angry", "beautiful", "handsome", "hungry", "brave"]
    adjs_human_playful = ["spinning", "swirling", "spooky", "playful", "joyful", "joyous", "cheerful", "jubilant", "exuberant", "spirited", "delightful", "upside-down", "thrilled", "euphoric", "affectionate", "wonder", "pleasant", "pleasing", "enchanted", "fascinating", "charismatic", "delightful", "youthful", "youth", "generation", "misplaced", "furry", "express", "improvised", "silly", "curious"]
    # adjs_human_colors = ["yellow", "blue", "red", "black", "violet", "orange", "turquoise"]
    adjs_human_nature = ["streaming", "flowing", "hot", "cold"]
    adjs_human_audacious = ["swift", "imminent", "stimulating", "unconventional", "unexpected", "impassioned", "imagination", "greatest", "ingenious", "audacious", "force", "incredible", "mastery", "world", "explosion", "tide", "universal", "upward", "forward", "powerful", "dangerous", "broken"]
    adjs_human_honest = ["quiet", "noble", "tiny", "genuine", "candid", "sincere", "loyal", "pure", "nude", "honest", "natural", "mindful", "easy", "compact", "almost", "strange", "simple"]
    adjs_human_opposite = ["electric", "unattainable", "impalpable", "indescribable", "ambiguous", "bound", "opposite","impossible", "vain", "absurd", "wild", "undoable", "unreasonable"]
    adjs_latin = ["astro-", "pre-", "post-", "ab-", "ex-", "semi-", "ultra-", "hyper-", "inter-"]
    verbs = ["poke"]

    adjs_human = adjs_latin + adjs_human_food + adjs_human_travel + adjs_human_philsophy + adjs_human_relationship + adjs_human_antropomorphism + adjs_human_playful + adjs_human_nature + adjs_human_audacious + adjs_human_honest + adjs_human_opposite

    adjs_tech_applied_experimental = ["compact", "scientific", "exploratory"]
    adjs_tech_algorithm = ["buttons", "recurrence", "volatile", "stochastic", "unknown", "algorithmic", "rapid", "deterministic", "unresolved", "random"]
    adjs_tech_inventive = ["future", "breakthrough"]
    adjs_tech_scientific = ["atomic", "eletric", "upstream", "exponential", "space", "infinite", "discrete", "indiscrete", "high-dimensional", "parallel", "absolute", "relative", "quantum", "super-",  "exo", "nano", "isometric", "continuous", "singular", "negative"]
    adjs_tech_abstract = ["intertwined","invariant", "Intangible", "Undecidable", "Ethereal", "Spectral", "recursive", "meta"]

    adjs_tech = adjs_latin + adjs_tech_applied_experimental + adjs_tech_algorithm + adjs_tech_inventive + adjs_tech_scientific + adjs_tech_abstract

    words_tech = adjs_tech + things_tech
    words_human = adjs_human + things_human + adjs_latin

    things_all = things_tech + things_human

    verbs = ["poke", "kill", "move"]



    def tuple_to_str(tuple):
        return " ".join(tuple)

    human_tech_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(words_tech, [thing] * len(words_tech))) for thing in things_human])]
    tech_human_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(words_human, [thing] * len(words_human))) for thing in things_tech])]

    human_human_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(adjs_human, [thing] * len(adjs_human))) for thing in things_human])]
    adj_adj_combos = [tuple_to_str(combo) for combo in combinations(adjs_human + adjs_tech, 2)]

    words_all_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(things_human, [thing] * len(things_human))) for thing in things_human])]
    # tech_tech_word_combos = [tuple_to_str(combo) for combo in chain.from_iterable([list(zip(adjs_tech, [thing] * len(adjs_tech))) for thing in things_tech])]

    # things_and_adjs = things + adjs
    # of_the_words = ["algorithms", "world", "logic", "machines", "play", "dream", "universe", "theories", "future", "loop", "mind"]
    # things_combined_word_combos = [combo[0] + " of the " + combo[1] for combo in chain.from_iterable([list(zip([thing] * len(things_and_adjs), things_and_adjs)) for thing in of_the_words])]


    word_combos = human_tech_word_combos + tech_human_word_combos + human_human_word_combos + adj_adj_combos
    # word_combos = tech_tech_word_combos

    import pprint
    pprint.pprint(word_combos)

generate()