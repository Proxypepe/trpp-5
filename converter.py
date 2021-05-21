class Converter:
    @staticmethod
    def convert(value:float, sys_from: str, sys_to: str):
        systems = {"c": "celsius", "k": "kelvin", "f": "fahrenheit"}
        if sys_from in systems and sys_to in systems:
            if sys_from == sys_to:
                return value
            return getattr(Converter, f"{systems[sys_from]}_to_{systems[sys_to]}")(value)
        else:
            return "Invalid system enter"

    @staticmethod
    def celsius_to_kelvin(value: float):
        return value + 273.15

    @staticmethod
    def celsius_to_fahrenheit(value: float):
        return (value * 9/5) + 32.0

    @staticmethod
    def kelvin_to_fahrenheit(value: float):
        return (value - 273.15) * 9/5 + 32

    @staticmethod
    def kelvin_to_celsius(value: float):
        return value - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(value: float):
        return (value - 32.0) * 5/9 + 273.15

    @staticmethod
    def fahrenheit_to_celsius(value: float):
        return (value - 32.0) * 5/9
