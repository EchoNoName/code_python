def interval_scheduling(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    # Initialize an empty list to store selected intervals
    selected_intervals = []
    
    # Track the end time of the last added interval
    last_end_time = float('-inf')

    count = 1
    #Initiate count

    while intervals:
        selected_intervals.append(count)
        #uses count to seperate the seperate intervals schedules
        for i, interval in enumerate(intervals):
            start, end = interval
            #Loops through the intervals and assigns start and end values using tuples
            # If the start time of the current interval is after the last end time, select it
            if start >= last_end_time:
                selected_intervals.append(interval)
                intervals[i] = 0
                #Make used interval 0
                last_end_time = end
        intervals = [i for i in intervals if i != 0]
        #removes all used intervals
        count += 1
        last_end_time = float('-inf')
        #reset end time for next loop
    
    return selected_intervals

intervals = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
print(interval_scheduling(intervals))


