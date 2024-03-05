# HW 10. Pandas
> *This is the repo for the tenth homework of the BI Python 2023 course*

## Usage
1. Clone this repo using SSH or HTTPS with the modules directory:
```bash
git clone git@github.com:Python-BI-2023/hw10-pandas-uzunmasha.git
``` 
**or**
```bash
git clone https://github.com/Python-BI-2023/hw10-pandas-uzunmasha.git
``` 
2. Launch the `HW10_Pandas.ipynb` in a code interpreter like Jupyter / VSCode / Google Colab.
3. Give a feedback on my code

### Homework description
This repo contains **`HW10_Pandas.ipynb`** and **`my_awesome_eda.py`** files.

`HW10_Pandas.ipynb` comprises 16 tasks related to various applications of Pandas.

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

The difference between missing values, such as NA, None, NAN, NULL:
* NaN (Not a Number) - means missing value. It appears in numerical columns with float type showing a missing value in that column. NaN is the default missing value marker.
* None (No one) - represents a missing entry, but its type is not numeric. So any column that contains a None value has object type.
* NA (not available) - Can be used in numeric and categorical columns. As I understood, Pandas changes it to NaN automatically.
* NULL (like zero) - represents an empty object. Usually, is not used in Pandas.
