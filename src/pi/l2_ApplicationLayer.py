import l3_DomainLayer as dl

def performCommand(command):
    car = dl.AICar()
    if(command == 1):
        car.startAIDriving()
    elif (command == 2):
        car.startManualDriving()