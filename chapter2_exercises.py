# Exercises for chapter 2:

# Name:Daniel Abrams

#Exercise 2.1 
#Python is seems to be using base 8 for all entries that begin with 0.
#This is backed up by the fact that the entry of any number greater than 7 after a 0 returns an error.
#This is also backed up by the fact that 010 is 8, 0100 is 64 and so on.

#Exercise 2.2
print 5
x = 5
print x+1
#prints 5 then prints 6
#we cannot print x = 5 because it is not an int. We can convert it to a string, but then it does not adjust the value of x.

#Exercise 2.3
# 1. (int) 8
# 2. (float) 8.5
# 3. (float) 4.0
# 4. (int) 11
# 5. (string) .....

#Exercise 2.4
# 1.
(4/3)*(3.1415926539)*(5^3)
# is equal to 18.8495559234

# 2.
bookCost = 24.95*(0.6)*60 
# Total Cost of books is 898.1999999999999
shippingCost = 3 + (59*.75)
#shipping costs equals 47.25
totalCost = bookCost + shippingCost
#Total Wholesale cost is 945.4499999999999

# 3.
easyPaceTime = (8*60)+15
# Easy Pace in seconds = 495
fastPaceTime = (7*60)+12
# Fast Pace in seconds = 432
totalTime = (easyPaceTime*2) + (3*fastPaceTime)
#total time is 2286
totalMinutes = totalTime/60
totalSeconds = totalTime -(totalMinutes*60)
#total Minutes is 38
#total Seconds is 6
#return home at 7:50:06
 


