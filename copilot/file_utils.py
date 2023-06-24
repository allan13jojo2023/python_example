import pdftotext

# open pdf file
# and convert to pandas dataframe
# return dataframe
def open_pdf_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            pdf = pdftotext.PDF(f)  # need install manually
        return pdf
    except Exception as e:
        print(e)
        return None

# compare two dataframe
# return difference
def compare_dataframe(df1, df2):
    pass

# compare two dataframe
# expected column header match exactly
# expected column value match exactly
# return difference row and column as result dataframe
def compare_dataframe_exact(df1, df2):
    pass

# compare two dictionary
# return difference
def compare_dictionary(dict1, dict2):
    pass