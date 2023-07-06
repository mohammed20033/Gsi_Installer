import os, time

os.system("cls")
print("""
 ▄▄▄▄▄ ▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄
█─▄▄▄▄█▄─▄▄─█▄─█─▄█▄─▄▄─█▄─▀█▄─▄█
█▄▄▄▄─██─▄█▀██▄▀▄███─▄█▀██─█▄▀─██
▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀
""")
print("GSI INSTALLER FOR SELENE")
print("")
print("By seveN")

print()
input("Go in normal fastboot and press enter ...")

print()
#boot = input("Are u want to flash boot.img ? y/n ==> ")

#if an == "y":
#    boot = input("Drage boot.img ==> ")
#    print()
#    print("Flashing boot...")
#    print()
#    os.system("fastboot flash boot " + boot)
#    print ()
#    print("Done")
#elif an == "n":
#    print("Skipping...")
#else:
#    print("Invalid input!")

print()
Gsi = input("Drage Gsi file here and press enter ==> ")
print ()
VB = input("okay now drage vbmeta file here and press enter ==> ")

os.system("cls")
print("""

█ █▄░█ █▀ ▀█▀ ▄▀█ █░░ █░░ █ █▄░█ █▀▀
█ █░▀█ ▄█ ░█░ █▀█ █▄▄ █▄▄ █ █░▀█ █▄█
""")
print()
print ("Now set back and Get coffe every
       thing is automated")
time.sleep(2)
print()
print("Disableing VBmeta")
print()
os.system("fastboot --disable-verity --disable-verification flash vbmeta " + VB)
print()
print ("Done")
print("-----------------------------------------------------------")

print()
print("Going to fastbootD ...")
print()
os.system("fastboot reboot fastboot")
print()
print ("Done")
print("-----------------------------------------------------------")

print()
print("Erasing userdata ...")
print()
os.system("fastboot erase userdata")
print()
print ("Done ")
print("-----------------------------------------------------------")

print()
print("Erasing system ...")
print()
os.system("fastboot erase system")
print()
print ("Done ")
print("-----------------------------------------------------------")

print()
print("Flashing gsi img to slot A...")
print()
os.system("fastboot flash system_a " + Gsi)


print()
print ("Done ")
print("-----------------------------------------------------------")
print()
input(" Hold vol + key and press enter to continu after going to recovery do wipe data then restart")
os.system("fastboot reboot")
print("-----------------------------------------------------------")
print()
print ("Bakaaa byeee <3 ...")
print()

input("press enter to exit")
exit()
