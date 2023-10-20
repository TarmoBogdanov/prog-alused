
def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum_result = num_a + num_b
    difference_result = num_a - num_b
    return sum_result, difference_result

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division_result = num_a / num_b
    return division_result

def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division_result = num_a // num_b
    return division_result

def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder

def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2
    return average

def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = 3.14159265 * radius ** 2
    return circle_area

def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = (side_length ** 2 * (3 ** 0.5)) / 4
    return int(triangle_area)

def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant

def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of the hypotenuse when the lengths of the catheti are given."""
    c = (a ** 2 + b ** 2) ** 0.5
    return c

def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of the cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = (c ** 2 - a ** 2) ** 0.5
    return b

def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} seconds is {hours} hour(s) and {minutes} minute(s)."

def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    import math
    sine = math.sin(math.radians(angle))
    cosine = math.cos(math.radians(angle))
    return f"Angle: {angle}, sine: {sine}, cosine: {cosine}."

def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey " * n
    return lots_of_heys.strip()

def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    result = num_a + num_b
    return str(result)