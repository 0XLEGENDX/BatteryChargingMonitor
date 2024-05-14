import psutil
import time
import win32api
import win32con
import win32gui
import os
from datetime import datetime

def hide_console():
    # Hide the console window
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide , win32con.SW_HIDE)


storepath = r"C:\Users\anura\OneDrive\Documents\chargingData.txt"
totalTime = r"C:\Users\anura\OneDrive\Documents\totalTime.txt"



def logData(timem,message,seconds=0):

    datetime_obj = datetime.fromtimestamp(timem)

    # Extract the date and time in a specific format
    date_str = datetime_obj.strftime('%Y-%m-%d')  # Format: YYYY-MM-DD
    time_str = datetime_obj.strftime('%H:%M:%S')

    f = open(storepath,'r+')
    data = f.read()
    data += "\n" + str(date_str) + " " + time_str + " " + message
    f.write(data)
    f.close()


    f = open(totalTime,"r+")
    data = f.read()
    if(data == ""):
        data = int(seconds)
    else:
        data = int(data) + int(seconds)
    f.close()

    f = open(totalTime,"w")
    f.write(str(data))
    f.close()




# def readState():

#     if(os.path.exists(storepath)):

#         f = open(stateStore,"r+")
#         data = f.read()
#         f.close()
#         return True if data == "True" else False

#     return False

# def storeState():

#     if(storepath)






def monitor_charging():
    # Initialize charging status
    prev_status = psutil.sensors_battery().power_plugged
    start_time = None

    while True:
        # Check current charging status
        current_status = psutil.sensors_battery().power_plugged

        # If charging status changes
        if current_status != prev_status:
            if current_status:
                # Charging started
                # print(current_status)
                start_time = time.time()
                logData(time.time(), f"Charging Started")
            else:
                # Charging stopped
                if start_time is not None:
                    charging_time = time.time() - start_time
                    # print("Charging Stopped")
                    logData(  time.time(), f"Charging stopped. Connected time: {charging_time:.2f} seconds",charging_time)
            prev_status = current_status

        time.sleep(5)  # Check status every second



if __name__ == "__main__":
    hide_console() 
    monitor_charging()
