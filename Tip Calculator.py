#Tip calulator

# Problem 
''' Calculate the total Bill and the split it amongs the friends with tip added ''' 
# Solution   

#welcome message
print("*** Welcome to Tip calculater! *** \n") #welcome message

#Asking user for bill amount and coverting it to float
bill=(input("What was the total bill?\n Bill: $"))
bill_amount =(float(bill))

#Asking user the bill percent and calcuting the tip amount
percentage = input("What percentage of Bill you would like to give as Tip? 10, 12, or 15?\n ==> ")
percent_int =int(percentage)
percent = 1 + (percent_int/100)
print()
#Asking user in man people will divide the bill 
No_of_people = input("How many people you want to divdided bill into?\n ==> ")
print()
num_ppl = int(No_of_people)
cal = ((bill_amount/num_ppl)*percent)
Total = round(cal,2)

#Printing final amount to be paid by each person 
print(f"Each person should pay ${Total}")

print()
print("*** Thank You ***")
