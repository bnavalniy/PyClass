seconds_input = float(input("Enter time > 1000 in seconds:"))
# Hours
float_hours = seconds_input / 3600
# Minutes
float_minutes = seconds_input / 60
time_message = (
    f"{int(float_hours)}h:"
    f"{int(float_minutes)}m:"
    f"{int(seconds_input)}s"
)
print(time_message)
