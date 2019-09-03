import pandas

def read_documentation_for_pandas():
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    return False

def read_file_return_dict(filename):
    # TODO write docstring
    excel = pandas.ExcelFile(filename)
    print("sheet names are {}".format(excel.sheet_names))
    # TODO move the sheet name as argument to make the method more generic (to work for different excels)
    data_frame = excel.parse('Sheet1')
    # TODO plot the data frame with bar representation, zipcode column as x axis, val1 as y
    # TODO use pyplot.show() to display the plot

    # TODO create dict from the data_frame
    return dict()

