import time
import threading
from datetime import datetime

class CountdownTimer:
    def __init__(self):
        self.is_running = False
        self.timer_thread = None

    def start_countdown(self, duration_seconds):
        self.is_running = True
        start_time = time.time()
        end_time = start_time + duration_seconds

        while self.is_running and time.time() < end_time:
            remaining_time = int(end_time - time.time())
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print(f'\rTime remaining: {minutes:02d}:{seconds:02d}', end='')
            time.sleep(1)

        if self.is_running:
            print('\n🔔 Time is up! Countdown completed!')
            self.is_running = False

    def start(self, duration_seconds):
        if self.timer_thread and self.timer_thread.is_alive():
            print('A timer is already running!')
            return

        self.timer_thread = threading.Thread(target=self.start_countdown, args=(duration_seconds,))
        self.timer_thread.start()

    def stop(self):
        self.is_running = False
        if self.timer_thread:
            self.timer_thread.join()

def get_duration_input():
    while True:
        try:
            choice = input('Enter duration in (M)inutes or (S)econds? [M/S]: ').upper()
            if choice not in ['M', 'S']:
                print('Please enter M for minutes or S for seconds.')
                continue

            duration = float(input('Enter the duration: '))
            if duration <= 0:
                print('Please enter a positive number.')
                continue

            return duration * 60 if choice == 'M' else duration

        except ValueError:
            print('Please enter a valid number.')

def main():
    timer = CountdownTimer()
    print('Welcome to the Countdown Timer!')

    while True:
        print('\n1. Start a new timer')
        print('2. Stop current timer')
        print('3. Exit')
        
        choice = input('\nEnter your choice (1-3): ')

        if choice == '1':
            duration_seconds = get_duration_input()
            timer.start(duration_seconds)
        elif choice == '2':
            timer.stop()
            print('Timer stopped.')
        elif choice == '3':
            timer.stop()
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()