import l2_ApplicationLayer as al

def startRobot():
    print("Choose an action:")
    print("1. AI + Driving;")
    print("2. Manual control (To Do);")
    print("To cancel action press 'q' in window...")
    
    al.performCommand(int(input()))