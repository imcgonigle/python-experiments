import threading
import time
import subprocess

def schedule_task(command, run_at):
    def task():
        sleep_time = run_at - time.time()

        if sleep_time > 0:
            time.sleep(sleep_time)

        print(f"\nRunning command: {command}")

        subprocess.run(command, shell=True)
    threading.Thread(target=task).start()

def main():
    tasks = []
    while True:
        print("\nTask Scheduler")
        print("1. Schedule Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            command = input("Enter command to run: ")
            time_str = input("Enter time to run (HH:MM 24-hour format): ")
            run_time_struct = time.strptime(time_str, "%H:%M")
            print(run_time_struct)
            current_time = time.localtime()
            
            run_at = time.mktime((
                current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                run_time_struct.tm_hour, run_time_struct.tm_min, 0, 0, 0, -1
            ))
            if run_at < time.time():
                run_at += 86400
            schedule_task(command, run_at)
            tasks.append((command, time_str))
            print("Task scheduled.")
        elif choice == '2':
            print("\nSchedul Tasks:")
            for command, time_str in tasks:
                print(f"{command} at {time_str}")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

