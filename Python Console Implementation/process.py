class Process:

    # instance variables
    process_id = 0
    arrival_time = 0
    cpu_burst = 0
    TAT = 0
    WT = 0

    # constructor
    def __init__(self, pid, at, cb, tat, wt):
        self.process_id = pid
        self.arrival_time = at
        self.cpu_burst = cb
        self.TAT = tat
        self.WT = wt

    # getter and setter
    def getProcessID(self):
        return int(self.process_id)
    def getArrivalTime(self):
        return int(self.arrival_time)
    def getCpuBurst(self):
        return int(self.cpu_burst)
    def getTAT(self):
        return self.TAT
    def getWT(self):
        return self.WT
    
    # setters
    def setProcessID(self, id):
        self.process_id = id
    def setArrivalTime(self, time):
        self.arrival_time = time
    def setCpuBurst(self, cpu):
        self.cpu_burst = cpu
    def setTAT(self, tat):
        self.TAT = tat
    def setWT(self, wt):
        self.WT = wt
    