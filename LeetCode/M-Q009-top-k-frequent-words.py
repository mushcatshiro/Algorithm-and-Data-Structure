"""
Given a non-empty list of words,
return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency,
then the word with the lower alphabetical order comes first.

e1
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

e2
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up: Try to solve it in O(n log k) time and O(n) extra space.

tags: bucket sort, min heap
"""


def solution(words, k):
    tmp = {}
    for word in words:
        if word not in tmp:
            tmp[word] = 1
        else:
            tmp[word] += 1
    bucket_required = max(tmp.values())
    bucket = [[] for _ in range(bucket_required + 1)]
    for key, value in tmp.items():
        bucket[value].append(key)
    for i in range(len(bucket)):
        bucket[i] = sorted(bucket[i])
    ret = []
    for i in range(bucket_required, 0, -1):
        if bucket[i]:
            for j in bucket[i]:
                ret.append(j)
                if len(ret) == k:
                    return ret


"""
its somehow ugly due with bucket sort approach and without importing packages.
"""