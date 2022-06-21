# What's this script
A simple python script that uses BeautifulSoup to parse the webpage with virus sample data at https://epicov.org/epi3/epi_set/EPI_SET_20220616yx?main=true. It writes the data in a CSV file in order to make it easier to work with.

# Running the script (unix/macOS)
Follow these instructions if the ones in this file don't work or if use a windows system: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. Install `pip` with `python3 -m pip install --user --upgrade pip`
2. (Optional) Create a virtual env and activate it
    1. `python3 -m venv env`
    2. `source env/bin/activate`
3. Install dependencies with `python3 -m pip install -r requirements.txt`

Please, run scrappers responsibly, don't overload the server and respect backoff timeouts.

# License
Licensed under de MIT license, see [LICENSE.md](/LICENSE.md)
