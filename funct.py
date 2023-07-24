import random
с = 0
def read_f():
    with open('words.txt', 'rt') as fp:
        lines = fp.read()
        words = lines.splitlines()
    return words
def shuffle_words(word):
    wordas = list(word)
    random.shuffle(wordas)
    return ''.join(wordas)
def write_record(name, score):
    with open('history.txt', 'a') as f:
        f.write(f'{name} {score}\n')
def static():
    scores = []
    with open('history.txt', 'r') as f:
        for line in f:
            player_name, player_score= line.strip('\n').split()
            scores.append(int(player_score))
        max_s = max(scores)
        len_s = len(scores)
    return {'max':max_s, 'len':len_s}