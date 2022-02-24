# a healthy programmer
"""we have to make functions for eye , exercise , and drink water"""
# import time
# from datetime import datetime
# def eye():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def exercise():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def water():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# if _name_ == "__main__":
#     log = 20
#     inp = input("enter your name : ")
#     inp1 = input(f"ok {inp} , let's create some files , enter the name for exercise file : ")
#     f = open(f"{inp1}","x")
#     f.write("this is a file for exercise only.")
#     f.close()
#     inp2 = input("enter the name for eye exercise file : ")
#     f = open(f"{inp2}","x")
#     f.write("this is a file for eye exercise only.")
#     f.close()
#     inp3 = input("enter the name for the water drinking : ")
#     f = open(f"{inp3}","x")
#     f.write("this is a file for drinking water.")
#     while(log>1):
#         time.sleep(5)
#         eye()
#         inp4 = input("time to do eye exercise , enter 'ey done' to stop the alarm : ")
#         if inp4=="ey done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp2}","w")
#             f.write(f"{inp} has done the eye exercise at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")
#         time.sleep(5)
#         exercise()
#         inp5 = input("time to do physical exercise , enter 'ex done' to stop the alarm : ")
#         if inp5=="ex done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp1}","w")
#             f.write(f"{inp} has done physical exercise at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")
#         time.sleep(5)
#         exercise()
#         inp6 = input("time to drink water , enter 'dw done' to stop the alarm : ")
#         if inp6=="dw done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp3}","w")
#             f.write(f"{inp} has dranked water at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")# a healthy programmer
# """we have to make functions for eye , exercise , and drink water"""
# import time
# from datetime import datetime
# def eye():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def exercise():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def water():
#     from pygame import mixer
#     mixer.init()
#     mixer.music.load("ultrainstinct.mp3")
#     mixer.music.play()
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# if _name_ == "__main__":
#     log = 20
#     inp = input("enter your name : ")
#     inp1 = input(f"ok {inp} , let's create some files , enter the name for exercise file : ")
#     f = open(f"{inp1}","x")
#     f.write("this is a file for exercise only.")
#     f.close()
#     inp2 = input("enter the name for eye exercise file : ")
#     f = open(f"{inp2}","x")
#     f.write("this is a file for eye exercise only.")
#     f.close()
#     inp3 = input("enter the name for the water drinking : ")
#     f = open(f"{inp3}","x")
#     f.write("this is a file for drinking water.")
#     while(log>1):
#         time.sleep(5)
#         eye()
#         inp4 = input("time to do eye exercise , enter 'ey done' to stop the alarm : ")
#         if inp4=="ey done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp2}","w")
#             f.write(f"{inp} has done the eye exercise at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")
#         time.sleep(5)
#         exercise()
#         inp5 = input("time to do physical exercise , enter 'ex done' to stop the alarm : ")
#         if inp5=="ex done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp1}","w")
#             f.write(f"{inp} has done physical exercise at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")
#         time.sleep(5)
#         exercise()
#         inp6 = input("time to drink water , enter 'dw done' to stop the alarm : ")
#         if inp6=="dw done":
#             from pygame import mixer
#             mixer.init()
#             mixer.music.load("ultrainstinct.mp3")
#             mixer.music.stop()
#             f = open(f"{inp3}","w")
#             f.write(f"{inp} has dranked water at {getdate()}")
#             f.close()
#             log = log-1
#         else:
#             print(" enter a valid input! after 5 seconds. ")
#



