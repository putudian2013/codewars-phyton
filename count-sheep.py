# Given a non-negative integer, 3 for example, 
# return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    
    murmur = ''

    for element in range(1, n+1):
        murmur += str(element) + ' sheep...'

    return murmur