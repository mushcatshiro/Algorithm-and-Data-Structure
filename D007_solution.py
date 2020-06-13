"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# since its decodable thus not considering any thing larger than 26 and smaller than 1
# since decoding chuncks of 1 or 2 digit integers

from itertools import permutations

dic = {}
ndic = {}
msg = '234'

class mapping:
    def __init__(self, dic):
        self.dic = dic
    def get_map (self):
        i = 0
        while i < 26:
            self.dic[i+1] = chr(97+i)
            i+=1
        return self.dic


def chkRange(msg):
    return True #if (int(msg) < 27 and int(msg) > 0)

# use recursion
def solution(msg):
    decoded_msg = []
    tmp1 = []
    tmp2 = []

    if len(msg) == 0:
        return []

    # empty list + tmp1 = tmp1
    if len(msg) > 0:
        tmp1.append(chr(96+int(msg[0])))
        tmp1 += solution(msg[1:])
        if tmp1:
            decoded_msg.append(tmp1)
    if len(msg) > 1 and int(msg[:2]) < 27:
        tmp2.append(chr(96+int(msg[:2])))
        tmp2 += solution(msg[2:])
        if tmp2:
            decoded_msg.append(tmp2)

    # decoded_msg += tmp1
    # decoded_msg += tmp2

    return decoded_msg
    

print(solution(msg))