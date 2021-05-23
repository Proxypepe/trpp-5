from ctypes import CDLL, c_float

Converter = CDLL("./src_c/libconverter.so")

Converter.celsius_to_kelvin.restype = c_float
Converter.celsius_to_kelvin.argtypes = [c_float, ]

Converter.celsius_to_fahrenheit.restype = c_float
Converter.celsius_to_fahrenheit.argtypes = [c_float, ]

Converter.kelvin_to_fahrenheit.restype = c_float
Converter.kelvin_to_fahrenheit.argtypes = [c_float, ]

Converter.kelvin_to_celsius.restype = c_float
Converter.kelvin_to_celsius.argtypes = [c_float, ]

Converter.fahrenheit_to_kelvin.restype = c_float
Converter.fahrenheit_to_kelvin.argtypes = [c_float, ]

Converter.fahrenheit_to_celsius.restype = c_float
Converter.fahrenheit_to_celsius.argtypes = [c_float, ]


def convert(value: float, sys_from: str, sys_to: str):
    systems = {"c": "celsius", "k": "kelvin", "f": "fahrenheit"}
    functions = {
        "ck": Converter.celsius_to_kelvin,
        "cf": Converter.celsius_to_fahrenheit,
        "kf": Converter.kelvin_to_fahrenheit,
        "kc": Converter.kelvin_to_celsius,
        "fk": Converter.fahrenheit_to_kelvin,
        "fc": Converter.fahrenheit_to_celsius
    }
    if sys_from in systems and sys_to in systems:
        if sys_from == sys_to:
            return value
        return functions[f'{sys_from}{sys_to}'](value)
    else:
        return "Invalid system enter"
