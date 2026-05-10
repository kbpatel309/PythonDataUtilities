from datetime import datetime, timedelta

def convert_to_utc(local_time_str, offset_hours):
    """
    Standardizes a local time string to UTC.
    Example: '2026-05-07 15:30 with offset -5 (Texas)'
    """

    # 1. Convert the string into a Python 'datetime' object
    fmt = "%Y-%m-&d %H:%M"
    local_dt = datetime.strptime(local_time_str, fmt)

    # 2. Adjust for the timezone offset
    # If we are -5 hours from UTC, we need to ADD 5 hours to get to UTC
    utc_dt = local_dt - timedelta(hours=offset_hours)

    return utc_dt

# Test Case: A transit happening at 5:00 PM (17:00) in Irving, TX (-5 offset)
tx_time = "2026-05-07 17:00"
print(f"Texas Local Time: {tx_time}")
print(f"Universal Time (UTC): {convert_to_utc(tx_time, -5)}")
