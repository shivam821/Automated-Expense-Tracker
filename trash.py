# from random import randint

# uuid = randint(10000, 99999)
# print(uuid)

from datetime import datetime
created_at = datetime.now()
print(created_at)

from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

print("Date and time is:", dt)
print("Timestamp is:", ts)