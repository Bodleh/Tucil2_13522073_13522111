def valid_int_input(msg: str, has_limit: bool = False, lower_limit: int = 0) -> int:
    while True:
        try:
            user_input = int(input(msg))
            if has_limit and user_input < lower_limit:
                raise ValueError
            return user_input
        except ValueError:
            if has_limit:
                print(f"\nInvalid input, input must be an integer greater or equal to {lower_limit}!\n")
            else:
                print("\nInvalid input, input must be an integer!\n")

