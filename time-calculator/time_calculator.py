def add_time(start, duration, dow=''):

    days_of_week = {
        'Sunday': 0, 
        'Monday': 1, 
        'Tuesday': 2, 
        'Wednesday': 3, 
        'Thursday': 4, 
        'Friday': 5, 
        'Saturday': 6
    }

    hrmin, ampm = start.split()
    start_hr, start_min = hrmin.split(':')
    duration_hr, duration_min = duration.split(':')

    start_hr = int(start_hr)
    start_min = int(start_min)
    duration_hr = int(duration_hr)
    duration_min = int(duration_min)

#convert to 24h format (assume default is sunday) ---> convert to function if possible
    converted_hr = 0
    if dow == '':
        if ampm == 'PM':
            converted_hr = start_hr + 12
        else:
            converted_hr = start_hr
    else:
        if ampm == 'PM':
            converted_hr = 24 * days_of_week[dow.capitalize()] + (start_hr + 12)
        else:
            converted_hr = 24 * days_of_week[dow.capitalize()] + (start_hr)


# -----------------actual time operations----------------- #

# add the minutes, then carry over the excess to hours.
    total_min = start_min + duration_min
    final_min = total_min % 60

    extra_hr = total_min // 60
    total_hr = converted_hr + duration_hr + extra_hr
    final_hr = (total_hr % 24) % 12
    
    if final_hr == 0:
        final_hr = 12

    if dow == '':
        final_days = total_hr // 24
    else:
        final_days = ((total_hr // 24) - days_of_week[dow.capitalize()])

# -----------------format text results----------------- #
# Determine if AM or PM (Converts the total hrs to 24h format. 0-11 is AM, 12-23 is PM)
    if (total_hr % 24) <= 11:
        ampm = 'AM'
    else: 
        ampm = 'PM' 

# Check if the minute only has one digit (e.g. 1:3 AM should be 1:03 AM)
    if final_min < 10:
        final_min = '0' + str(final_min)

    final_dow = ''
    if dow != '':   
        for k,v in days_of_week.items():
            if v == (days_of_week[dow.capitalize()] + final_days) % 7:
                final_dow = ', '  + k

    optional = ''
    if final_days > 1:
        optional = f' ({final_days} days later)'
    elif final_days == 1:
        optional = ' (next day)'

    converted_time = f'{final_hr}:{final_min} {ampm}{final_dow}{optional}'

    return converted_time