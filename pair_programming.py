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


## Kailey's feedback:
# Your use of docstrings was good, and you successfully defined your parameters and returns. You also did a good job of including examples of your function in use. Although you had a good description of your function, you could have included a shorter description at the very top of your docstring to match Python function documentation. You also could have made it a little more clear within your description that you were converting the sum of the two parameters (feet and inches) to a meter value, rather than each of them seperately. 

def test_ftandin_to_meters():
    # test 1
    assert ftandin_to_meters(0, 0) == 0
    # test 2
    assert ftandin_to_meters(3.28084, 0) == 1.000000032
    # test 3
    assert ftandin_to_meters(0, 1) == 0.0254
    
    print("All tests passed")

# run my function which asserts multiple tests for ftandin_to_meters(feet, inches)
test_ftandin_to_meters()
          