# Time Complexity: O(4n), because at each of the n-1 positions between digits we can insert one of three operators + , -, * or choose no operator (concatenate digits), generating all possible expressions.
# Auxiliary Space: O(n), for the recursion stack and the current expression being built




def add_operators(s, target):
    result = []

    def backtrack(index, path, value, last):
        if index == len(s):
            if value == target:
                result.append(path)
            return

        for i in range(index + 1, len(s) + 1):
            num_str = s[index:i]
            if len(num_str) > 1 and num_str[0] == '0':
                continue  # Skip leading zeros
            num = int(num_str)

            if index == 0:
                backtrack(i, num_str, num, num)
            else:
                backtrack(i, path + '+' + num_str, value + num, num)
                backtrack(i, path + '-' + num_str, value - num, -num)
                backtrack(i, path + '*' + num_str, value -
                          last + last * num, last * num)

    backtrack(0, "", 0, 0)
    return sorted(result)


# Example usage
s = "124"
target = 9
print(add_operators(s, target))
    


    