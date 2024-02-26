def ftandin_to_meters(feet, inches):
    """
    Description
    ___________
    Function that converts two values, feet and inches to its equivilent value in meters. 
    
    Inputs
    __________
    feet: float or int
        Lenght in feet.
    inches: float or int
        Length in inches.
    Returns
    _________
    float
        Equivilent length in meters.
    
    Examples
    _________
    ftandin_to_meters(6, 0)
    1.8288
    
    """
    # converts feet to inches and sums
    total_inches = feet * 12 + inches
    # converts total inches to meters
    meters = total_inches * 0.0254 
    
    return meters

