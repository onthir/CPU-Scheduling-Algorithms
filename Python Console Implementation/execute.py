import time
from process import *
import statistics

class Execution:

    def __init__(self):
        self.processes = []
        self.avg_tat = 0
        self.avg_wt = 0
        self.algo = ""

        with open("process_table.txt", "r") as file:
            content = file.readlines()

        self.algo = content[0].strip()
        if self.algo == "first":
            print("Detected Algorithm: First Come First Serve Scheduling Algorithm")
        elif self.algo == "shortest":
            print("Detected Algorithm: Shortest Job Next Scheduling Algorithm")

    # first come first serve
    def get_processes(self):
        # ask user
        with open("process_table.txt", "r") as file:
            content = file.readlines()
        self.algo = content[0]
        # create objects
        for cont in content[1:]:
            splitted = cont.split(",")
            if splitted[0].isalnum():
                # create process obj
                processObj = Process(splitted[0], splitted[1], splitted[2], 0, 0)
                self.processes.append(processObj)


        return self.processes

    # re-arrange the processes
    def rearrange_processes(self,factor):
        afterProcesses = []
        # factor choices are : [arrival_time, cpu_burst]
        if factor.lower() == "time":
            # arrange based on time
            processes = self.get_processes()
            for p in processes:
                if int(p.getArrivalTime()) == 0:
                    afterProcesses.insert(0, p)
                # check if current process time and last inserted time are same
                if p.getArrivalTime() == afterProcesses[len(afterProcesses)-1].getArrivalTime():
                    # switch based on id
                    if p.getProcessID() < afterProcesses[len(afterProcesses)-1].getProcessID():
                        # replace indexes
                        afterProcesses.insert(len(afterProcesses)-1, p)
                        
            sorted_processes = sorted(processes, key=lambda x: x.arrival_time)
            for process in sorted_processes:
                if not process in afterProcesses:
                    afterProcesses.append(process)
            # now the process is sorted return the sorted one
            

        elif factor.lower() == "cpu":
            # arrange based on burst
            processes = self.get_processes()
            for p in processes:
                if int(p.getArrivalTime()) == 0:
                    afterProcesses.insert(0, p)
            
            sorted_processes = sorted(processes, key=lambda x: x.cpu_burst)
            for process in sorted_processes:
                if not process in afterProcesses:
                    afterProcesses.append(process)
            # now the process is sorted return the sorted one
        return afterProcesses

    # execute algorithm
    def execute_algorithm(self):
        TAT = []        # turn around time
        WT = []         # waiting time
        # execute
        processes = []
        if self.algo == "first":
            processes = self.rearrange_processes('time')
        elif self.algo == "shortest":
            processes = self.rearrange_processes('cpu')
        endTimes = []
        for process in processes:
            # CALCULATE THE TURNAROUND TIME
            time = process.getArrivalTime()
            cpu_burst = process.getCpuBurst()
            # append the endtimes of each process
            if len(endTimes) == 0:
                endTimes.append(int(cpu_burst))
            else:
                end = int(endTimes[len(endTimes)-1]) + int(cpu_burst)
                endTimes.append(end)
        
        i = 0
        for p in processes:
            tat = int(endTimes[i]) - int(p.getArrivalTime())
            wt = tat - int(p.getCpuBurst())
            p.setTAT(tat)
            p.setWT(wt)
            i += 1

        self.avg_tat =  statistics.mean(tat.TAT for tat in processes)
        self.avg_wt =  statistics.mean(tat.WT for tat in processes)

        return self.avg_tat, self.avg_wt
            
    def main(self):
        # create the table
        print("------------------------------------\n| PID\t|\tTAT\t|\tWT |\n------------------------------------")
        self.execute_algorithm()
        for process in self.processes:
            print("| " + str(process.process_id)+"\t|\t" + str(process.TAT)+"\t|\t"+str(process.WT)+"  |")

        print("------------------------------------")
        print("Average TAT: ", self.avg_tat)
        print("Average WT: ", self.avg_wt)
        
obj = Execution()
print(obj.main())


