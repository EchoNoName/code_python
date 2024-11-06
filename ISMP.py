def interval_scheduling(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    # Initialize an empty list to store selected intervals
    selected_intervals = []
    
    # Track the end time of the last added interval
    last_end_time = float('-inf')
    
    while intervals:
        count = 0
        selected_intervals.append(count)
        for interval in intervals:
            start, end = interval
            # If the start time of the current interval is after the last end time, select it
            if start >= last_end_time:
                selected_intervals.append(interval)
                intervals.remove(interval)
                last_end_time = end
        count += 1
        last_end_time = float('-inf')
    
    return selected_intervals

intervals = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
print("Maximum number of non-overlapping intervals:", interval_scheduling(intervals))


