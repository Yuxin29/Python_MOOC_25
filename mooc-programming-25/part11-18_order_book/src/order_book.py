class Task:
    running_id = 1
    def __init__(self, description: str, programmer: str,  workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.status = False
        self.finished = "NOT FINISHED"
        self.id = Task.running_id
        Task.running_id += 1
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"
    def is_finished(self):
        return self.status
    def mark_finished(self):
        self.status = True
        self.finished = "FINISHED"
    def description(self):
        return self.description
    def programmer(self):
        return self.programmer
    def workload(self):
        return self.workload

class OrderBook:
    def __init__(self):
        self.all = []
        self.workers = []
    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.all.append(order)
        self.workers.append(order.programmer)
        
    @property
    def all_orders(self):
        return self.all
    @property
    def programmers(self):
        return self.workers
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    for order in orders.all_orders():
        print(order)
    print()
    for programmer in orders.programmers():
        print(programmer)