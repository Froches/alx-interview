def minOperations(n):
    if n == 1:
        return 0  # Base case: Already have one 'H'
    
    operations = 0
    clipboard = 1  # Initialize clipboard with one 'H'
    buffer = 1  # Start with one 'H' in the buffer

    while buffer < n:
        if n % buffer == 0:
            # If n is divisible by buffer, it's possible to get n 'H's
            clipboard = buffer  # Update clipboard to the current buffer size
            operations += 1  # Perform one Copy All operation
        operations += 1  # Perform one Paste operation
        buffer += clipboard  # Add clipboard size to the buffer
    
    if buffer == n:
        return operations
    else:
        return 0  # Impossible to achieve n 'H's

# Example usage:
n = 9
print(minOperations(n))  # Output: 6
