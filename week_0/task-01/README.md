# Welcome To Moonlight Energy Solution Analsysis

On this part I will show you how you can run this project without any errors.

# Installation

Since the project is based on python libraries you need to install the
requirment packages

```bash
 #windows
 pip install -r requirment.txt

 #linux and mac
 pip3 install -r requirment.txt
```

# Guid to the file structure
```txt
    ├── .vscode/
    │   └── settings.json
    ├── .github/
    │   └── workflows
    │       ├── unittests.yml
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
     |------ src/
    ├── notebooks/
    │   ├── __init__.py
    │   └── README.md
    ├── tests/
    │   ├── __init__.py
    └── scripts/
        ├── __init__.py
        └── README.md
```
## notebooks
This directory include the necessary analysis in **jupyter notebook** each jupyter notebook is dedicated into cleaning and making EDA analysis on the repsective dataset.

## src
This directory have the custom helper program to help automate the process. 
Since the business objective is same and the reading(datasets) have same variables I have created a dataframewrapper file which have DataFrameWrapper class

I assumed the dataset variables are the same but the missing values might differ in each datasets so, the **DataFrameWrapper** class recieve the cleaned data

### DataFrameWrapper in the jupyter notebook

```python3
#import necessary package

import sys

#append the helper wrapper location relative to the file structure

sys.path.append("../src/") #in our case

#import the helper
from dataframewrapper import DataFrameWrapper

```
## Use of the DataFrameWrapper
+ Less storage by working on one instance
+ Relatively fast
+ Reducing Redundency for the same data


> [!CAUTION]
> The data-frame wrapper only works with this data set.


