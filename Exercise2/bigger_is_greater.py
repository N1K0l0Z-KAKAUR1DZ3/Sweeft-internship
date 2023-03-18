def bigger_is_greater(w):
    result = ''
    n = len(w)
    w = list(w)

    i = n-2
    while i >= 0 and w[i] >= w[i+1]:
        i-=1

    if i == -1:
        result = "no answer"
    else:
        j=n-1
        while j >= 1 and w[j] <=w[i]:
           j -= 1
    
        w[i], w[j] = w[j], w[i]
        w="".join(w)
        result = w[:i+1] + w[i+1:][::-1]

    return result


print(bigger_is_greater('lmno'))  # lmon
print(bigger_is_greater('dcba'))  # no answer
print(bigger_is_greater('dcbb'))  # no answer
print(bigger_is_greater('abdc'))  # acbd
print(bigger_is_greater('abcd'))  # abdc
print(bigger_is_greater('fedcbabcd'))  # fedcbabdc