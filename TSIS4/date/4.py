from datetime import *

today = datetime.now()
tomorrow = today + timedelta(days=1)

difference = tomorrow - today

print(difference.total_seconds())