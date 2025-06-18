import time

my_time = int(input("Enter your time in seconds: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)
# hiermee duurt het 3 seconde voordat het pas wordt uitgevoerd
# time.sleep(3)

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time's up!")
