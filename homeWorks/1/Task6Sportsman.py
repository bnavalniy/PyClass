first_distance = float(input("Enter distance: "))
goal = int(input("Enter your goal: "))
i = 1
progress = first_distance
while True:
    print(f"{i}-day: {progress}")
    i += 1
    progress += (progress * 0.1)
    if progress >= goal:
        print(f"On {i}-day sportsman has been reached the goal at least: {goal} km")
        break
