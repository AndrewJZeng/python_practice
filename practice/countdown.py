import time, subprocess

def main():
    timeLeft = 15
    while timeLeft > 0:
        print(timeLeft)
        time.sleep(1)
        timeLeft -= 1
        
    subprocess.Popen(['start', 'alarm.wav'], shell=True)
    
if __name__ == '__main__':
    main()