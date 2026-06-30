def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        input_temperature('25')
        print("Temperature is now 25°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()

    try:
        print("Input data is 'abc'")
        input_temperature('abc')
        print("Temperature is now abc°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()

    try:
        print("Input data is '100'")
        input_temperature('100')
        print("Temperature is now 100°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()

    try:
        print("Input data is '-50'")
        input_temperature('-50')
        print("Temperature is now -50°C")
        print()
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()

    test_temperature()
