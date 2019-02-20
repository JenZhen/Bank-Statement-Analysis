# Bank-Statement-Analysis

## Steps
Part1. Categorization
### 1. Create categories.txt with categorization and hiererachy structure

Part2. Prepare statement data
### 1. Parse PDF Statement transaction lines into raw data in csv file
    csp_01-01-2019.pdf --> csp_01-01-2019_raw.csv
### 2. Predict new statement against pretrained data -- if no pretrainied data, label all new transaction with categorization id (taken as correction process) -- if prediction correct, enter to skip, if wrong, enter id to correct.
    Predicted data contains 2 parts -- 1) Expense/Income type, 2) Vendor name
    csp_01-01-2019_raw.csv --> csp_01-01-2019_labeled.csv
### 3. Add labeled data to pretrained data. Remove duplicate from this step. (TODO: definition of duplicate).
    Display/Visualization of previous labeled data csp_01-01-2019.csv
### 4. Analyze transactions for certain period of time. It could be the aggregation of multiple labeled csv files. Data visualization could be presented in form of jupyter notebook.



Development Note:

- requirements.txt
$ python3 -m pip install -r requirement.txt --user
where
$ python3 is where I'm going to run this program