# Method-2:
# import time
# from pygame import mixer
# #Initalising the programme''''
# Name = input("Please enter your name ")
# print(f"{Name.capitalize()}, Welcome to office")
# file = Name
# _file= open(file,'a')
#
# StartTime = '09:00:00'
# FinishTime = '17:00:00'
#
# def playmusic(file):
#     file = 'Car Siren.mp3'
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#
# def TimeNow (CurrentTime):
#     if CurrentTime>StartTime and CurrentTime<FinishTime:
#         #print (currentTime=time.strftime('%H:%M:%S'))
#         return True
#     else:
#         return False
#
# currentTime=time.strftime('%H:%M:%S')
# #print(currentTime=time.strftime('%H:%M:%S'))
# #Setting up the parameters'''''
#
# DrinkWater = 2
# ActiveMan = 2
# ActiveEyes = 2
# ActualDrinkWater = 0
# ActualActiveMan= 0
# ActualActiveEyes = 0
# LastDrinkWater =1586941200
# LastActiveMan = 1586941200
# LastActiveEyes = 1586941200
# AlarmDrinkWater = 2 #After 900 Secs or 15 Mins but reduced to allow for quick execution and testing
# AlarmActiveMan = 3 #After Every 45 Mins but reduced to allow for quick execution and testing
# AlarmActiveEyes = 4 #After Every 15 Mins but reduced to allow for quick execution and testing
#
# while(True):
#     if DrinkWater> 0:
#         #print(f"Total water {DrinkWater}, remainwater {ActualDrinkWater}")
#         if((time.time()-LastDrinkWater) > AlarmDrinkWater):
#             playmusic(file)
#             print ("Time to Drink Water and Play music")
#             if (input("Water Drank = " ).lower()=="done"):
#                  LastDrinkWater=time.time()
#                  updatedTime = currentTime
#                  ActualDrinkWater = ActualDrinkWater+1
#                  DrinkWater= DrinkWater-1
#             _file.write(f"{currentTime}-you have had {ActualDrinkWater} glass of water.\n")
#
#     if ActiveEyes>0:
#         if((time.time()-LastActiveEyes)>AlarmActiveEyes):
#             playmusic(file)
#             print ("Time to Exercise Eyes and Play music")
#             if (input("Did you exercise your eyes = " ).lower()=="done"):
#                 LastActiveEyes=time.time()
#                 ActualActiveEyes = ActualActiveEyes+1
#                 ActiveEyes = ActiveEyes-1
#             _file.write(f"{currentTime}-Last Eye exercise done.\n " )
#
#
#     if ActiveMan >0:
#         if((time.time()-LastActiveMan)>ActualActiveMan):
#             playmusic(file)
#             print ("Time to move from your desk and Play music")
#             if (input("Did you move around = " ).lower()=="done"):
#                 LastActiveMan=time.time()
#                 ActiveMan-=1
#             _file.write(f"{currentTime}-Last desk Exercise done.\n"  )
#     else:
#         break
# _file.close()



# Method-3:
# import time
# import pygame
# import datetime
#
# freq = 1000    # audio CD quality
# bitsize = -16   # unsigned 16 bit
# channels = 2    # 1 is mono, 2 is stereo
# buffer = 1024
# pygame.mixer.init(freq,bitsize,channels,buffer)
# pygame.mixer.music.set_volume(10)
# def playsound(music):
#     pygame.init()
#     pygame.mixer.music.load(music)
#     pygame.mixer.music.play(5)
#
#     clock = pygame.time.Clock()
#     while pygame.mixer.music.get_busy():
#         # print "Playing..."
#         pygame.mixer.music.play(5)
#         # print("playing...........")
#         pygame.mixer.music.rewind()
#         clock.tick(1000)
#
# watertime=0
# eyestime=0
# physicletime=0
# while True:
#     with open("helthyprogram.txt",'a') as f:
#         time.sleep(1)
#         watertime+=1
#         eyestime+=1
#         physicletime+=1
#         if(watertime==20*60):
#             playsound("water.mp3")
#             if input("Are you drinking water :")=='done':
#                 f.write(datetime.datetime.now(),"you drank water at \n")
#                 pygame.mixer.music.stop()
#             watertime=0
#         elif(eyestime==30*60):
#             playsound('eyes.mp3')
#             if input("Are you drinking water :")=='done':
#                 f.write(datetime.datetime.now(),"eyes excersice \n")
#
#                 pygame.mixer.music.stop()
#
#             eyestime=0
#         elif physicletime==45*60:
#             playsound("physical.mp3")
#             if input("Are you drinking water :")=='done':
#                 f.write(datetime.datetime.now(),"physical excersice \n")
#
#                 pygame.mixer.music.stop()
#             physicletime=0
#
            