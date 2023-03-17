from collections import Counter 

def word_order():
    # n represents the number of words that are passed in the function
    n = int(input())
    l = list()

    
    for _ in range(n):
        l.append(input())

    # serializes the list in order
    x = Counter(l)

    #prints th number of distinct words
    print(len(x))

    #prints the occurrence of each distinct word
    print(x)