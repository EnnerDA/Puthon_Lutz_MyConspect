import time, sys
timer = time.perf_counter
def total(reps, func, *pargs, **kargs):
    '''Сумарное время выполнения функции func() reps раз.
        Возвращает суммарное время и последний результат'''
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return elapsed, ret

def bestof(reps, func, *pargs, **kargs):
    '''Самая быстрая функция func() среди reps запусков. 	
    Возвращает (лучшее время, последний результат)'''
    besttime = float('inf')
    bedtime = 0
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < besttime:
            besttime = elapsed
        if elapsed > bedtime:
            bedtime = elapsed
        
    print(f'\tFrom {func.__name__} in {reps} reps:')
    if len(str(ret)) < 60:
        print(f'besttime = {besttime}, \nbedtime = {bedtime}, \nresult = {ret[1]}')
    else:
        print(f'''besttime = {besttime} \nbedtime = {bedtime} \nto many symbols to write the result...''')
    

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    '''Лучшее суммарное время:
    (лучшее время из repsl запусков (суммарное время reps2 запусков func))'''	
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
