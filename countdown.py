import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

def main():
    print("Countdown Timer")
    print("-" * 25)

    try:
        total_seconds = int(input("Enter time in seconds: "))
        if total_seconds <= 0:
            print("Please enter a positive number.")
            return
        countdown(total_seconds)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
