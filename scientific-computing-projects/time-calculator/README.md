# Time Calculator

Adds a duration to a start time and returns the new time. Handles time rollover, AM/PM, and days of the week.

## Features
- AM/PM time conversion
- Day of week calculation
- Human-readable output

## Usage
```python
add_time("3:00 PM", "3:10")  # Returns: '6:10 PM'
add_time("11:30 AM", "2:32", "Monday")  # Returns: '2:02 PM, Monday'
```

## Skills Demonstrated
- Time arithmetic
- Modular math
- Optional arguments
