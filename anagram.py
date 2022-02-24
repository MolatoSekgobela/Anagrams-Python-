"""
Given:
string1 = "Clint,East#w?ood"
string2 = "old-west-action"

step1: clean the strings
step2: compare string size
step3: count frequency of letters
step4: we do reverse onn second string
step5: check count in dictionery
step6: if all are zeros terminate loop
"""

from dataclasses import replace


def is_anagram(str1,str2):
    
    unwanted_chars = [',','#','-','?']

    # clean strings
    for i in unwanted_chars:
        str1 = str1.replace(i,'').lower()
    for i in unwanted_chars:
        str2 = str2.replace(i,'').lower()

    # check string length

    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False

    # declare empty dictionery
    count = {}
    # interate through loop
    # count character occurences
    for characters in str1:
        if characters in count:
            count[characters] += 1
        else:
            count[characters] = 1
    
    for characters in str2:
        if characters in count:
            count[characters] -= 1
        else:
            count[characters] = 1

    for i in count:
        if count[i] != 0:
            return False
    return True
    

def is_anagram_sorted(str1,str2):
    # declare array of unwanted chars
    unwanted_chars = [',','#','-','?']
    # clean strings
    for i in unwanted_chars:
        str1 = str1.replace(i,'').lower()
    for i in unwanted_chars:
        str2 = str2.replace(i,'').lower()

    # check string length

    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False
    str1_arry = []
    str2_arry = []

    for i in range(n1):
        str1_arry.append(str1[i])
        str2_arry.append(str2[i])
    # sort both arrays
    # string 1
    for i in range(n1):
        for j in range(n1 - 1):
            if str1_arry[j] > str1_arry[j+1]:
                temp = str1_arry[j]
                str1_arry[j] = str1_arry[j+1]
                str1_arry[j+1] = temp
    
    # string 2
    for i in range(n1):
        for j in range(n1 - 1):
            if str2_arry[j] > str2_arry[j+1]:
                temp = str2_arry[j]
                str2_arry[j] = str2_arry[j+1]
                str2_arry[j+1] = temp

    # compare characters in the sorted arrays
    for i in range(n1):
        if str1_arry[i] != str2_arry[i]:
            return False

    return True

# driver code 
if __name__ == "__main__":

    # declare and assign strings
    str1 = "Clint,East#w?ood"
    str2 = "old-west-action"

    # function call to check strings

    x1 = is_anagram(str1,str2)
    x2 = is_anagram_sorted(str1,str2)

    # sorted function
    if x2:
        print("Strings are anagrams")
    else:
        print("Not anagrams")

    # funtion using dictionery
    if x1:
        print("Strings are anagrams")
    else:
        print("Not anagrams")

    