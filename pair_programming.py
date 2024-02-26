def ftandin_to_meters(feet, inches):
    """
    Description
    ___________
    Function that converts two values, feet and inches to meters
    
    Inputs
    __________
    feet (float): Length in feet
    inches (float): Length in inches
    
    Returns
    _________
    float : equivilent length in meters
    
    """
    total_inches = feet * 12 + inches # converts feet to inches and sums
    meters = total_inches * 0.0254 # converts total inches to meters
    return meters

# user input
feet = float(input("Enter feet: ")) 
inches = float(input("Enter inches: "))

# conversion
meters = ftandin_to_meters(feet, inches)

# display results
print(f"{feet} feet and {inches} inches is equal to {meters: .2f} meters.")