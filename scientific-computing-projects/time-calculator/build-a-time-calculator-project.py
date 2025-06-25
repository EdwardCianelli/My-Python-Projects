** start of main.py **

def add_time(start, duration, starting_day=None):
    time_part = start.split()
    clock = time_part[0]
    ampm = time_part[1]

    hour, minute = clock.split(":")
    hour = int(hour)
    minute = int(minute)

    if ampm == "PM" and hour != 12:
        hour += 12
    if ampm == "AM" and hour == 12:
        hour = 0

    dur_hour, dur_min = duration.split(":")
    dur_hour = int(dur_hour)
    dur_min = int(dur_min)

    total_minutes = hour * 60 + minute + dur_hour * 60 + dur_min

    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    total_days = total_minutes // (24 * 60)

    if new_hour_24 == 0:
        final_hour = 12
        period = "AM"
    elif new_hour_24 < 12:
        final_hour = new_hour_24
        period = "AM"
    elif new_hour_24 == 12:
        final_hour = 12
        period = "PM"
    else:
        final_hour = new_hour_24 - 12
        period = "PM"

    result = str(final_hour) + ":" + str(new_minute).zfill(2) + " " + period

    if starting_day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = days.index(starting_day.lower().capitalize())
        new_day = days[(day_index + total_days) % 7]
        result += ", " + new_day

    if total_days == 1:
        result += " (next day)"
    elif total_days > 1:
        result += " (" + str(total_days) + " days later)"

    return result


** end of main.py **

