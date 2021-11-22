import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
    
treadObj = threading.Thread(target=takeANap)
treadObj.start()

print('End of program.')