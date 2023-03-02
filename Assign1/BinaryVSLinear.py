import time
import random
random.seed(12345)

#


class Searching:

    def __init__(self, n):
        self.BinaryTime = 0.0
        self.LinearTime = 0.0
        self.k = None
        self.n = n
        self.list_source = []
        self.list_target = []

    def SourceListInit(self):
        # creates source list
        for i in range(self.n):
            self.list_source.append(random.random())

    def TargetListInit(self):
        SourceSize = len(self.list_source)

        # STARTING K VALUE
        self.k = 2

        # get half of k worth of elements from source, half of k worth from random
        for x in range(self.k // 2):
            # get random index from 0 to size of listsource
            SourceIndex = random.randint(0, self.n-1)

            # add number at random index to target list
            self.list_target.append(self.list_source[SourceIndex])
        for y in range(self.k // 2):
            # all numbers in the seed are below, so generating numbers from 1-10
            # and adding them to the list.
            self.list_target.append(random.randint(1, 10))

    # adds 1 to k everytime binary search is slower then linear
    # also updates targetlist

    def TimeChecker(self):
        print("\nafter 1000 runs with k value = ", self.k, "   Binary time totals to: ",
              self.BinaryTime, "and Linear time totals to: ", self.LinearTime)
        # if binary slower, add 1 to k for the targetl list, append value to target list.
        if self.LinearTime <= self.BinaryTime:
            self.k += 2
            print("Linear faster, adding 1 to k and updating target_list, running 100 tests with k value of: ", self.k)
            # same as TargetListInit, cant reuse due to range implementation
            SourceIndex = random.randint(0, self.n-1)
            # add number at random index to target list
            self.list_target.append(self.list_source[SourceIndex])
            self.list_target.append(random.randint(1, 10))
            test.SearchAndTest()
        else:
            print(self.list_source, "\n\n TARGET:", self.list_target)
            print("\n FINAL: With k value of:", self.k, "and n value of",
                  self.n, "Binary time is faster then Linear")
            print("Binary: ", self.BinaryTime,
                  "Linear: ", self.LinearTime, "\n")

    # testing sequence begins, will be updated using targetlistupdate throughout testing

    def SearchAndTest(self):
        self.BinaryTime = 0
        self.LinearTime = 0

        # Obtains times for specified k and n value using search methods.
        # Timechecker compares times as well as updates target list
        # runs test 1000 times for k value, adds total times together
        for i in range(1000):
            self.LinearTime += test.LinearSearch()
            self.BinaryTime += test.BinarySearch()
        test.TimeChecker()

    def BinarySearch(self):
        start = time.time()

        # sort the list_source
        self.list_source.sort()
        for x in self.list_target:
            low = 0
            high = len(self.list_source) - 1
            found = False
            while found == False:
                if high >= low:
                    mid = (high + low) // 2

                    # If element is present at the middle itself
                    if self.list_source[mid] == x:
                        found = True

                    # If element is smaller than mid, then it can only
                    # be present in left subarray
                    elif self.list_source[mid] > x:
                        high = mid - 1
                    # Else the element can only be present in right subarray
                    else:
                        low = mid + 1
                else:
                    # Element is not present in the array
                    found = None

        end = time.time()
        FinalTime = end-start
        return FinalTime

    # returns time of linear search
    def LinearSearch(self):
        start = time.time()

        for i in (self.list_target):
            for t in (self.list_source):
                if i == t:
                    pass
                else:
                    pass

        end = time.time()
        FinalTime = end - start
        return FinalTime

    def Main(self):
        # initalize lists
        test.SourceListInit()
        test.TargetListInit()

        # Compares times, updates k & target list if Binary slower
        test.SearchAndTest()


# 100 is the N value, change for reproducing tests
test = Searching(100)
test.Main()
