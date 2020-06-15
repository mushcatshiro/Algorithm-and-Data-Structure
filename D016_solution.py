"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
•	record(order_id): adds the order_id to the log
•	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible
"""

"""
hash table
"""
        

class ERecords():
    """docstring for ERecords"""
    def __init__(self):
        self.records = self.create_records()

    def create_records(self):
        # return 'some data structure'
        return []
        
    def record(self, order_id):
        self.records.append(order_id)
        return True

    def get_last(self, i):
        return self.records[-i]


def test():
    q = ERecords()

    l = [4, 5, 2, 7, 1, 9]

    for i in l:
        q.record(i)

    assert q.get_last(1) == 9, 'incorrect value'
    assert q.get_last(2) == 1, 'incorrect value'

test()