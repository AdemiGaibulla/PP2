from datetime import *

todaydate = datetime.now()

fivedays = timedelta(days=5)

result = todaydate - fivedays
print(result)