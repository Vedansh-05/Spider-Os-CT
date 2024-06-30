def calculate_waiting_time(processes, n, burst_time, waiting_time):
    # Waiting time for the first process is 0
    waiting_time[0] = 0
    
    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

def calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

def calculate_average_times(processes, n, burst_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculate waiting time for all processes
    calculate_waiting_time(processes, n, burst_time, waiting_time)
    
    # Calculate turnaround time for all processes
    calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time)
    
    # Calculate total waiting time and total turnaround time
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
    
    # Calculate average waiting time and average turnaround time
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n
    
    # Print results
    print(f"{'Process':<10}{'Burst Time':<12}{'Waiting Time':<14}{'Turnaround Time'}")
    for i in range(n):
        print(f"{processes[i]:<10}{burst_time[i]:<12}{waiting_time[i]:<14}{turnaround_time[i]}")
    
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

# Example usage
processes = ['P1', 'P2', 'P3']
burst_time = [24, 3, 3]
n = len(processes)

calculate_average_times(processes, n, burst_time)
