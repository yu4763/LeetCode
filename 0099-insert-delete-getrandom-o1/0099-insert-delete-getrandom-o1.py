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
        items = list(self.el)  # Convert set to a list
        randomIndex = random.randint(0, len(items) - 1)  # Generate random index
        return items[randomIndex]  # Return random element