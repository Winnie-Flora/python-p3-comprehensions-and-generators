# #!/usr/bin/env python3

def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]

print(return_evens(num_list = [1,2,3,4,5,6,7,8,9,10,12]))

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
print(make_exclamation(sentence_list = ["Hello", "Time for vacation", "You look stunning"]))
