def minutes_since_last_departure(departure_times, current_time):
    # Helper function to convert "HH:MM" to total minutes from 00:00
    def to_minutes(time_str):
        hh, mm = time_str.split(':')
        return int(hh) * 60 + int(mm)

    # Convert current time to minutes
    current_time_minutes = to_minutes(current_time)

    # Convert each departure time to minutes
    departures_in_minutes = [to_minutes(t) for t in departure_times]

    # Initialize 'last_departure' to None. This will store the latest departure < current_time.
    last_departure = None

    for d in departures_in_minutes:
        if d < current_time_minutes:  # bus departed strictly before current time
            last_departure = d

    # If no bus departed before current_time, return -1
    if last_departure is None:
        return -1

    # Otherwise, return the difference in minutes
    return current_time_minutes - last_departure


# Example usage:
departure_times_1 = ["12:30", "14:00", "19:55"]
current_time_1 = "14:30"
print(minutes_since_last_departure(departure_times_1, current_time_1))
# Expected output: 30

departure_times_2 = ["00:00", "14:00", "19:55"]
current_time_2 = "00:00"
print(minutes_since_last_departure(departure_times_2, current_time_2))
# Expected output: -1
