'''Interview questions

'''

#Given two strings, check to see if they are anagrams. An anagram is when the two
#strings can be written using the exact same letters.
def anagram(s1,s2):

    #Remove spaces and lowercase letters!
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #Return boolean for sorted match
    return sorted(s1) == sorted(s2)

#print(anagram('dog', 'god'))
#print(anagram('clint eastwood', 'olD West Action')) #True bcs we're lowercasing too
#print(anagram('aa', 'bb'))

def anagram2(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    #Check if same number of letters
    if len(s1) != len(s2):
        return False
    
    #Count frequency of each letter
    count = {}

    for letter in s1: #for every letter in first string
        if letter in count: #if letter is already in my dictionary, then
            count[letter] += 1 # add 1 to that letter key
        else:
            count[letter] = 1

    #do reverse for second string
    for letter in s2: 
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

x = anagram2('clint eastwood', 'olD West Action')
#print(x)




#My solution to the problem:
def my_anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    count = []

    for letter in s1:
        count.append(letter)

    for letter in s2:
        count.remove(letter)

    if len(count) == 0:
        return True
    return False

print(my_anagram('westwood', 'tsEWoWod'))
