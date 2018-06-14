# kuvera cli

I built this program since I had some limitations on the Kuvera platform where I was not able to sort by expense ratio, 1st year gains etc.

### Installation

* Clone the repo
* Activate virtualenv with `python3.6 -m venv kuvera-env && source kuvera-env/bin/activate`
* Install requirements with `pip install -r requirements.txt`
* Run `python crawler.py` which downloads the funds data inside the folder `data`
* Run `python insert-db.py` which inserts the data into SQLite database named `data.db` and also generates a CSV named `data.csv`

### Files

* data.db - SQLite file with funds data
* data.csv - CSV file with funds data

### Sample use cases

* Top 10 funds with highest one year return

```sqlite
(kuvera-env) karthi@ubuntu:~/kuvera$ sqlite3 data.db
SQLite version 3.23.1 2018-04-10 17:39:29
Enter ".help" for usage hints.
sqlite> .mode column
sqlite> .headers on
sqlite> select name, returns_year_1 from funds order by returns_year_1 desc limit 10;
name                                                                        returns_year_1
--------------------------------------------------------------------------  --------------
INVESCO INDIA TREASURY ADVANTAGE DISCRETIONARY DIVIDEND PAYOUT DIRECT PLAN  66.6505
INVESCO INDIA TREASURY ADVANTAGE DISCRETIONARY DIVIDEND REINVEST DIRECT PL  66.6505
TATA DIGITAL INDIA REINVETSMENT DIVIDEND PAYOUT DIRECT PLAN                 51.2647
TATA DIGITAL INDIA REINVETSMENT DIVIDEND REINVEST DIRECT PLAN               51.2647
TATA DIGITAL INDIA GROWTH DIRECT PLAN                                       51.2647
ADITYA BIRLA SUN LIFE DIGITAL INDIA GROWTH DIRECT PLAN                      40.8273
ADITYA BIRLA SUN LIFE DIGITAL INDIA DIVIDEND PAYOUT DIRECT PLAN             40.8067
ADITYA BIRLA SUN LIFE DIGITAL INDIA DIVIDEND REINVEST DIRECT PLAN           40.8067
EDELWEISS LIQUID WEEKLY DIVIDEND PAYOUT DIRECT PLAN                         38.4686
EDELWEISS LIQUID WEEKLY DIVIDEND REINVEST DIRECT PLAN                       38.4686
```

* Fund with the highest expense ratio

```sqlite
(kuvera-env) karthi@ubuntu:~/kuvera$ sqlite3 data.db
SQLite version 3.23.1 2018-04-10 17:39:29
Enter ".help" for usage hints.
sqlite> .mode column
sqlite> .headers on
sqlite> select name, expense_ratio  from funds order by expense_ratio desc limit 1;
name                                          expense_ratio
--------------------------------------------  -------------
TAURUS TAXSHIELD DIVIDEND PAYOUT DIRECT PLAN  2.47
```

### Donation

If you found the program useful please consider donating to the awesome folks at Python Software Foundation. Refer : https://www.python.org/psf/donations/

### Disclaimer

The data is from Kuvera and I don't hold responsibility for any inconsistency in data.

### LICENSE

Copyright © 2018 Karthikeyan S

Distributed under the MIT License