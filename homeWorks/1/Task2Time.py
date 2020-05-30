seconds_input = int(input("Enter time in seconds:"))
# Hours
hours = seconds_input // 3600
# Minutes
minutes = (seconds_input // 60) - (hours * 60)
seconds = seconds_input % 60
time_message = (
    f"{hours:02}:"
    f"{minutes:02}:"
    f"{seconds:02}"
)
print(time_message)
print(f"{hours:02}:{minutes:02}:{seconds:02}")
