def countLines(file_name):
    res = len(open(r''+file_name).readlines())
    print('There are', res, 'lines in', file_name)

def countChars(file_name):
    res = len(open(r''+file_name).read())
    print('There are', res, 'chars in', file_name)
    
    
def tester():
    # вставить возможность подхватывать код из командной строки, мать её
    try:
        fname = input('Введиет имя файла, или жмякните Enter\n')
        if fname.strip() == '': fname = 'mymod.py'
        countLines(fname)
        countChars(fname)
    except:
        print('Мы не нашли что вы хотели, поэтому протестим на этом же файле')
        fname = 'mymod.py'
        countLines(fname)
        countChars(fname)
        

if __name__ == '__main__':
    tester()
