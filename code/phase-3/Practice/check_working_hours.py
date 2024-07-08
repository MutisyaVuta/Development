def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper  
@check_working_hours
def sweep_floor(time):
    print("Sweeping the floor...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floor(2000)

wash_dishes(1430)

chop_vegetables(230)
