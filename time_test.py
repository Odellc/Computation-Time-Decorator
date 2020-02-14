import sys 
import os
import pandas as pd
from pandas import read_excel
import datetime
from datetime import datetime
from modules.computation_time import computation_time


file_path = os.path.join(os.curdir)
output_path = os.path.join(os.curdir, os.pardir, 'Data', 'test')
today = datetime.today()


@computation_time(message="Double Loop Time:")
def dloop_test(data):
    customers = []
    for rep in data["REP"]:
        df = data[data["REP"]==rep]
        for customer in df["Customer"]:
            customers.append(customer)

    print(f"number of rows = {len(customers)}")

@computation_time(message="Double List Comprehension Time:")
def dlist_comp_test(data):
    print(f'number of rows = {len([customer for rep in data["REP"] for customer in data[data["REP"]==rep]["Customer"]])}')

@computation_time(message="Read File Time:")
def read_file(path, fileName):
    file_path = os.path.join(path, fileName)
    try:
        return read_excel(file_path)
    except FileNotFoundError:
        return pd.DataFrame()

@computation_time(message="Single Loop Time:")
def sloop_test(data):
    reps = []
    for rep in data["REP"]:
        reps.append(rep)

    print(f"number of rows = {len(reps)}")

@computation_time(message="Single List Comprehension:")
def slist_comp_test(data):
    print(f'number of rows = {len([rep for rep in data["REP"]])}')


def main():
    data = read_file(file_path, "test_data.xlsx")

    sloop_test(data)
    slist_comp_test(data)

    dloop_test(data)
    
    dlist_comp_test(data)


if __name__ == "__main__":
    main()