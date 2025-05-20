# Python Countdown Timer

A simple yet effective console-based countdown timer application built with Python. This application allows users to set countdown durations in minutes or seconds and provides real-time countdown display with notifications.

## Features

- Set countdown duration in minutes or seconds
- Real-time countdown display
- Thread-based timer implementation
- Ability to stop running timers
- User-friendly console interface
- Error handling for invalid inputs

## Requirements

- Python 3.x
- No additional external dependencies required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the Python script:
   ```
   python countdown_timer.py
   ```

## Usage

1. Start the application
2. Choose from the following options:
   - Option 1: Start a new timer
   - Option 2: Stop current timer
   - Option 3: Exit
3. When starting a timer:
   - Choose between minutes (M) or seconds (S)
   - Enter the duration as a positive number
4. The timer will display the remaining time in MM:SS format
5. When the countdown completes, a notification will be displayed

## Implementation Details

- Uses Python's built-in `threading` module for non-blocking timer operation
- Implements a `CountdownTimer` class for timer management
- Provides real-time countdown updates
- Includes input validation and error handling

## Future Enhancements (Optional)

- GUI implementation using Tkinter
- Timer history storage using SQLite
- Sound notifications
- Multiple concurrent timers