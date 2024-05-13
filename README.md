# Nowcasting German GDP with text data

## Overview

This repository contains the code accompanying the paper "Nowcasting German GDP with Text Data" by Mariia Okuneva, Philipp Hauber, Kai Carstensen, and Jasper Bär. The repository provides detailed Jupyter notebooks that document the pre-processing steps applied to a dataset of articles from Handelsblatt, Süddeutsche Zeitung (SZ), Welt, and Deutsche Presse-Agentur (dpa).

Each folder within the repository corresponds to a specific source and includes a dedicated notebook that outlines the step-by-step pre-processing steps performed on that source's data. The specifics of each pre-processing step are detailed in the appendix of the paper, ensuring transparency and reproducibility.  

## Repository Structure

The repository is organized into several folders, each dedicated to a specific news media source or pre-processing task:

- [**Handelsblatt**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Handelsblatt)
  - [Handelsblatt.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Handelsblatt/Handelsblatt.ipynb): A notebook explaining all pre-processing steps applied to the Handelsblatt articles.

- [**SZ**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/SZ)
  - [SZ.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/SZ/SZ.ipynb): A notebook detailing the pre-processing steps carried out on articles from Süddeutsche Zeitung.

- [**Welt**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Welt)
  - [Welt.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Welt/Welt.ipynb): A notebook that documents the pre-processing steps for Welt articles.

- [**dpa**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa)
  - [dpa.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa/dpa.ipynb): A notebook describing the pre-processing steps for articles from Deutsche Presse-Agentur.
  - [Truecasing.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/dpa/Truecasing.ipynb): This notebook details the process of restoring proper casing in the dpa articles.

- [**Umlauts**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Umlauts)
  - [Umlauts_fix.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Umlauts/Umlauts_fix.ipynb): A notebook that explains the methodology for restoring umlauts in articles from SZ, Handelsblatt, and dpa.

- [**Collocations**](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Collocations)
  - [Collocations.ipynb](https://github.com/MashenkaOkuneva/newspaper_data_processing/tree/master/Collocations/Collocations.ipynb): This notebook explains how one can identify two-word and three-word collocations that are later used in topic modeling.
