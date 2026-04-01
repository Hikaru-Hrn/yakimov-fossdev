def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def tax_calculator_bugged(income):
    if income < 0:
        raise ValueError("Could not agree negative count")
    return int(income * 0.15 * 100) / 100
