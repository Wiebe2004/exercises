# Write your code here
def format_time(hours, minutes, seconds):

    if len(str(hours)) < 2:
        hours = "0" + str(hours)
    if len(str(minutes)) < 2:
        minutes = "0" + str(minutes)
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)

    return f'{hours}:{minutes}:{seconds}'