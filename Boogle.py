'''
Given a dictionary a method to do look up in dictionary and a M X N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters.Note that we can move to any
of 8 adjacent characters bnut a word should not have muliple instance of same cell
'''



'''
####def findWord(board, visited, row, col, word, englishDict):
####      if(englishDict  
##def isWord(string):
##    for i in string:
##            if i == j:
##                return True
##    return False
##
##def find(boogle, visited, i, j, string):
##    visited[i][j] = True
##    string = string + boogle[i][j]
##
##    if(isWord(string)):
##        print(string)

pathRow = [0, 0, 1, 1, -1, 1, -1, 1]
pathCol = [1, -1, -1, 1, 1, 0, 0, -1]

def findWord(board, visited, row, col, word, englishDict):
    rowsLen = len(board)
    colsLen = len(board[0])
    totalLen = rowsLen * colsLen
    
##    res = any(ele in word for ele in englishDict)
##    if(res):
##        print(word)
    for i in englishDict:
        
        if i == word:
            print(word)
##    if word in englishDict:
##        print(word)

##    if englishDict.find(word) == -1:
##        print(word)
    if(totalLen == len(word)):
        return
    for i in range(0, len(pathRow)):
        rowNew = row + pathRow[i]
        colNew = col + pathCol[i]
        if(ifValid(rowNew, colNew, visited)):
            visited[rowNew][colNew] = True
            findWord(board, visited, rowNew, colNew, word+board[rowNew][colNew],englishDict)
            visited[rowNew][colNew] = False
            

def ifValid(rowNew, colNew, visited):
    if((rowNew >0) and (colNew >0) and (rowNew < 3) and (colNew < 3) and (visited[rowNew][colNew] is False)):
        
        return True
    else:
        return False
        


board =[['g','i','z'],['u','e','k'],['q','s','e']]
#print(board[1][1])
englishDict = {"geeks", "for", "quiz", "guq", "ee"}

visited = [[False for i in range(3)]for j in range(3)]
word = ""

##print(word+board[0][0])
#print(visited)
for row in range(3):
    for col in range(3):
        visited[row][col] = True
        findWord(board, visited, 0, 0, word+board[row][col], englishDict)
        visited[row][col] = False
'''




from collections import defaultdict
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#english_words = words.words()

# If you wan to remove stop words
#stop_words = set(stopwords.words('english'))
#english_words = [w for w in english_words if w not in stop_words]

english_words = ['apple', 'pickle', 'side', 'kick', 'sick', 'mood', 'cat',
                 'cats', 'man', 'super', 'antman', 'godzilla', 'dog', 'dot',
                 'sine', 'cos', 'signal', 'bitcoin', 'cool', 'zapper']

boggle = [
    ['c', 'n', 't', 's', 's'],
    ['d', 'a', 't', 'i', 'n'],
    ['o', 'o', 'm', 'e', 'l'],
    ['s', 'i', 'k', 'n', 'd'],
    ['p', 'i', 'c', 'l', 'e']
]

# Instead of X and Y co-ordinates
# better to use Row and column
lenc = len(boggle[0])
lenr = len(boggle)

# Initialize trie datastructure
trie_node = {'valid': False, 'next': {}}

# lets get the delta to find all the nighbors
neighbors_delta = [
    (-1,-1, "↖"),
    (-1, 0, "↑"),
    (-1, 1, "↗"),
    (0, -1, "←"),
    (0,  1, "→"),
    (1, -1, "↙"),
    (1,  0, "↓"),
    (1,  1, "↘"),
]


def gen_trie(word, node):
    """udpates the trie datastructure using the given word"""
    if not word:
        return

    if word[0] not in node:
        node[word[0]] = {'valid': len(word) == 1, 'next': {}}

    # recursively build trie
    gen_trie(word[1:], node[word[0]])


def build_trie(words, trie):
    """Builds trie data structure from the list of words given"""
    for word in words:
        gen_trie(word, trie)
    return trie


def get_neighbors(r, c):
    """Returns the neighbors for a given co-ordinates"""
    n = []
    for neigh in neighbors_delta:
        new_r = r + neigh[0]
        new_c = c + neigh[1]

        if (new_r >= lenr) or (new_c >= lenc) or (new_r < 0) or (new_c < 0):
            continue
        n.append((new_r, new_c, neigh[2]))
    return n


def dfs(r, c, visited, trie, now_word, direction):
    """Scan the graph using DFS"""
    if (r, c) in visited:
        return

    letter = boggle[r][c]
    visited.append((r, c))

    if letter in trie:
        now_word += letter

        if trie[letter]['valid']:
            print('Found "{}" {}'.format(now_word, direction))

        neighbors = get_neighbors(r, c)
        for n in neighbors:
            dfs(n[0], n[1], visited[::], trie[letter], now_word, direction + " " + n[2])


def main(trie_node):
    """Initiate the search for words in boggle"""
    trie_node = build_trie(english_words, trie_node)

    # print the board
    print("Given board")
    for i in range(lenr):print (boggle[i])
    print ('\n')

    for r in range(lenr):
        for c in range(lenc):
            letter = boggle[r][c]
            dfs(r, c, [], trie_node, '', 'directions from ({},{})({}) go '.format(r, c, letter))


if __name__ == '__main__':
    main(trie_node)







