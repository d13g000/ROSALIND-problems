import os

def hamming_distance(s, t):
    """ Calculates the Hamming distance between two DNA strings of equal length
    where:
    s = First DNA string
    t = Second DNA string"""
    # Ensure both strings are of equal length
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length.")

    # Calculate and return the Hamming distance
    return sum(1 for a, b in zip(s, t) if a != b) # Computes Hamming distance
    # by combining sequences into pairs of characters at the same index,
    # iterating over each pair and checking whether the letter is the same or
    # different, producing 1 if they are different and, summing up all the 1s
    # generated

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "rosalind_hamming.txt")

# Read the file and handle multi-line sequences
with open(file_path, "r") as file:
    lines = file.read().strip().splitlines()

sequence1 = [] # Create empty list for sequence 1
sequence2 = [] # Create empty list for sequence 2

# Assume the first half of the lines belong to the first sequence and the
# second half to the second sequence
halfway = len(lines) // 2

# Join lines into one continuous string for each sequence
sequence1 = "".join(lines[:halfway])
sequence2 = "".join(lines[halfway:])

# Ensure that two sequences are present
if not sequence1 or not sequence2:
    raise ValueError("File must contain exactly two DNA sequences.")

print(f"Hamming distance: {hamming_distance(sequence1, sequence2)}")