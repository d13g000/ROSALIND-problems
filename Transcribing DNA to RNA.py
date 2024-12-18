import os

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_folder, "rosalind_dna.txt")

with open(file_path, "r") as file:
    dna_string = file.read().strip()

rna_string = dna_string.replace('T', 'U')  # Replace all instances
# of T with U

print("DNA string:", dna_string)
print("RNA string:", rna_string)