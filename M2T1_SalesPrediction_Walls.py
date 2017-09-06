# CTI-110
# M2T1 - Sales Prediction
# Dominik Sian Walls
# 8/30
#

# This program will allow a company who's annual profit is typically
# 23 percent of total sales calculate their annual profit based on
# the company's current total sales.

# Asks the user to input a number for Total Sales
totalSales = int(input("Type the number of Total Sales: "))

# Calculates the annual profit based off of user's totalSales input
annualProfit = 0.23 * totalSales

# Prints the annual profit amount
print("The Annual Profit is", annualProfit)
