def add_time(start, duration, day=None):
    # Maintaining Days in a week
    day_week = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }
    # Getting useful data from start string
    timebig, ampm = start.split()
    hour, minutes = timebig.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # Making the clock into 24 hour format
    if ampm == "PM":
        hour += 12

    # Getting data from duration
    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    # Calculating total hours, minutes
    totalminutes = minutes + duration_minutes
    finalminutes = totalminutes % 60
    extra_hours = totalminutes // 60
    totalhour = hour + duration_hour + extra_hours

    # final hours as per 12 Hour clock
    finalhour = (totalhour % 24) % 12

    # Edge case
    if finalhour == 0:
        finalhour = 12
    finalhour = str(finalhour)

    # total days 24 hr 1 day
    totalday = (totalhour // 24)

    # deciding mid day (AM/PM)
    finalampm = ""
    if (totalhour % 24) <= 11:
        finalampm = "AM"
    else:
        finalampm = "PM"

    # Handling single digit minutes case
    if finalminutes <= 9:
        finalminutes = '0' + str(finalminutes)
    else:
        finalminutes = str(finalminutes)
    # returning logic
    time_stamp = finalhour + ":" + finalminutes + " " + finalampm
    if day == None:
        if totalday == 0:
            return time_stamp
        if totalday == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(totalday) + ' days later)'
    else:
        finalday = (day_week[day.lower().capitalize()] + totalday) % 7
        for i, j in day_week.items():
            if j == finalday:
                finalday = i
                break
        if totalday == 0:
            return time_stamp + ', ' + finalday
        if totalday == 1:
            return time_stamp + ', ' + finalday + ' (next day)'
        return time_stamp + ', ' + finalday + ' (' + str(totalday) + ' days later)'