class Bot:

    def __init__(self):
        self._data_items = []
        self.list = []

    def Sum(self):
        # makes sure there are atleast 2 numbers to sum
        if len(self._data_items) > 1:
            # pulls off top two integers from stack for manipulation
            top = self._data_items.pop()
            bottom = self._data_items.pop()
            sum = top + bottom

            # emulating push
            self._data_items.append(bottom)
            self._data_items.append(top)
            return sum

        else:
            print("not enough data items in stack")

    def Triple(self):
        PreVal = self._data_items.pop()
        NewVal = PreVal * 3
        # emulating push
        self._data_items.append(PreVal)
        self._data_items.append(NewVal)

    def Delete(self):
        self._data_items.pop()

    def Main(self):
        # iterates through list that has already converted string numbers to ints
        # adds all integers to _data_items
        for i in self.list:
            if type(i) == int:
                self._data_items.append(i)
            elif i == "A":
                # emulates push of the two summed numbers calculatd using Sum()
                self._data_items.append(self.Sum())
                # run A method
            elif i == ("T"):
                self.Triple()
                # run T method
            elif i == ("D"):
                self.Delete()
                # run "D" Method
                pass

    """
    Only runs once at beginning
    """

    def Start(self):
        Unfilt_List = []
        run = True
        while run == True:
            add = input(
                "enter element to add to list, otherwise enter finished ")
            if add != "finished":
                Unfilt_List.append(add)
            else:
                run = False

        new_list = [int(x) if x.isdigit() else x for x in Unfilt_List]
        thing.list = new_list
        print("input", thing.list)
        thing.Main()
        print("output", thing._data_items)


thing = Bot()
thing.Start()
