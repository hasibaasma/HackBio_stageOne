#!/bin/bash/python3

# Function to translate DNA into protein
def translate_dna_to_protein(dna_seq):
    # Standard genetic code dictionary
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

    dna_seq = dna_seq.upper()
    protein = ""

    # Translate codon-by-codon
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        aa = codon_table.get(codon, '?')  # '?' for unknown codon

        if aa == '*':  # Stop codon
            break

        protein += aa

    return protein


# Validate DNA sequence
def is_valid_dna(seq):
    valid = {'A', 'T', 'G', 'C'}
    for char in seq.upper():
        if char not in valid:
            return False
    return True


# Main function
def main():
    while True:  # Loop for multiple translations
        dna = input("Enter DNA sequence: ")

        # Validation
        if not is_valid_dna(dna):
            print("Error: Invalid DNA sequence! Only A, T, G, C allowed.")
            continue  # Ask again

        protein = translate_dna_to_protein(dna)
        print("Protein sequence:", protein)

        # Ask user if they want more translation
        choice = input("Do you want to translate another sequence? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting... Goodbye!")
            break


# Run main
if __name__ == "__main__":
    main()

