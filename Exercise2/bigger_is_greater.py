def bigger_is_greater(w):
    result = ''
    n = len(w)
    w = list(w)

    # Find the largest index i such that w[i] < w[i+1]
    i = n-2
    while i >= 0 and w[i] >= w[i+1]:
        i-=1

    # If no such index exists, the word cannot be rearranged
    if i == -1:
        result = "no answer"
    else:
        # Find the largest index j such that w[j] > w[i]
        j=n-1
        while j >= 1 and w[j] <=w[i]:
           j -= 1
    
        # Swap w[i] and w[j]
        w[i], w[j] = w[j], w[i]

        # Reverse the substring w[i+1:]
        w="".join(w)
        result = w[:i+1] + w[i+1:][::-1]

    # Return the result
    return result