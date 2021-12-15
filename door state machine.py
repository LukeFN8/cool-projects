door_state=2
lock_door=0
times=int(input('enter the number of times you want to play the simulation: '))
for item in range(times):
    print('what do you want to do?')
    print()
    state_choose=int(input('to close enter 1, to open enter 2, to lock enter 3: '))
    print()
    if state_choose==1 and door_state==2 and lock_door==0:
        print ('the door is closed')
        print()
        door_state=1
    elif state_choose==1 and door_state==1:
        print('the door is alredy closed')
        print()
    elif state_choose==1 and door_state==2 and lock_door==1:
        print('the door is locked and open you are unable to close the door')
        print()
    elif state_choose==2 and door_state!=2 and lock_door==0:
        print('the door is open')
        print()
        door_state=2
    elif state_choose==2 and door_state==2:
        print('the door is alredy open')
        print()
    elif state_choose==2 and door_state==1 and lock_door==1:
        print('the door is locked you cant open it')
        print()
    elif state_choose==3 and door_state==1 and lock_door==0:
        print('you locked the door')
        print()
        lock_door=1
    elif state_choose==3 and door_state==2 and lock_door==0:
        print('the door is now unable to close')
        print()
        lock_door=1
    elif state_choose==3 and door_state==1 and lock_door==1:
        print('the door is now unlocked')
        lock_door=0
        print()
    elif state_choose==3 and door_state==2 and lock_door==1:
        print('the door is now open and unlocked')
        lock_door=0
        print()

