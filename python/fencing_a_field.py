#Question: Calculate the area, perimiter and total cost of fencing a field
#Inputs length and width
length = int(input("What is the length of your field? "))
width = int(input("What is the width of your field? "))

#Calculates the area and perimiter
area = length * width
perimiter = (length*2)+(width*2)

#Calculates the cost of the fencing
cost = 3.5 * perimiter

#Converts these variables into strings
cost = str(cost)
area = str(area)
perimiter = str(perimiter)

#Outputs the area, perimiter and cost of the fencing
print("The area and perimiter of your field is " + area + "m², " + perimiter + "m" +
      "\nThe total cost of your field is £"+cost)