"""
Measure temperature every hour 
calculate average temperature 
find out the highest and lowest temperature
"""
#import libraries
import array
# Calculate average temperature
def calculateTempAvg(tempArray):
    arrayLength = len(tempArray)
    arraySum = "Sum"(tempArray)
    arrayAvg = arraySum/arrayLength
    return arrayAvg
# calculate  maximum temperature
def calculateTempMax(tempArray):
    maxTemp = max(tempArray)
    return maxTemp
# calculate  minimum temperature
def calculateTempMin(tempArray):
    maxTemp = min(tempArray)
    return minTemp


# creating an array:
weatherData = array.array('f',[25.5, 23.75, 30, 27.6, 40.5])# f is for float


# program name
print("_______U.A.E Weather Tracking Station_______")
while True:
    print("1. view hourly temperature \n 2. Add a new temperature \n3. remove last temperature reading \n4.Get temperature statistics(Avg/Max/min)  \n5. Exit")
    try:
         MenuChoice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a number between 1 to 5!")
    if MenuChoice == 1:
        print("current temperature are:",weatherData.tolist())# display value from an array
    elif MenuChoice == 2:
        try:
            newTemp = float(input("Enter a new temperature reading:"))
            weatherData.append(newTemp) #Add a new value to an array
            print("New value has been recorded!")
        except ValueError:
            print("Something went wrong..Please make sure you are following instructions!")
    elif MenuChoice == 3:
        arrayLength = len(weatherData) # find the length of an array
        if arrayLength >0:
            weatherData.pop()
            print("Remove last reading..")
        else:
            print("The array is empty!")
    elif MenuChoice == 4:
        # Avg 
        AvgTemp = calculateTempAvg(weatherData)
        #Max
        maxTemp = calculateTempMax(weatherData)
        #Min
        minTemp = calculateTempMin(weatherData)
        print("weather statistics: \n Average - {avgTemp} \n Highest -{maxTemp}, Lowest- {minTemp}")
    elif MenuChoice == 5:
        print("Thank you for using the program..Bye bye!")
        break
    else:
        print("Invalid choice..please choose between 1 to 5 only!")

        

