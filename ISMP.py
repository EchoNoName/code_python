def interval_scheduling(intervals):
    # Sort intervals by their end times
    intervals.sort(key=lambda x: x[1])
    # Initialize an empty list to store selected intervals
    selected_intervals = []
    
    # Track the end time of the last added interval
    last_end_time = float('-inf')

    for interval in intervals:
        # Unpacks the tuples
        start, end = interval
        # If the start time of the current interval is after the last end time, select it
        if start >= last_end_time:
            # Add the Interval to the set of Selected Intervals
            selected_intervals.append(interval)
            # Update the end time to the end time of the newest interval
            last_end_time = end
    
    return selected_intervals

intervals = [(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)]
print(interval_scheduling(intervals))