class RandomizedSet(object):

    def __init__(self):
        import random
        self.el = set()
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.el:
            return False
        self.el.add(val)
        return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.el:
            self.el.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.sample(self.el, 1)[0] 

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()