import datetime

print(f"microsecond: {datetime.datetime.now().microsecond}")
print(f"second: {datetime.datetime.now().second}")
print(f"minute: {datetime.datetime.now().minute}")
print(f"hour: {datetime.datetime.now().hour}")
print(f"day: {datetime.datetime.now().day}")
print(f"month: {datetime.datetime.now().month}")
print(f"year: {datetime.datetime.now().year}")
print(f"dst: {datetime.datetime.now().dst()}")
print(f"date: {datetime.datetime.now().date()}")
print(f"weekday: {datetime.datetime.now().weekday()}")
print(f"time: {datetime.datetime.now().time()}")
print(f"utcnow: {datetime.datetime.now().utcnow()}")
print("-" * 100)
print(f"now: {datetime.datetime.now()}")
print(datetime.datetime.now().strftime("%m %d %Y %H:%M"))



