def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Incompatible types"

result = function(5, "hello")
print(result) # Output: Error: Incompatible types

result2 = function(5, 10)
print(result2) # Output: 15