# Latex Timetable
## Setup
- I use pdfTeX, Version 3.14 but chances are it works with and latex version

## How It Works
1. **Dynamic Day and Time Slot Generation:**  
   The `Timetable` environment (defined in `timetable.tex`) takes parameters that indicate the type and sequence of days. It then:
   - Calculates the number of IPA (work) days versus rest days.
   - Creates headers for each day.
   - Generates time slots using a loop structure defined in LaTeX3 (see `tex3.tex`).

2. **Task Scheduling:**  
   The `\task` macro allows users to define tasks with a name, planned hours, and completed hours. This macro inserts the task into the timetable, using helper commands to fill in the corresponding time slots.

## Customization
- **Adjusting Time Blocks:**  
  Change `\blockSize`, `\hoursPerDay`, or `\minutesPerHour` in `vars.tex` to modify the granularity of your timetable.
  