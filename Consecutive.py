def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start only when num is the beginning of a sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    
    return longest
