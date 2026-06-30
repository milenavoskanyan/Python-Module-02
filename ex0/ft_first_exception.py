def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        input_temperature('25')
        print("Temperature is now 25°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    try:
        print("Input data is 'abc'")
        input_temperature('abc')
        print("Temperature is now abc°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()

    test_temperature()
