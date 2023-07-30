import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining: {seconds // 60:02d}:{seconds % 60:02d}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up! Stay focused!")

if __name__ == "__main__":
    print("Welcome to the Focus Timer!")
    try:
        minutes = int(input("Enter the duration in minutes: "))
        focus_timer(minutes)
    except ValueError:
        print("Invalid input. Please enter a valid integer for minutes.")
