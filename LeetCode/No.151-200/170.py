class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.HashMap = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.HashMap[number] = self.HashMap.get(number, 0)+1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.HashMap:
            diff = value - i
            if diff in self.HashMap:
                if diff != i or (diff == i and self.HashMap.get(i) >= 2):
                    return True

        return False



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)

if __name__ == '__main__':
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    print obj.find(4)
    print obj.find(7)