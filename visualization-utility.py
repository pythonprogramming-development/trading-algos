def exclusive_time(n, logs):
    exclusive_times = [0] * n
    prev_time = None
    start_times = {}

    for log in logs:
        function_id, action, timestamp = log.split(':')
        function_id, timestamp = int(function_id), int(timestamp)

        if action == 'start':
            if not (prev_time is None):
                exclusive_times[start_times[function_id]] += timestamp - prev_time
            start_times[function_id] = timestamp
            prev_time = timestamp
        else:  # action == 'end'
            exclusive_times[function_id] += timestamp - start_times.pop(function_id) + 1
            prev_time = timestamp + 1

    return exclusive_times

# Example usage:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(exclusive_time(n, logs))  # Output: [3, 4]
