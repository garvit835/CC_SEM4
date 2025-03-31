def build_suffix_array(s):
    """ Constructs the suffix array using sorting (O(n log n)) """
    suffixes = sorted((s[i:], i) for i in range(len(s)))
    return [suffix[1] for suffix in suffixes]

def build_lcp(s, suffix_array):
    """ Constructs the LCP (Longest Common Prefix) array (O(n)) """
    n = len(s)
    rank = [0] * n
    lcp = [0] * n

    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1
    return lcp

def count_distinct_substrings(s):
    """ Uses Suffix Array + LCP to count distinct substrings efficiently """
    n = len(s)
    suffix_array = build_suffix_array(s)
    lcp = build_lcp(s, suffix_array)

    total_substrings = n * (n + 1) // 2  # Total substrings in a string of length n
    lcp_sum = sum(lcp)  # Sum of LCP array

    return total_substrings - lcp_sum  # Removing repeated substrings

# Example Usage
s = "abc"
print("Total Distinct Substrings:", count_distinct_substrings(s))
