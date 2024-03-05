# HW 11. Visualization
> *This is the repo for the tenth homework of the BI Python 2023 course*

**The heatmap plot was visualized after the deadline, EDA plots were before.**

## Usage
1. Clone this repo using SSH or HTTPS with the modules directory:
```bash
git clone git@github.com:Python-BI-2023/hw11-visualisation-uzunmasha.git
``` 
**or**
```bash
git clone https://github.com/Python-BI-2023/hw11-visualisation-uzunmasha.git
``` 
2. Launch the `HW11_Visualisation.ipynb` in a code interpreter like Jupyter / VSCode / Google Colab.
3. Give a feedback on my code

### Homework description
This repo contains **`HW11_Visualisation.ipynb`** and **`my_awesome_eda.py`** files.

`HW11_Visualisation.ipynb` comprises tasks related to various visualization tasks.

It also launches EDA module from `my_awesome_eda.py` and demonstrates statistics of particlular dataset.

EDA file contains:

* Greeting!
* Number of observations (rows) and parameters (features, columns).
* Data types of each column.
* For each <b>categorical</b> feature, displays counts and frequencies (counts / total_counts) of values in the dataframe.
* For each <b>numerical</b> feature, displays its min, max, mean, std, q0.25, median, and q0.75.
* Displays the number of outliers for each numerical feature that has outliers (applying the rule ± 1.5 IQR).
* Displays how many missing values are there in total in the dataframe, how many rows contain missing values, and which columns contain missing values.
* Displays how many duplicate rows are there in the dataframe.
* Shows boxplot for a fraction of missing values for all columns.
* Displays heatmap for numerical values correlations.
