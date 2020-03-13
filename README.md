# kuvera cli

I built this program since I had some limitations on the Kuvera platform where I was not able to sort by expense ratio, 1st year gains etc.

### Files (Refreshed as of 13/03/2020)

* data.db - SQLite file with funds data
* data.csv - CSV file with funds data

### Installation

* Clone the repo
* Activate virtualenv with `python3.6 -m venv kuvera-env && source kuvera-env/bin/activate`
* Install requirements with `pip install -r requirements.txt`
* Run `python crawler.py` which downloads the funds data inside the folder `data`
* Run `python insert-db.py` which inserts the data into SQLite database named `data.db` and also generates a CSV named `data.csv`


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

### Schema

```sqlite
sqlite> .mode line
sqlite> select * from funds order by returns_year_1 desc limit 1;
          portfolio_turnover =
                        code = RGRGD2-DP
                    swp_flag = Y
                    lump_min = 1000.0
                    stp_flag = Y
                  face_value = 10.0
               sip_available = Y
             sip_maximum_gap = 60.0
                returns_date = 2020-03-12
           returns_inception = 3.9046
              returns_year_5 = 9.955
              returns_year_1 = 37.6925
              returns_year_3 = 13.2844
              sip_multiplier = 1.0
                        ISIN = INF205K01NH3
        investment_objective = To provide returns that closely corresponds to returns providedby Religare Gold Exchange Traded Fund.
                  volatility = 25.2216
                        name = Invesco India Gold Dividend Payout Direct Plan
                  fund_house = INVESCOMUTUALFUND_MF
               last_nav_date = 2020-03-11
                last_nav_nav = 13.5802
                fund_manager = Krishna Cheemalapati
               fund_category = Fund of Funds
             lump_multiplier = 1.0
          redemption_allowed = Y
                      direct = Y
                   fund_type = Others
   redemption_amount_minimum = 1000.0
                    category = Equity
                     sip_min = 500.0
                 detail_info = https://invescomutualfund.com/literature-and-form?tab=Complete
redemption_quantity_multiple = 0.001
                    nav_date = 2020-03-12
                     nav_nav = 13.8013
              switch_allowed = Y
         lump_min_additional = 1000.0
                   fund_name = INVESCO Mutual Fund
                     sip_max = 999999999.0
               expense_ratio = 0.09
               crisil_rating = Moderately High
  purchase_amount_multiplier =
                     instant = N
 redemption_quantity_minimum = 0.001
              lump_available = Y
                    lump_max = 10000000000000.0
  redemption_amount_multiple = 1.0
                        plan = AS N WHEN
                  short_name = Invesco India Gold Dividend Payout
                  short_code = invesco
                reinvestment = N
                        slug = invesco-india-gold-dividend-payout--RGRGD2-DP
        channel_partner_code = 120RGD2
                  tax_period = 1095
               maturity_type = Open Ended
                         aum = 180
                  jan_31_nav = 9.3346
                 merged_code =
                 merged_name =
                 merged_date =
```

### Thanks

Thanks much to Gaurav Rastogi, CEO of Kuvera who was generous enough to allow this. Relevant thread : https://www.reddit.com/r/IndiaInvestments/comments/8r0k9q/kuveracli_a_simple_program_to_download_funds_data/e0oz5wf/

### Donation

If you found the program useful please consider donating to the awesome folks at Python Software Foundation. Refer : https://www.python.org/psf/donations/

### Disclaimer

No one holds responsibility for any inconsistency in data.

### LICENSE

Copyright © 2018 Karthikeyan S

Distributed under the MIT License
