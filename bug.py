def function_with_uncommon_bug(data):
    # Simulate accessing a dictionary key that may not exist
    try:
        value = data['missing_key']
    except KeyError:
        # This is the part where the bug might occur.
        # If this function is used extensively,
        # the exception handling might not be sufficient.
        # consider using the get method instead to avoid such exceptions
        return None
    return value * 2

# Example usage that might lead to unexpected behavior:
my_data = {'key1': 10, 'key2': 20}
result = function_with_uncommon_bug(my_data)
print(result)