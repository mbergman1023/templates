from naoqi import ALProxy
from multiprocessing import Process
import Queue
import threading
import os
import time

# all robot IPs go here. recommended to have a static IP per robot
#Example:
ip1='192.168.12.34'
ip2='192.168.56.78'



running=True

def StopBehavior(ip):
    bm = ALProxy("ALBehaviorManager",ip,9559)
    bm.stopAllBehaviors()

def StartBehavior(ip,behavior):
    bm = ALProxy("ALBehaviorManager",ip,9559)
    bm.startBehavior(behavior)

def PreloadBehavior(ip):
    bm = ALProxy("ALBehaviorManager",ip,9559)
#Format of name of project to access, replace all of [ApplicationID/BehaviorID]'s with the actual project
    bm.preloadBehavior('ApplicationID/BehaviorID')
#Example:
    bm.preloadBehavior('synctest-7caffc/behavior_1')


if __name__ == '__main__':
    #you must pre load the behaviors from the robot's drive to the memory. this will ensure super-fast load time.
    p1=Process(target=PreloadBehavior, args=(ip1,))
    p2=Process(target=PreloadBehavior, args=(ip2,))
    p1.start()
    p2.start()
     
    #below is the command prompt for the operation. there are 4 commands: say, stop, stand, sit and dance.
    
    while running:
        print(ip1)
        cmd=raw_input("Awaiting command: (say,behavior1,behavior2,quit) ")
        if cmd == "say":
            tts = ALProxy("ALTextToSpeech",ip1,9559)
            tts.say("hello from python")
        elif cmd=="stop":
            p1=Process(target=StopBehavior, args=(ip1,))
	    p2=Process(target=StopBehavior, args=(ip2,))
            p1.start()
	    p2.start()
            print("kk")
        elif cmd=="behavior1":
            p1=Process(target=StartBehavior, args=(ip1,'ApplicationID/BehaviorID'))
	    p2=Process(target=StartBehavior, args=(ip2,'ApplicationID/BehaviorID'))
            p1.start()
	    p2.start()
        elif cmd=="behavior2":
            p1=Process(target=StartBehavior, args=(ip1,'ApplicationID/BehaviorID'))
	    p2=Process(target=StartBehavior, args=(ip2,'ApplicationID/BehaviorID'))
            p1.start()
	    p2.start()
            time.sleep(2)
            #make sure the path is correct to the file on your local hard drive.
            os.startfile('C:\\Users\\alber\\Downloads\\caravanPalace_shanghai.wav')
            
        elif cmd == "quit":
	    p1=Process(target=StopBehavior, args=(ip1,))
	    p2=Process(target=StopBehavior, args=(ip2,))
            p1.start()
	    p2.start()
            running=False
        else:
            print ("\n**WRONG COMMAND**\n")
    else:
        print('quitting')
    