def reverse_string(s):
    if len(s) == 0:
        return ""
    
    return reverse_string(s[1:]) + s[0]

# Example usage:
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)