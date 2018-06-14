import csv
import glob
import json
import sqlite3

DONATION_MESSAGE = """
Hey there! 

If you found the program useful please consider donating to the awesome folks at Python Software Foundation.
https://www.python.org/psf/donations/

PS : I love feedback. You can write to me at tir.karthi@gmail.com
"""

def create_table(cursor):
    print("Creating table")
    CREATE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS funds (portfolio_turnover text,code text,swp_flag text,lump_min float,stp_flag text,face_value float,sip_available text,sip_maximum_gap float,returns_date text,returns_inception text,returns_year_5 float,returns_year_1 float,returns_year_3 float,sip_multiplier float,ISIN text,investment_objective text,volatility float,name text,fund_house text,last_nav_date text,last_nav_nav float,fund_manager text,fund_category text,lump_multiplier float,redemption_allowed text,direct text,fund_type text,redemption_amount_minimum float,category text,sip_min float,detail_info text,redemption_quantity_multiple float,nav_date text,nav_nav text,switch_allowed text,lump_min_additional float,fund_name text,sip_max float,expense_ratio float,crisil_rating text,purchase_amount_multiplier float,instant text,redemption_quantity_minimum float,lump_available text,lump_max float,redemption_amount_multiple float,plan text)'''

    cursor.execute(CREATE_TABLE_QUERY)

def insert_fund(fund, cursor):
    columns = []
    values = []

    for key, value in fund.items():
        # Skip date fields
        if not "date" in key:
            if isinstance(value, (str, float, int)):
                columns.append(key)
                values.append(value)
            elif isinstance(value, dict):
                for k, v in value.items():
                    columns.append(key + "_" + k)
                    values.append(str(v))

    placeholders = ', '.join('?' * len(columns))
    columns = ', '.join(columns)
    sql = 'INSERT INTO funds ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, values)

def process_file(filename):
    with open(filename) as f:
        try:
            funds = json.load(f)
            for fund in funds:
                insert_fund(fund, cursor)
        except json.decoder.JSONDecodeError as e:
            print("Corrupt filename : ", filename)

def generate_csv(cursor, csv_file="data.csv"):
    cursor.execute("select * from funds;")
    with open(csv_file, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
            
if __name__ == "__main__":
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    create_table(cursor)

    print("Processing funds data")
    for filename in glob.iglob('data/*.json', recursive=True):
        process_file(filename)

    print("Generating csv at data.csv")
    generate_csv(cursor)
        
    conn.commit()
    conn.close()
    print("We are good to go!")
    print(DONATION_MESSAGE)
