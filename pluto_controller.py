import dagger
import keyboard  
from time import sleep

Pluto_IP = "192.168.4.1"
Pluto_PORT = 23

pluto = dagger.PlutoConnection()
pluto.connect((Pluto_IP, Pluto_PORT))
rc = dagger.SetRawRC(pluto)
pluto_control = dagger.PlutoControl(pluto)

def take_off():
    print("Taking off...")
    pluto_control.take_off()
    sleep(10) 
    print("Drone in air")

def disarm_drone():
    print("Disarming drone...")
    rc.disarm_drone()
    print("Drone disarmed.")

def control_drone():
    while True:
        if keyboard.is_pressed('w'):
            rc.roll(0)    
            rc.pitch(1)  
            print("Moving forward")
        elif keyboard.is_pressed('s'):  
            rc.roll(0)
            rc.pitch(-1)  
            print("Moving backward")
        elif keyboard.is_pressed('a'): 
            rc.yaw(-1)    
            print("Turning left")
        elif keyboard.is_pressed('d'):  
            rc.yaw(1)    
            print("Turning right")
        elif keyboard.is_pressed('q'):
            disarm_drone()
            break
        else:
            rc.roll(0)
            rc.pitch(0)
            rc.yaw(0)     
            print("Hovering")
        
        
        sleep(0.1)

def main():
    take_off()
    try:
        control_drone()
    except KeyboardInterrupt:
        disarm_drone()
        print("Exiting program.")

if __name__ == "__main__":
    main()
