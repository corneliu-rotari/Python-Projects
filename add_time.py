def add_time(start, duration, day= ""):
    time = start.split()
    hours = time[0].split(":")
    addit = duration.split(":")
    
    time_stamp = time[1]
    hour1 = hours[0]
    minutes1 = hours[1]
    hour2 = addit[0]
    minutes2 = addit[1]

    ceas = 0
    next_day = 0
    ora = 0
    week = {
        "monday" : 0,
        "tuesday" : 1,
        "wednesday" : 2,
        "thursday" : 3,
        "friday" : 4,
        "saturday" : 5,
        "sunday" : 6 
    }
    
    minutes_final =  int(minutes1) + int(minutes2)
    if int(minutes1) + int(minutes2) > 60:
        minutes_final %= 60
        if minutes_final < 10:
            aux = "0"
            aux += str(minutes_final)
            minutes_final = aux
        ora += (int(minutes1) + int(minutes2))// 60
    
    ceas = (ora + int(hour1)+int(hour2))
    if ceas >= 12:
        next_day += (ora + int(hour1)+int(hour2)) // 24
        if time_stamp == "AM" and ceas < 24:
            time_stamp = "PM"
        elif time_stamp == "PM" : 
            time_stamp = "AM"
            next_day += 1
        ceas %= 12
    if ceas == 0 and time_stamp == "AM" : ceas = "12"


    new_time = str(ceas) + ':' + str(minutes_final) + " "+ time_stamp

    if hour2 == "0" and minutes2 == "00" :
        new_time = start

    if len(day) > 1 :
        if next_day > 0:
            indent = (week[day.lower()] + next_day % 7) %7 
            for k,v in week.items():
                if v == indent:
                    day = k
        new_time += ", " + day.lower().capitalize()

    
    if next_day > 0: 
        if next_day == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(next_day) +" days later)"   

    

    return new_time
print(add_time("2:26 AM", "6:00", "friday"))