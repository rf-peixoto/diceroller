import os
import sys
import platform
from random import randint
from datetime import datetime
# --------------------------------------------------------- #
# Check OS:
# --------------------------------------------------------- #
op_sys = platform.system()
if op_sys == "Linux":
    clean_command = "clear"
else:
    clean_command = "cls"
# --------------------------------------------------------- #
# Initialize
# --------------------------------------------------------- #
banner = """# =========================================== #
  ___   _           ___       _  _
 |   \ (_) __  ___ | _ \ ___ | || | ___  _ _
 | |) || |/ _|/ -_)|   // _ \| || |/ -_)| '_|
 |___/ |_|\__|\___||_|_\\\___/|_||_|\___||_|
# =========================================== #"""
os.system(clean_command)
print(banner)
# --------------------------------------------------------- #
# Functions
# --------------------------------------------------------- #
def get_time():
    time = datetime.now()
    return "[{1}/{0}/{2} {3}:{4}]".format(time.day, time.month, time.year, time.hour, time.minute)

def quit():
    input("Thank you, press anything to quit.")
    os.system(clean_command)
    sys.exit()

def save_log(start, end):
    header = "Session Start:\t{0}\n".format(start)
    end = "\nSession End:\t{0}\n".format(end)
    #filename = "{0}_{1}.txt".format(name, get_time().replace(" ", "_"))
    filename = "session_log.txt" # Debug
    with open(filename, "w") as fl:
        fl.write(header + "\n")
        for i in log:
            fl.write(i)
        fl.write(end)
# --------------------------------------------------------- #
# Menu
# --------------------------------------------------------- #
print("Welcome to DiceRoller. Start session? [y/anything to quit]")
start_time = get_time()
start = input(">>> ").lower()
if start != "y":
    quit()
# --------------------------------------------------------- #
# Rolling Loop
# --------------------------------------------------------- #
name = input("Character name: ")
started_at = get_time()
log = []
# Roll:
while True:
    roll = input("[{0}]: ".format(name))
    if roll.lower() == "q":
        break
    number_of_dices = int(roll.split("d")[0]) + 1 
    result = []
    for n in range(1, number_of_dices):
        if roll.endswith("h"):
            dice = int(roll.split("d")[-1].replace("h", ""))
            dice_res = randint(1, dice)
            while dice_res < dice * 0.5:
                dice_res = randint(1, dice)
            result.append(dice_res)
        else:
            dice = int(roll.split("d")[-1])
            result.append(randint(1, dice))
    tmpstr = ""
    for i in result:
        tmpstr += "{0} + ".format(i)
    print(tmpstr[:-2] + "= {0}".format(sum(result)))
    log.append("{0}\t[{1}]\t{2}\t{3}\n".format(get_time(), name, roll, str(tmpstr[:-2] + "= {0}".format(sum(result)))))
# --------------------------------------------------------- #
# End
# --------------------------------------------------------- #
print("Closing session.")
end = get_time()
opt = input("Done. Save log? [y/anything to quit]\n>>> ").lower()
if opt != "y":
    quit()
else:
    save_log(start_time, end)
    quit()
