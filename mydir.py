seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = seplen * sepchr
    if verbose:
        print(sepline)
        print('name:', module.__name__, end ='')
        try:
            print('file:', module.__file__)
        except AttributeError:
            print()
        print(sepline)
    count = 0
    for attr in sorted(module.__dict__):
        print('%02d) %s'%(count, attr), end = ' ' )
        if attr.startswith('_'): print('<built-in name>')
        else: print(getattr(module, attr))
        count += 1
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    import math
    listing(math)
    import xy
    listing(xy)

    
