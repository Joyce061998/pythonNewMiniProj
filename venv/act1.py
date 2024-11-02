"""
 Find out common letters between two strings Using Python
"""

def common_letters():
    str1= input("Enter first String: ")
    str2 = input("Enter Second String: ")
    s1=set(str1)
    s2=set(str2)
    first= s1 and s2
    print(first)


common_letters()

"""
Count the frequency of words appearing in a string Using Python

Sample String = "Sheena Loves Eating apple and mango. Her sister also loves eating apple and mango"
"""

def words_one():
    words1=input("Enter a words: ")
    repeat=words1.split()
    d={}

    for i in repeat:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
words_one()