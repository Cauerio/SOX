import multiprocessing

def mi_proceso():
    print(f'Proceso hijo: PID {multiprocessing.current_process().pid}')

if __name__ == '__main__':
    print(f'Proceso padre: PID {multiprocessing.current_process().pid}')
    #print ("hola")
    
    proceso = multiprocessing.Process(target=mi_proceso)
    proceso.start()
    proceso.join()


    import multiprocessing

