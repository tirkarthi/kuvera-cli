import os
import requests
import json

DONATION_MESSAGE = """
Hey there!

If you found the program useful please consider donating to the awesome folks at Python Software Foundation.
https://www.python.org/psf/donations/

PS : I love feedback. You can write to me at tir.karthi@gmail.com
"""

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def download_funds_file(funds_file='funds.json'):
    FUNDS_URL = "https://kuvera.in/funds.json?v=1.54.4"
    if not os.path.isfile(funds_file):
        with open(funds_file, 'wb+') as f:
            print("Downloading funds file")
            f.write(requests.get(FUNDS_URL).content)
    else:
        print("Funds file already exists and hence not downloading. If you need fresh data then consider deleting {}".format(funds_file))


def process_funds_file(funds_file='funds.json', output_dir='data'):
    FUND_DETAIL_URL = 'https://kuvera.in/api/v3/funds/{}.json?v=1.54.4'
    with open(funds_file) as f:
        funds = json.load(f)
        codes = []
        urls = []

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        else:
            print("Output directory already exists and hence not downloading. If you need fresh data then consider deleting {}".format(output_dir))
            return
            
        for fund in funds:
            codes.append(fund['code'])

        for chunk in chunks(codes, 10):
            filename = '_'.join(chunk) + ".json"
            url_param = '|'.join(chunk)
            urls.append((filename, FUND_DETAIL_URL.format(url_param)))

        print("Downloading funds details from the funds file")
        for filename, url in urls:
            file_path = os.path.join(output_dir, filename)
            if not os.path.isfile(file_path):
                with open(file_path, 'wb+') as f:
                    f.write(requests.get(url).content)

if __name__ == "__main__":
    download_funds_file()
    process_funds_file()
    print(DONATION_MESSAGE)
