You are going to complete the following tasks to reinforce your python skills in bioinformatics.

Write a python function for translating DNA to protein
Write a python function for calculating the hamming distance between your slack username (e.g josoga) and twitter/X (joseph) handle (synthesize one if you don’t have one). Feel free to pad it with extra words if they are not of the same length.
Furthermore, you are going to work with your team to review one of the following papers.
 Your literature review essay should be between 300-400 words long.
 Surprise Task

Reproduce the figures 1A-F below using Python Data Libraries (Pandas, Seaborn and maybe matplotlib)

📂 Datasets

Gene Expression (Heatmap & Volcano Plot)
a. Normalized counts for HBR vs UHR samples
b. Differential expression results (chromosome 22)
Breast Cancer Diagnostic Data (Correlation & Scatter/Density Plots)
c–f. Breast Cancer Wisconsin dataset
Tasks

Part A – Gene Expression Analysis

a. Heatmap
Use the normalized gene expression dataset to plot a clustered heatmap of the top differentially expressed genes between HBR and UHR samples.
Label both genes and samples.
Use a color gradient (e.g., Blues) to indicate expression levels.
b. Volcano Plot
Plot log2FoldChange vs log10(Padj) from the DEG results.
Color points by significance:
Upregulated: green
Downregulated: orange
Not significant: grey
Add dashed vertical lines at log2FoldChange = ±1.
Part B – Breast Cancer Data Exploration

c. Scatter Plot (radius vs texture)
Plot texture_mean vs radius_mean and color points by diagnosis (M = malignant, B = benign).
d. Correlation Heatmap
Compute the correlation matrix of six key features:

radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean.

Plot as a heatmap with correlation values annotated.

e. Scatter Plot (smoothness vs compactness)
Plot compactness_mean vs smoothness_mean colored by diagnosis.
Include gridlines and clear axis labels.
f. Density Plot (area distribution)
Plot kernel density estimates (KDE) of area_mean for both M and B diagnoses on the same axis.
Add legend and labeled axes.
