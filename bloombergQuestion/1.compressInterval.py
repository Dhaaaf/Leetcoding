def compress(times):
  sorted_times = sorted(times, key = lambda x : x[0])
  combined = [sorted_times[0]]
  
  for current_interval in sorted_times[1:]:
    last_start, last_end = combined[-1]
    current_start, current_end = current_interval
    
    if current_start <= last_end:
      if current_end > last_end:
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval)
  return combined