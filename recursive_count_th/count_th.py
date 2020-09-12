'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # print(word)

    i = 0
    if len(word) - 1 <= 0:
        return i
    else:
        if word[0] == 't' and word[1] == "h":
            # print(word[:2])
            return count_th(word[2:])  + 1
        else:
            return count_th(word[1:])
