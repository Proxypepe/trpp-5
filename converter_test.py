import pytest

from converter import Converter

positive_arg = 10
zero = 0
negative_arg = -10
converter_test = 4242


@pytest.mark.parametrize('value, sys_from, sys_to, func',
                         [(converter_test, 'c', 'k', Converter.celsius_to_kelvin),
                          (converter_test, 'c', 'f', Converter.celsius_to_fahrenheit),
                          (converter_test, 'k', 'c', Converter.kelvin_to_celsius),
                          (converter_test, 'k', 'f', Converter.kelvin_to_fahrenheit),
                          (converter_test, 'f', 'k', Converter.fahrenheit_to_kelvin),
                          (converter_test, 'f', 'c', Converter.fahrenheit_to_celsius),
                          (converter_test, 'f', 'f', lambda value: value),
                          (converter_test, 'd', 'c', lambda x: "Invalid system enter"),
                          ])
def test_converter(value, sys_from, sys_to, func):
    assert Converter.convert(value, sys_from, sys_to) == func(value)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_celsius_to_kelvin(value):
    assert round(Converter.celsius_to_kelvin(value), 2) == round(value + 273.15, 2)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_celsius_to_fahrenheit(value):
    assert round(Converter.celsius_to_fahrenheit(value), 2) == round((value * 9/5) + 32.0, 2)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_kelvin_to_fahrenheit(value):
    assert round(Converter.kelvin_to_fahrenheit(value), 2) == round((value - 273.15) * 9/5 + 32.0, 2)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_kelvin_to_celsius(value):
    assert round(Converter.kelvin_to_celsius(value), 2) == round(value - 273.15, 2)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_fahrenheit_to_kelvin(value):
    assert round(Converter.fahrenheit_to_kelvin(value), 2) == round((value - 32.0) * 5/9 + 273.15, 2)


@pytest.mark.parametrize('value', [positive_arg, zero, negative_arg])
def test_fahrenheit_to_celsius(value):
    assert round(Converter.fahrenheit_to_celsius(value), 2) == round((value - 32.0) * 5/9, 2)


# Fixed section


def test_celsius_to_kelvin_fixed():
    assert Converter.celsius_to_kelvin(225) == 498.15


def test_celsius_to_fahrenheit_fixed():
    assert Converter.celsius_to_fahrenheit(134) == 273.2


def test_kelvin_to_fahrenheit_fixed():
    assert Converter.kelvin_to_fahrenheit(-6913) == -12903.07


def test_kelvin_to_celsius_fixed():
    assert Converter.kelvin_to_celsius(3322) == 3048.85


def test_fahrenheit_to_kelvin_fixed():
    assert round(Converter.fahrenheit_to_kelvin(588), 3) == 582.039


def test_fahrenheit_to_celsius_fixed():
    assert Converter.fahrenheit_to_celsius(2264) == 1240

