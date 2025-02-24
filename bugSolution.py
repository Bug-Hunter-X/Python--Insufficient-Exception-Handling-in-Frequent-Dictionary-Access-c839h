def function_with_improved_handling(data, default_value=0):
    # Use the get() method to gracefully handle missing keys.
    value = data.get('missing_key', default_value)
    return value * 2

# Example usage with the improved handling:
my_data = {'key1': 10, 'key2': 20}
result = function_with_improved_handling(my_data)
print(result)

# Example with a missing key
my_data_missing = {'key1':10}
result_missing = function_with_improved_handling(my_data_missing)
print(result_missing)