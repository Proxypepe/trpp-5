float celsius_to_kelvin(float value)
{
    return value + 273.15;
}

float celsius_to_fahrenheit(float value)
{
    return (value * 9/5) + 32.0;
}

float kelvin_to_fahrenheit(float value)
{
    return (value - 273.15) * 9/5 + 32.0;
}
float kelvin_to_celsius(float value)
{
    return value - 273.15;
}

float fahrenheit_to_kelvin(float value)
{
    return (value - 32.0) * 5/9 + 273.15;
}

float fahrenheit_to_celsius(float value)
{
        return (value - 32.0) * 5/9;
}
