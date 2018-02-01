
import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
Prepositions =["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]


def comp(a, b):
    if a == b:
        return False


def list_creation():
    noun_verbs_adjectives_list = []
    for i in range(3):
        for j in (nouns, verbs, Adjectives):
            noun_verbs_adjectives_list.append(random.choice(j))
    return noun_verbs_adjectives_list


def list_propositions():
    prepositions_list = []
    for k in range(2):
        prepositions_list.append(random.choice(Prepositions))
    return prepositions_list


def make_poem():
    final_creation_list = list_creation()
    for i in range(len(final_creation_list)):
        for j in range(i + 1, len(final_creation_list)):
            while comp(final_creation_list[i], final_creation_list[j]) is False:
                make_poem()

    final_proposition_list = list_propositions()
    for k in range(len(final_proposition_list)):
        for l in range(k + 1, len(final_proposition_list)):
            while comp(final_proposition_list[k], final_proposition_list[l]) is False:
                make_poem()

    adverb = random.choice(Adverbs)
    adjective1 = final_creation_list[2]
    adjective3 = final_creation_list[8]
    if adjective1[0] in ("a", "e", "i", "o", "u"):
        vowel = "An"
    else:
        vowel = "A"
    if adjective3[0] in ("a", "e", "i", "o", "u"):
        vowel1 = "an"
    else:
        vowel1 = "a"
    print("\n", vowel, adjective1, final_creation_list[0], "\n",
          vowel, adjective1, final_creation_list[0], final_creation_list[1], final_proposition_list[0],
          "the", final_creation_list[5], final_creation_list[3], "\n",
          adverb + ",", "the", final_creation_list[0], final_creation_list[4], "\n",
          "the", final_creation_list[3], final_creation_list[7], final_proposition_list[1], vowel1, adjective3,
          final_creation_list[6])


make_poem()


