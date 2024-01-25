def get_days_later(days):
  """
  Get a human-readable string indicating the number of days in the future.

  Args:
      days (int): The number of days in the future.

  Returns:
      str: A string describing the number of days, such as "(next day)" or "(X days later)", or an empty string if days is 0 or negative.
  """
  if days == 1:
      return "(next day)"
  elif days > 1:
      return f"({days} days later)"
  return ""


def add_time(start_time, end_time, day=None):
  # Constants for time calculations
  ONE_DAY_HOURS = 24
  HALF_DAY_HOURS = 12
  WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # Initialize the variable to track the number of days to add
  days_later = 0

  # Split the input times into components (hours, minutes, and period)
  hours, mins = start_time.split(":")
  mins, period = mins.split(" ")
  end_time_hours, end_time_mins = end_time.split(":")

  # Convert the components to integers
  hours = int(hours)
  mins = int(mins)
  end_time_hours = int(end_time_hours)
  end_time_mins = int(end_time_mins)

  # Calculate the total hours and minutes
  total_hours = hours + end_time_hours
  total_mins = mins + end_time_mins

  # Adjust for the case when total minutes exceed 60
  if total_mins >= 60:
      total_hours += int(total_mins / 60)
      total_mins %= 60

  # Handle cases involving AM and PM, and calculate days to add
  if end_time_hours or end_time_mins:
      if period == "pm" and total_hours > HALF_DAY_HOURS:
          if total_hours % ONE_DAY_HOURS >= 1.0:
              days_later += 1

      if total_hours >= HALF_DAY_HOURS:
          hours_left = total_hours / ONE_DAY_HOURS
          days_later += int(hours_left)

      temp_hours = total_hours

      # Handle AM/PM switching for the remaining hours
      while True:
          if temp_hours < HALF_DAY_HOURS:
              break
          if period == "am":
              period = "pm"
          else:
              period = "am"

          temp_hours -= HALF_DAY_HOURS

  # Calculate the remaining hours and minutes
  remaining_hours = int(total_hours % HALF_DAY_HOURS) or hours + 1
  remaining_mins = int(total_mins % 60)

  # Generate the time string in the format "HH:MM AM/PM"
  results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"

  # Check if a day of the week is provided
  if day:
      # Normalize and lowercase the input day
      day = day.strip().lower()
      # Calculate the adjusted day of the week
      selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
      current_day = WEEK_DAYS[selected_day]
      # Append the adjusted day and the number of days later
      results += f", {current_day.title()} {get_days_later(days_later)}"
  else:
      # If no day is provided, add an empty day string and the number of days later
      results += f" {get_days_later(days_later)}"

  # Return the formatted result string with leading and trailing whitespace stripped
  return results.strip()
