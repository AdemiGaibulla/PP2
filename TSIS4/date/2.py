from datetime import *

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)