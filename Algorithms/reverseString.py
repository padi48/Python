'''
Given a string of words, reverse all the words

start = "This is the best"
finis = "best the is This"
'''

def reverse(s):
    #return " ".join(reversed(s.split()))
    #return " ".join(s.split()[::-1])

    lenght = len(s)
    spaces = [' ']
    words = []
    i = 0

    while i < lenght:
        if s[i] not in spaces:
            word_start = i

            while i < lenght and s[i] not in spaces:
                i += 1
            
            words.append(s[word_start:i])
        
        i +=1

    return "".join(reversed(s))

print(reverse("This is the best"))

def my_solution(s):
    return s[::-1]

print(my_solution("This is the best"))

def rev(s):
    return s.split()[::-1]

print(rev("This is the best"))
