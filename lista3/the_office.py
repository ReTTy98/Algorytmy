import random


class Client:
    def __init__(self):
        self.task_type = random.choice(['A', 'B', 'C'])
        self.task_difficulty = random.randint(1, 10)

    def __str__(self):
        return f'Client with a type {self.task_type} task, difficulty {self.task_difficulty}'


class Worker:

    def __init__(self, specialisation):
        self.specialisation = specialisation
        self.current_client = None
        self.job_left = 0
        self.num = None
        self.clients_handled = 0

    @property
    def is_busy(self):
        return self.job_left >= 1

    def assign_client(self, client):
        if not self.is_busy and (self.specialisation == 'E' or client.task_type == self.specialisation):
            self.current_client = client
            self.job_left = client.task_difficulty
            self.clients_handled += 1
            print(f'worker {self.num}{self.specialisation} will handle', client)
        else:
            raise ValueError("Can't handle such task!")

    def tick(self):
        if self.job_left != 0:
            self.job_left -= 1

    def __str__(self):
        return f'Worker {self.num}{self.specialisation} that has serviced {self.clients_handled} clients today'


class Office:
    def __init__(self):
        self.free_worker_num = 0
        
        self.workers = []
        self.worked_time = 0;

    def add_worker(self, worker):
        worker.num = self.free_worker_num
        self.free_worker_num += 1
        self.workers.append(worker)

    @property
    def no_one_is_working(self):
        for worker in self.workers:
            if worker.is_busy:
                return False

        return True

    def try_helping_client(self, client):
        for worker in self.workers:
            try:
                worker.assign_client(client)
                return
            except ValueError:
                pass

        raise ValueError('Could not find a viable worker for this client')

    def tick(self):
        self.worked_time += 1

        for worker in self.workers:
            worker.tick()


    def print_summary(self):
        print('======= SUMMARY =======')
        print()

        print('# TIME')
        print(f'Simulation ticks: {self.worked_time}')
        print()

        print('# WORKERS')
        for worker in self.workers:
            print(worker)
        print()
        



if __name__ == '__main__':

    

    for i in range(5):
        print(Client())