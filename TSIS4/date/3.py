from datetime import *

today = datetime.now()
today = today.replace(microsecond=0)

print(today)