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

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]

        if pCrawl.isEndWord:
            return key
        else:
            tmp = []

            for char in pCrawl.children:
                if char and pCrawl.isEndWord:
                    tmp.append(key+'char')
                



        # return pCrawl != None and pCrawl.isEndWord


def test():
    queryKeys = ['dog', 'deer', 'deal']

    t = Trie()

    for key in queryKeys:
        t.insert(key)

    return(t.search('de'))

print(test())

assert test() == True, 'dont match' # full copy of trie data structure
assert test() == ['deer', 'deal'], 'wrong text'