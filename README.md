# Nowcasting German GDP with text data

## Overview

This repository contains the code accompanying the paper "Nowcasting German GDP with Text Data" by Mariia Okuneva, Philipp Hauber, Kai Carstensen, and Jasper Bär. The repository provides detailed Jupyter notebooks that document the pre-processing steps applied to a dataset of articles from Handelsblatt, Süddeutsche Zeitung (SZ), Welt, and Deutsche Presse-Agentur (dpa).

Each folder within the repository corresponds to a specific source and includes a dedicated notebook that outlines the step-by-step pre-processing steps performed on that source's data. The specifics of each pre-processing step are detailed in the appendix of the paper, ensuring transparency and reproducibility.  

## Repository Structure

The repository is organized into several folders, each dedicated to a specific news media source or pre-processing task:

- [**Handelsblatt**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Handelsblatt)
  - [Handelsblatt.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Handelsblatt/Handelsblatt.ipynb): A notebook explaining all pre-processing steps applied to the Handelsblatt articles.

- [**SZ**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/SZ)
  - [SZ.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/SZ/SZ.ipynb): A notebook detailing the pre-processing steps carried out on articles from SZ.

- [**Welt**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Welt)
  - [Welt.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Welt/Welt.ipynb): A notebook that documents the pre-processing steps for Welt articles.

- [**dpa**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa)
  - [dpa.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa/dpa.ipynb): A notebook describing the pre-processing steps for articles from dpa.
  - [Truecasing.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa/Truecasing.ipynb): This notebook details the process of restoring proper casing in the dpa articles.

- [**Umlauts**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Umlauts)
  - [Umlauts_fix.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Umlauts/Umlauts_fix.ipynb): A notebook that explains the methodology for restoring umlauts in articles from SZ, Handelsblatt, and dpa.

- [**Collocations**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Collocations)
  - [Collocations.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Collocations/Collocations.ipynb): This notebook explains how one can identify two-word and three-word collocations that are later used in topic modeling.
  
## Data Pre-processing Steps Applied

### Steps Applied to All or the Majority of Sources:
1. **Short Article Removal**
2. **Removal of Exact Duplicates**
3. **Extensive Filtering**
4. **Language-Based Filtering**
5. **Umlaut Normalization**
6. **Number-Heavy Article Removal**
7. **Table Exclusion**
8. **Article Continuation Merging**
9. **Correction of OCR-Induced ‘O’ and ‘0’ Confusion**
10. **Separation of Merged Words and Numbers**
11. **Fuzzy Duplicates Removal**
12. **Exclusion of Articles with a High Proportion of German Names**
13. **Irrelevant Text Removal**

### Steps Specific to Each Source:

#### SZ:
- Exclusion of Regional News

#### Handelsblatt:
- Special Treatment for Short Articles that are Part of a Continuation
- Unicode Error Correction
- Removal of Articles with Encoding Issues and Non-Systematic Errors

#### Welt:
- Separation of Aggregated Articles
- Unicode Encoding Error Correction
- Removal of Articles within Time Intervals with Insufficient Data Availability

#### dpa:
- Deletion of dpa-Specific Duplicated Articles, such as News Corrections, News Updates, Summaries, Overviews, Repeated Articles, and Advance Notifications
- Separation of Compilations of News Articles into Individual Articles
- Removal of dpa-AFX Wirtschaftsnachrichten Articles
- Casing Correction

All the details on each pre-processing step can be found in the code and the appendix for the paper.

