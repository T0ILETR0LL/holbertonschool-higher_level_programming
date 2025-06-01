#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    else:
        highscore = lambda score:score[1]
        sort_dictionary = sorted(a_dictionary.items(), key = highscore, reverse = True)
        return sort_dictionary[0][0]