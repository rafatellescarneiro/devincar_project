import time

def execution_time(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print(f'\nTempo de execução da função {method.__name__} foi {te-ts:.2f} sec')

        return result

    return timed