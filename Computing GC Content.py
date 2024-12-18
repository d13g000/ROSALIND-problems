import os

def parse_fasta(data):
    """Parses a FASTA format into a dictionary."""
    fasta_data = {}
    label = None
    for line in data.splitlines(): # Split data into lines
        if line.startswith(">"):
            label = line[1:]  # Remove '>' symbol and save as sequence name/key
            fasta_data[label] = "" # Set empty sequence/value
        else:
            fasta_data[label] += line.strip() # Add sequence to sequence/value
    return fasta_data # Returns dictionary with sequence name/key and
    # sequence/value

def gc_content(dna_sequence):
    """Calculates the GC content of a DNA sequence."""
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    return (gc_count / len(dna_sequence)) * 100 # Calculates %age GC content

def highest_gc_content(data):
    """Finds the label and GC content of the sequence with the highest GC
    content."""
    fasta_data = parse_fasta(data) # Runs parse_fasta function above
    max_label = None # Initial case where no sequence name is associated with
    # highest GC content
    max_gc = 0 # Initial case where GC content is not yet determined
    for label, sequence in fasta_data.items():
        gc = gc_content(sequence) # Runs gc_content function above
        if gc > max_gc:
            max_label = label # Resets label with sequence name
            max_gc = gc # Resets GC content
    return max_label, max_gc

# Read FASTA file
downloads_folder = os.path.expanduser("~/Downloads")
file_path = os.path.join(downloads_folder, "rosalind_fasta.txt")

# Ensure file exists before proceeding
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found at {file_path}. Please check the path.")

# Read FASTA data
with open(file_path, "r") as file:
    fasta_input = file.read()

# Process FASTA data
label, gc_percentage = highest_gc_content(fasta_input)

print(label)
print(f"{gc_percentage:.2f}")