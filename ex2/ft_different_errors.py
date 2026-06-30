def garden_operations(operation_number: int) -> None:
    match operation_number:
        case t if t == 0:
            int('abc')
        case t if t == 1:
            3/0
        case t if t == 2:
            open("/non/existent/file", "r")
        case t if t == 3:
            'abc' + 3  # type: ignore


def test_error_types() -> None:
    for op in [0, 1, 2, 3]:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print()
    test_error_types()
