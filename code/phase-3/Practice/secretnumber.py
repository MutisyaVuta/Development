available_time = 23
work_time = 1

if available_time + work_time >24:
    print("Invalid time!");
elif (available_time + work_time) >= 24:
    print("Full schedule!");
else:
    leftover_time = abs(24-available_time + work_time);
    print("Leftover time: ", leftover_time)
print("End of Day")