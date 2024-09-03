def length_convert(value, from_unit, to_unit):

    conversions = {
        "meter": {
            "kilometer": value / 1000,
            "centimeter": value * 100,
            "millimeter": value * 1000,
            "micrometer": value * 1e6,
            "nanometer": value * 1e9,
        },
        "kilometer": {
            "meter": value * 1000,
            "centimeter": value * 100000,
            "millimeter": value * 1e6,
            "micrometer": value * 1e9,
            "nanometer": value * 1e12,
        },
        "centimeter": {
            "meter": value / 100,
            "kilometer": value / 100000,
            "millimeter": value * 10,
            "micrometer": value * 1e4,
            "nanometer": value * 1e7,
        },
        "millimeter": {
            "meter": value / 1000,
            "kilometer": value / 1e6,
            "centimeter": value / 10,
            "micrometer": value * 1000,
            "nanometer": value * 1e6,
        },
        "micrometer": {
            "meter": value / 1e6,
            "kilometer": value / 1e9,
            "centimeter": value / 1e4,
            "millimeter": value / 1000,
            "nanometer": value * 1000,
        },
        "nanometer": {
            "meter": value / 1e9,
            "kilometer": value / 1e12,
            "centimeter": value / 1e7,
            "millimeter": value / 1e6,
            "micrometer": value / 1000,
        },
    }

    if from_unit in conversions and to_unit in conversions[from_unit]:
        return conversions[from_unit][to_unit]
    else:
        return None


def temp_convert(value, from_unit, to_unit):
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9 / 5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5 / 9
        elif to_unit == "K":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return ((value - 275.15) * (9 / 5)) + 32


def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "square_meters": 1,
        "square_kilometers": 1e6,
        "square_centimeters": 1e-4,
        "square_millimeters": 1e-6,
        "acres": 4046.86,
        "hectares": 1e4,
        "square_yards": 0.836127,
        "square_feet": 0.092903,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")

    value_in_meters = value * conversion_factors[from_unit]

    value_in_target_unit = value_in_meters / conversion_factors[to_unit]

    return value_in_target_unit


def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": 1,
        "km/h": 1 / 3.6,
        "mph": 1 / 2.237,
        "ft/s": 0.3048,
        "knots": 0.514444,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")

    value_in_mps = value * conversion_factors[from_unit]

    value_in_target_unit = value_in_mps / conversion_factors[to_unit]

    return value_in_target_unit


def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400,
        "weeks": 604800,
        "months": 2628000,
        "years": 31536000,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")

    value_in_seconds = value * conversion_factors[from_unit]

    value_in_target_unit = value_in_seconds / conversion_factors[to_unit]

    return value_in_target_unit


def convert_mass(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 1000,
        "milligrams": 0.001,
        "micrograms": 1e-6,
        "pounds": 453.592,
        "ounces": 28.3495,
        "stones": 6350.29,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")

    value_in_grams = value * conversion_factors[from_unit]

    value_in_target_unit = value_in_grams / conversion_factors[to_unit]

    return value_in_target_unit


def convert_data(value, from_unit, to_unit):
    conversion_factors = {
        "bytes": 1,
        "kilobytes": 1024,
        "megabytes": 1024**2,
        "gigabytes": 1024**3,
        "terabytes": 1024**4,
        "petabytes": 1024**5,
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit")

    value_in_bytes = value * conversion_factors[from_unit]

    value_in_target_unit = value_in_bytes / conversion_factors[to_unit]

    return value_in_target_unit
