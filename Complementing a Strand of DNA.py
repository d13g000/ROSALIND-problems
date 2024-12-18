import os

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "rosalind_dna.txt")

with open(file_path, "r") as file:
    dna_string = file.read().strip()

# Create dictionary of complementary bases
complement = {"A": "T", "T": "A", "C": "G","G": "C"}

# Generate complementary sequence and reverse it
reverse_complement = ''.join(complement[base] for base in reversed(dna_string))

print("DNA string:         ", dna_string)
print("Reverse complement: ", reverse_complement)