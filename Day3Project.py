#  A Simple Earnings Calculator

name = input("Whats ur name : ").strip().title()
hourlyWage = input("Whats ur hourly wage : ")
hourWork = input("How many hour u work this week : ")



# total earning for week (in dollars)
totalEarning = (int(hourlyWage) * int(hourWork))

print(f"{name} earned ${totalEarning} this week.")
