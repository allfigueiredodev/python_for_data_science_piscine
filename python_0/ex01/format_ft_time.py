from datetime import datetime

epoch_time = datetime.now().timestamp()

formatted_time = f"{epoch_time:,.4f}"
scientific_time = f"{epoch_time:.2e}"
now = datetime.now()

print(f"Seconds since January 1, 1970: {formatted_time} or {scientific_time} in scientific notation")
print(f"{now.strftime("%b %d %Y")}")
