# Bank-Statement-Analysis

## Steps
### Part1. Categorization
1. Create categories.txt with categorization and hiererachy structure
Example: /data/categories.txt

### Part2. Prepare transaction activity data
1. Download original transaction activity csv files from online banking.
Original csv files should be saved in dir: /original_transactions/ with naming convention as <BANK>_<XXX>.csv, where
<BANK> section is support 1) AMEX, 2) BOA, 3)CHASE, 4) CITI, and
<XXX> could be anything such as account id to differentiate accounts.
Example: /original_transactions/BOA_1234_201901.csv

2. Use data_processor.py to get generate clean transaction data that can fit into the analytical models. Clean data will be generated in /clean_transactions/
Example: /original_transactions/BOA_1234_201901.csv 's clean data is
         /clean_transactions/BOA_1234_201901_clean.csv

3. Setup pre-labeld pretrained data.

4. TODO


Development Note:

- requirements.txt
$ python3 -m pip install -r requirement.txt --user
where
$ python3 is where I'm going to run this program
