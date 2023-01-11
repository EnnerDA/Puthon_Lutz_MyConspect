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
    
    
if __name__ == '__main__':
    selftest()
