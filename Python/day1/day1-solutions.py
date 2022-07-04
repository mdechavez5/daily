# Problems Completed [ ]

# Your test/solution code here 

# Problem 0
def phrase_finder(words, phrase):
    # print(phrase)
    count = 0
    for word in words:
        # print(word)
        if word in phrase:
            count += 1
        if count == 2:
            return True
    return False
print(phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep'))
print(phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye'))

# Problem 1
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return float('nan')
    distance = 0
    for i in range(0,len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance
print(hamming_distance('abc', 'abc'))
print(hamming_distance('a1c', 'a2c'))
print(hamming_distance('!!!!', '****'))
print(hamming_distance('abc', 'ab'))

# Problem 2
import math
def is_prime(num):
    if (num < 2):
        return False;
    sq = int(math.sqrt(num))
    for i in range(2, sq + 1):
        if (num % i == 0):
            return False
    return True
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(29))
print(is_prime(200))

# Problem 3
def find_the_parity_outlier(lst):
  mods = [n % 2 for n in lst]
  return lst[mods.index(0)] if sum(mods[:3]) > 1 else lst[mods.index(1)]
print(find_the_parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_the_parity_outlier([160, 3, 1719, 19, 11, 13, -21]))
