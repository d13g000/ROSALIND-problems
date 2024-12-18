import os  # os module is used to navigate

# Navigate to required file in "Downloads" directory
downloads_folder = os.path.join(os.path.expanduser("~"),"Downloads")
# "Downloads" directory
file_path = os.path.join(downloads_folder, "rosalind_dna.txt") # File name

with open(file_path, "r") as file:
    dna_string = file.read().strip()  # Remove any spaces or new line markers

count_a = dna_string.count("A")  # Count occurrences of A
count_c = dna_string.count("C")  # Count occurrences of C
count_g = dna_string.count("G")  # Count occurrences of G
count_t = dna_string.count("T")  # Count occurrences of T

print(f"A: {count_a}")
print(f"C: {count_c}")
print(f"G: {count_g}")
print(f"T: {count_t}")