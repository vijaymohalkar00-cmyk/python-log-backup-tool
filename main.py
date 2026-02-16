from log_analyzer import analyze_log
from backup import take_backup

def menu():
    print("1. Analyze log file")
    print("2. Take folder backup")
    choice = input("Enter choice: ")

    if choice == "1":
        log_file = input("Enter log file path: ")
        errors, warnings = analyze_log(log_file)
        print("Errors:", errors)
        print("Warnings:", warnings)

    elif choice == "2":
        src = input("Enter folder to backup: ")
        dest = input("Enter backup folder: ")
        take_backup(src, dest)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()
