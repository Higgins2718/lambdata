#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3

"""
    Lambdata - a collection of Data Science helperr functions
"""


import pandas as pandas
import example_module
from datetime import datetime

# Y = example_module.increment(example_module.x)
time = datetime.today().strftime('%Y-%m-%d')
df = pandas.DataFrame({'time':time}, index=[0])
print(df)

TEST = example_module.split_datetime('time', df)
print(TEST)
test_list = ['banana', 'apple', 'orange', 'grape']
TEST2 = example_module.list_to_column(test_list, df, "Fruits")
print(TEST2)
