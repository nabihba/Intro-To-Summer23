import random as r
days_of_the_week=["Sunday","Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday"]
temperatures=[]
above_avg=[]
avg=0
good_days_count=0
highest_temp=0
highest_temp_day=""
lowest_temp=1000
lowest_temp_day=""
for i in range(7):
	temperatures.append(r.randint(26,41))
	avg+=(temperatures[i])/7
	if temperatures[i]%2==0:
		good_days_count+=1
	if temperatures[i]>highest_temp:
		highest_temp=temperatures[i]
		highest_temp_day=days_of_the_week[i]
	if temperatures[i]<lowest_temp:
		lowest_temp=temperatures[i]
		lowest_temp_day=days_of_the_week[i]
for i in range(7):
	if temperatures[i]>avg:
		above_avg.append(temperatures[i])
print("The weather report:")
for i in range(7):
	print(days_of_the_week[i] + ": "+str(temperatures[i]))
print("shelly had "+str(good_days_count)+"good days")
print("the hottest temperature was: "+ str(highest_temp)+ " on "+highest_temp_day)
print("the lowest was: "+ str(lowest_temp)+" on "+ lowest_temp_day)
print("the average temperature was "+ str(avg))
print("the days that were above average: "+str(above_avg))