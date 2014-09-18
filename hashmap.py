""" Implementation of a hash table in Python. """

# Class 

class hashmap():
    def __init__(self, n=20):
        """ Initialize a hash map with n buckets. """
        self.n = n
        self.buckets = [None] * self.n
        
