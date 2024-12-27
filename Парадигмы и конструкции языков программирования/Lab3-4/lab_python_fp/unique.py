class Unique(object):
    def __init__(self, items, **kwargs):
        try:
            kwargs['ignore_case']
            self.ignore_case = True
        except KeyError:
            self.ignore_case = False
        self.items = items
        self.data = []
        self.coded_data = []
        self.items_index = 0
        while self.items_index != len(self.items):
            self.__iter__()

    def __next__(self):
        self.items_index +=1

    def __iter__(self):
        code_num = 128
        curr_coded_num = 0
        for i in str(self.items[self.items_index]):
            curr_coded_num = 0
            ASCII_i_num = ord(i)
            if self.ignore_case:
                if 97 <= ASCII_i_num <= 122:
                    ASCII_i_num -= 32
            curr_coded_num = curr_coded_num * code_num + ASCII_i_num
        if curr_coded_num not in self.coded_data:
            self.data.append(self.items[self.items_index])
            self.coded_data.append(curr_coded_num)
        self.__next__()
        return self
    def get_data(self):
        return self.data
if __name__ == "__main__":
    data = ['asd','aSd', 'ASd', 'ASD','asD','ADS']
    t = Unique(data, ignore_case=True)
    print(t.get_data())