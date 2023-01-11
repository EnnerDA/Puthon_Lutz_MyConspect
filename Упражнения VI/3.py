class MyList:
    def __init__(self, user_list = []):
        self.__work_list = user_list[:]
    def __str__(self):
        return 'My list: ' + str(self.__work_list)
    def __repr__(self):
        return str(self.__work_list)
    def append(self, data):
        print(f'do append {data} ... ', end ='')
        self.__work_list.append(data)
        print('ok!')
    def __add__(self, data):
        if type(data) == list: self.__work_list += data
        else: self.append(data)
        return self.__work_list
    def sort(self):
        print('no, nikakoi sortirovki bleat`')

        
class MyListSub(MyList):
    def __init__(self, user_list = []):
        self.__work_list = list(user_list)
        self.str_i = 0
        self.repr_i = 0
        self.append_i = 0
        self.add_i = 0
        self.sort_i = 0
        self.stdout = 0        
    def __str__(self):
        self.str_i += 1
        return 'My list: ' + str(self.__work_list)
    def __repr__(self):
        self.repr_i += 1
        return str(self.__work_list)
    def append(self, data):
        self.append_i += 1
        print(f'Do append {data} ... ', end ='')
        self.__work_list.append(data)
        print('ok!')
    def __add__(self, data):
        self.add_i += 1
        if type(data) == list: self.__work_list += data
        else: self.__work_list.append(data)
        return self.__work_list
    def sort(self):
        self.sort_i += 1
        print('No, nikakoi sortirovki bleat`')
    def print_stdout(self):
        self.stdout = (self.str_i + self.repr_i +
                       + self.append_i + self.add_i + self.sort_i)
        print(f''' ***
There are {self.stdout} operations:
self.str_i  = {self.str_i}
self.repr_i = {self.repr_i}
self.append_i = {self.append_i}
self.add_i = {self.add_i}
self.sort_i = {self.sort_i}
''')
    
    



def selftest():
    l1 = [1,2,3,4]
    x = MyList(l1)
    print(x)
    x
    x.append('spam')
    print(x)
    print(l1)
    x+1
    print()
    x + l1
    print(x)
    x.sort()
    x + [6,6,6]
    print(x)
    print(x.__dict__)

def selftest2():
    print('***** test 2 ****')
    l1 = [1,2,3,4]
    x = MyListSub(l1)
    print(x)
    x
    x.append('spam')
    print(x)
    print(l1)
    x+1
    print()
    x + l1
    print(x)
    x.sort()
    x + [6,6,6]
    print(x)
    x.print_stdout()
    
    
if __name__ == '__main__':
    selftest()
    selftest2()
