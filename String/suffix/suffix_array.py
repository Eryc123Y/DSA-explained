def build_suffix_array_naive(text):
    """
    Builds a suffix array for the given text using the naive approach.

    Args:
        text: The input string.

    Returns:
        A list representing the suffix array (sorted starting indices).
    """
    # Add a unique character with the smallest lexicographical value
    # This helps in comparing suffixes of different lengths and ensures all suffixes are unique strings
    processed_text = text + '$'
    n = len(processed_text)

    # Create a list of tuples: (suffix string, original starting index)
    suffixes = []
    for i in range(n):
        suffixes.append((processed_text[i:], i))

    # Sort the list of tuples based on the suffix string (lexicographical comparison)
    # Python's sort is stable and handles string comparisons directly
    suffixes.sort(key=lambda x: x[0])

    # Extract the original starting indices from the sorted list
    suffix_array = [index for _, index in suffixes]

    return suffix_array


def build_suffix_array_doubling(text):
    """
    Builds a suffix array for the given text using the prefix doubling approach.

    Args:
        text: The input string.

    Returns:
        A list representing the suffix array (sorted starting indices).
    """
    # Add a unique character with the smallest lexicographical value
    processed_text = text + '$'
    n = len(processed_text)

    # SA: Suffix Array - stores starting indices of sorted suffixes
    # Rank: stores the rank of the suffix starting at index i
    # newRank: stores the rank in the next iteration
    sa = list(range(n))
    rank = [ord(c) for c in processed_text] # Initial rank based on first character's ASCII value
    newRank = [0] * n

    k = 1 # Current length of the prefix being considered (starts at 1)

    # The main loop iterates until the comparison length (k * 2) is >= n
    # In each iteration, we sort based on prefixes of length k * 2
    while k < n:
        # Sort suffixes based on the pair (rank of first k characters, rank of next k characters)
        # We use key-based sorting, sorting primarily by the second part, then the first part
        # Python's sort is stable, which is crucial for this algorithm

        # The key for sorting will be (rank[i], rank[i+k] if i+k < n else -1)
        # We use -1 for the second part if the suffix part goes beyond the string boundary
        # -1 is chosen because '$' has the smallest rank initially, and any valid character rank is >= 0
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))

        # Update the ranks based on the new order in SA
        # The first suffix in the sorted list gets rank 0
        newRank[sa[0]] = 0
        # Subsequent suffixes get a rank. If a suffix is different from the previous one
        # (based on the 2*k length prefix), it gets a new rank. Otherwise, it gets the same rank.
        for i in range(1, n):
            # Compare suffix starting at sa[i] and sa[i-1] using their ranks from the previous iteration
            prev_suffix_pair = (rank[sa[i-1]], rank[sa[i-1] + k] if sa[i-1] + k < n else -1)
            current_suffix_pair = (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else -1)

            if current_suffix_pair == prev_suffix_pair:
                newRank[sa[i]] = newRank[sa[i-1]]
            else:
                newRank[sa[i]] = newRank[sa[i-1]] + 1

        # Check if all ranks are unique. If so, sorting is complete.
        # The maximum possible rank is n-1. If the highest rank reached is n-1,
        # it means all n suffixes have distinct ranks.
        rank = list(newRank) # Update rank for the next iteration
        if rank[sa[n-1]] == n - 1:
             break # All suffixes are uniquely sorted

        k *= 2 # Double the length of the prefix for the next iteration

    return sa

def main():
    # Example Usage:
    text = "banana"
    sa_doubling = build_suffix_array_doubling(text)
    print(f"Original text: {text}")
    print(f"Processed text: {text+'$'}")
    print(f"Doubling Suffix Array: {sa_doubling}")

    # The output should be the same as the naive method: [6, 5, 3, 1, 0, 4, 2]

    # Example Usage:
    text = "banana"
    sa_naive = build_suffix_array_naive(text)
    print(f"Original text: {text}")
    print(f"Processed text: {text+'$'}")
    print(f"Naive Suffix Array: {sa_naive}")

    # Let's verify the sorted suffixes based on the naive SA:
    # banana$ -> 0
    # anana$  -> 1
    # nana$   -> 2
    # ana$    -> 3
    # na$     -> 4
    # a$      -> 5
    # $       -> 6

    # Indices in SA_naive: [6, 5, 3, 1, 0, 4, 2]
    # Corresponding suffixes:
    # processed_text[6:] = "$"
    # processed_text[5:] = "a$"
    # processed_text[3:] = "ana$"
    # processed_text[1:] = "anana$"
    # processed_text[0:] = "banana$"
    # processed_text[4:] = "na$"
    # processed_text[2:] = "nana$"
    # This matches the sorted list we derived manually earlier.

if __name__ == "__main__":
    main()
