from imp import reload

def status(module): print('realoding', module.__name__, '...')

def tryreload(module):
    try:reload(module)
    except: print('ERRRORRRRRR %s'%module)

def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        for attrobj in module.__dict__.values():
            if str(type(attrobj)) == "<class 'module'>":
                transitive_reload(attrobj,visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if str(type(arg)) == "<class 'module'>":
            transitive_reload(arg,visited)
            

if __name__ == '__main__':

    def tester(reloader, modname):
        import importlib, sys
        if len(sys.argv) > 1: modname = sys.argv[1]
        module = importlib.import_module(modname)
        reloader(module)

    tester(reload_all, 'reloadall')
    tester(reload_all, 'xy')
    
    

    
            
                
