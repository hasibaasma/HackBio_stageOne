#!/usr/bin/env python3
# full_code.py

"""
FULL  SCRIPT
Includes:
1. DNA → Protein Translator (interactive)
2. Hamming Distance Calculator (interactive)
3. Gene Expression Analysis (heatmap + volcano plot)
4. Breast Cancer Data Exploration (scatter, heatmap, KDE)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ----------------------------------------------------------
# PART 1 — DNA → PROTEIN TRANSLATION
# ----------------------------------------------------------

codon_table = {
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
    'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
    'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
    'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
    'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
    'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
    'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
    'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
    'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
    'TAC':'Y','TAT':'Y','TAA':'*','TAG':'*',
    'TGC':'C','TGT':'C','TGA':'*','TGG':'W'
}

def is_valid_dna(seq):
    return all(c in "ATGC" for c in seq.upper())

def translate_dna_to_protein(dna_seq):
    dna_seq = dna_seq.upper()
    protein = ""

    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        aa = codon_table.get(codon, '?')
        if aa == "*":
            break
        protein += aa
    return protein

def run_dna_translation():
    while True:
        dna = input("\nEnter DNA sequence: ").strip()

        if not is_valid_dna(dna):
            print("❌ ERROR: Invalid nucleotide detected (only A,T,G,C allowed).")
            continue

        protein = translate_dna_to_protein(dna)
        print("✔ Protein sequence:", protein)

        again = input("Translate another? (yes/no): ").lower()
        if again != "yes":
            break


# ----------------------------------------------------------
# PART 2 — HAMMING DISTANCE
# ----------------------------------------------------------

def hamming_distance(str1, str2, ignore_spaces=False):
    if ignore_spaces:
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")

    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len)
    str2 = str2.ljust(max_len)

    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance, str1, str2

def run_hamming():
    print("\n=== Hamming Distance Calculator ===")

    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    choice = input("Ignore spaces? (yes/no): ").lower()
    ignore_spaces = (choice == "yes")

    distance, s1_p, s2_p = hamming_distance(s1, s2, ignore_spaces)

    print("\nProcessed Strings:")
    print("String 1:", repr(s1_p))
    print("String 2:", repr(s2_p))
    print("Hamming Distance:", distance)


# ----------------------------------------------------------
# PART 3 — GENE EXPRESSION ANALYSIS
# ----------------------------------------------------------

def heatmap_expression():
    df = pd.read_csv("hbr_uhr_top_deg_normalized_counts.csv", index_col=0)
    sns.clustermap(df, cmap="Blues", figsize=(10,12))
    plt.title("Heatmap of Top DEGs (HBR vs UHR)")
    plt.show()

def volcano_plot():
    df = pd.read_csv("hbr_uhr_deg_chr22_with_significance.csv")

    df["PAdj"] = df["PAdj"].replace(0, 1e-300).fillna(1)
    df["-log10PAdj"] = -np.log10(df["PAdj"])

    def classify(r):
        if r["PAdj"] < 0.05:
            if r["log2FoldChange"] >= 1: return "Up"
            if r["log2FoldChange"] <= -1: return "Down"
        return "NS"

    df["category"] = df.apply(classify, axis=1)

    colors = {"Up": "green", "Down": "orange", "NS": "grey"}

    plt.figure(figsize=(10,6))
    for cat, color in colors.items():
        subset = df[df["category"] == cat]
        plt.scatter(subset["log2FoldChange"], subset["-log10PAdj"], c=color, label=cat, alpha=0.7)

    plt.axvline(1, linestyle="--", color="black")
    plt.axvline(-1, linestyle="--", color="black")

    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10(PAdj)")
    plt.title("Volcano Plot (Chr22)")
    plt.legend()
    plt.show()


# ----------------------------------------------------------
# PART 4 — BREAST CANCER DATA EXPLORATION
# ----------------------------------------------------------

def breast_cancer_plots():
    df = pd.read_csv("data-3.csv")

    # c. Scatter Plot
    colors = {"M":"red", "B":"blue"}
    plt.figure()
    for d in df["diagnosis"].unique():
        sub = df[df["diagnosis"] == d]
        plt.scatter(sub["radius_mean"], sub["texture_mean"], c=colors[d], label=d, alpha=0.7)
    plt.title("Radius vs Texture")
    plt.xlabel("Radius Mean")
    plt.ylabel("Texture Mean")
    plt.legend()
    plt.grid()
    plt.show()

    # d. Correlation Heatmap
    features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean"]
    corr = df[features].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

    # e. Scatter smoothness vs compactness
    plt.figure()
    for d in df["diagnosis"].unique():
        sub = df[df["diagnosis"] == d]
        plt.scatter(sub["smoothness_mean"], sub["compactness_mean"], c=colors[d], label=d, alpha=0.7)
    plt.xlabel("Smoothness Mean")
    plt.ylabel("Compactness Mean")
    plt.title("Smoothness vs Compactness")
    plt.grid()
    plt.legend()
    plt.show()

    # f. KDE plot
    sns.kdeplot(df[df["diagnosis"]=="M"]["area_mean"], shade=True, label="Malignant")
    sns.kdeplot(df[df["diagnosis"]=="B"]["area_mean"], shade=True, label="Benign")
    plt.xlabel("Area Mean")
    plt.ylabel("Density")
    plt.title("Area Mean Distribution")
    plt.legend()
    plt.show()


# ----------------------------------------------------------
# SINGLE MENU-BASED MAIN()
# ----------------------------------------------------------

def main():
    while True:
        print("""
========= MAIN MENU =========
1. DNA → Protein Translation
2. Hamming Distance Calculator
3. Heatmap (Gene Expression)
4. Volcano Plot
5. Breast Cancer Plots
0. EXIT
""")
        choice = input("Choose an option: ")

        if choice == "1":
            run_dna_translation()
        elif choice == "2":
            run_hamming()
        elif choice == "3":
            heatmap_expression()
        elif choice == "4":
            volcano_plot()
        elif choice == "5":
            breast_cancer_plots()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
