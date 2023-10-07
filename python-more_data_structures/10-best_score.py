#!/usr/bin/python3
def best_score(a_dictionary):
    last = 0
    if a_dictionary == None:
        return None
    for keys in a_dictionary:
        if a_dictionary[keys] > last:
            last = a_dictionary[keys]
    for key in a_dictionary:
         if last == a_dictionary[key]:
              return key
