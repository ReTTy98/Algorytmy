from time import sleep

SIMULATION_TICK_TIME = 0

def run_simulation(office, queue):
    done = False

    while not done:
        could_help = True

        while could_help:
            try:
                if len(queue) != 0:
                    client = queue.head.value # Take the first client in queue
                    office.try_helping_client(client) # Try assigning him to the office workers
                    queue.pop() # If assigned, remove him from the queue
        
                else:
                    could_help = False
            except ValueError:
                could_help = False # If the client could not be assigned, make him wait
        
        if office.no_one_is_working:
            done = True

        print('tick!')
        office.tick()
        sleep(SIMULATION_TICK_TIME)

