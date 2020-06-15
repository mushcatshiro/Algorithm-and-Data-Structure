"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries
"""

# trie

class TrieNode():
    """docstring for TrieNode"""
    def __init__(self):
        self.children = [None] * 26
        self.isEndWord = False
        
class Trie():
    """docstring for Trie"""
    def __init__(self):
        self.root = self.getNode()
        self.words = []

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def _IndexToChar(self, index):
        return chr(index)

    # can be refractor since insert, checkExist and findAllWords
    # all three share same staring
    def insert(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndWord = True

    def checkExist(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndWord

    def findAllWords(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                print('prefix not found')
                return False

            pCrawl = pCrawl.children[index]
            # we obtained the last word/node
        if pCrawl.isEndWord:
            print('prefix ends here, no other combinations')



        words = self._findAllWord(pCrawl, key)

        return words

    def _findAllWord(self, node, word):

        if node.isEndWord:
            self.words.append(word)

        for index in range(len(node.children)):
            if node.children[index]:
                self._findAllWord(node.children[index],\
                                  word+self._IndexToChar(index+97))


        return self.words



def testCheckEist():
    queryKeys = ['dog', 'deer', 'deal']

    t = Trie()

    for key in queryKeys:
        t.insert(key)

    return(t.checkExist('deer'))

def testFindAllWords():
    queryKeys = ['dog', 'deer', 'deal']

    t = Trie()

    for key in queryKeys:
        t.insert(key)

    return(t.findAllWords('de'))


# assert testCheckEist() == True, 'key DNE' # full copy of trie data structure
assert set(testFindAllWords()) == set(['deer', 'deal']), 'mismatch results'