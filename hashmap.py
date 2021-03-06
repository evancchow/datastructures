""" Implementation of a hash table in Python. """

# Class for a Linked List. This is a separate-chaining hash table.
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class hashmap():

    def __init__(self, n=20):
        """ Initialize a hash map with n buckets. """
        self.numBuckets = n
        self.buckets = [None] * (self.numBuckets + 1)
        self.totalNodeCount = [0] * (self.numBuckets + 1)
    
    def put(self, val):
        # Insert at end of linked list for relevant bucket (by hash).
        hashed = self.hash(val)
        if not self.buckets[hashed]: # empty case
            self.buckets[hashed] = Node(val)
        else:
            # Iterate to end of bucket's linked list, and add node.
            last = self.buckets[hashed]
            while last.next:
                last = last.next
            last.next = Node(val)
        self.totalNodeCount[hashed] += 1

        # Rebalance table on average > 3 nodes / bucket, and rehash all keys.
        if (sum(self.totalNodeCount) / self.numBuckets) > 3:
            self.buckets.extend([None] * (self.numBuckets))
            self.numBuckets *= 2
            for i in range(len(self.numBuckets / 2)):
                curr = self.buckets[i]
                while curr:
                    # Move node to new bucket. Corner case: same bucket.
                    
                    curr = curr.next
        
    def hash(self, string):
        """ Hash a string. We're using a super simplistic
        (total sum of all ord(chars)) % (total # of buckets), 
        but we could be fancy and use something like
        "hashlib.md5(string.encode())" . """
        return (sum((ord(i) for i in str(string)))) % self.numBuckets

    def items(self):
        """ Print all items by bucket in the hashmap. """
        for ix, bucket in enumerate(self.buckets):
            if not isinstance(bucket, Node):
                print "Bucket {} is empty".format(ix)
                continue
            vals = []
            curr = bucket
            while curr:
                vals.append(curr.val)
                curr = curr.next
            print "Bucket {0} has: {items!s}".format(ix, items=vals)

    def numNodes(self):
        """ Return total # of nodes. """
        return self.totalNumNodes

    def numBuckets(self):
        """ Return total # of buckets. """
        return self.numBuckets

hm = hashmap()        
hm.put(1)
hm.put(2)
hm.put(3)
