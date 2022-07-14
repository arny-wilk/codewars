def anagrams(word, words):

    res = []

    temp = word[-1:len(word)]
    temps = words[:1]


    if temp == temp

    dfs(i, cur=None, prev=temp, branch=temps):


        cur = []
        for i in branch:
            if i != prev:
                continue
            cur.append(i)
            dfs(i+1, cur, prev=temp[-1:], branch=temps[:1])


    dfs(0, [], prev=temp[-1:]], branch=words[:1])

    return cur








print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print("")
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print("")
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
