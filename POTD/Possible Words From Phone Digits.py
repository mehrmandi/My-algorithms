# Recursive function to generate combinations
def possibleWordsRec(arr, index, prefix, padMap, res):
    if index == len(arr):
        res.append(prefix)
        return

    digit = arr[index]

    # Skip invalid digits
    if digit < 2 or digit > 9:
        possibleWordsRec(arr, index + 1, prefix, padMap, res)
        return

    # Place all possible letters for this digit
    for ch in padMap[digit]:
        possibleWordsRec(arr, index + 1, prefix + ch, padMap, res)


# Function to find all possible letter combinations
def possibleWords(arr):
    res = []

    # mapping numbers with letters
    padMap = ["", "", "abc", "def", "ghi", "jkl",
              "mno", "pqrs", "tuv", "wxyz"]

    possibleWordsRec(arr, 0, "", padMap, res)
    return res


if __name__ == "__main__":
    arr = [7, 8]
    words = possibleWords(arr)
    for word in words:
        print(word, end=" ")
