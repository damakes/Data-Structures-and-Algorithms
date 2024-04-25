def check_balance(text):
    # Your code here
    """
    Checks the balance of brackets in a given text.

    Parameters: text : checked for balanced brackets.

    Returns: whether the brackets are balanced or an error position if imbalance is detected.
    """
    # track opening brackets
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}
    # Iterate over characters
    for index, char in enumerate(text):
        # open brackets
        if char in brackets_map.values():
            stack.append(char)

        # closed brackets
        elif char in brackets_map.keys():
            if not stack or stack[-1] != brackets_map[char]:
                return f'Match error at position {index}'
            stack.pop()

    # Check for remaining brackets
    if stack:
        return f'Match error at position {index}'
    else:
        return f'Ok - {text.count("(") + text.count("[") + text.count("{")}'



# TESTS
def test_check_balance():
    tests = [
        ("a(b)c[d]e{f}g", 'Ok - 3'),
        ('a(b)c[)d]e{f}g', 'Match error at position 6'),
        ('a(b)(((c[d]e{f}g)))', 'Ok - 6'),
        ('a(b)c(([d][e{f}])g)', 'Ok - 6'),
        ('a(b)c(([d][e{f}])g)(', 'Match error at position 19'),
        (']a(b)c(([d][e{f}])g)', 'Match error at position 0'),
        ('', 'Ok - 0'),
        ('abc', 'Ok - 0')
    ]

    for i, (input_text, expected_output) in enumerate(tests, start=1):
        result = check_balance(input_text)
        if result != expected_output:
            print(f"Test {i} failed. Expected: '{expected_output}', but got: '{result}'")
            return

    print("All tests passed successfully.")

test_check_balance()
