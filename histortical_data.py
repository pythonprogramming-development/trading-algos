# nsepy library depracated 
# from datetime import datetime
# from nsepy import get_history
# from datetime import date

# Rel = get_history(symbol='INFY',
#                    start=date(2024,12,16),
#                    end=date(2024,12,20))

# print(Rel)
# print(type(Rel))
# my_array = Rel.to_numpy()
# print(my_array)
# print(type(my_array))
# my_array2 = Rel.values
# print(my_array2)


# def printTohtml(Alist, htmlfile):    
#     html =  "<html>\n<head></head>\n<style>p { margin: 0 !important; }</style>\n<body>\n"

#     title = "Study - User - zip file -  Last date modified"
#     html += '\n<p>' + title + '</p>\n'

    # for line in Alist:
    #     para = '<p>' + line + '</p>'
    #     print(line)
    #     # html += para

    # with open(htmlfile, 'w') as f:
    #     f.write(html + "\n</body>\n</html>")
    #     f.write(str(Alist))


# Alist =  [['123', 'user1', 'New Compressed (zipped) Folder.zip', '05-24-17'],
# ['123', 'user2', 'Iam.zip', '05-19-17'], ['abcd', 'Letsee.zip', '05-22-17'],
# ['Here', 'whichTwo.zip', '06-01-17']]

# printTohtml(my_array, 'zip_files.html')

# https://agshiv92.medium.com/dhow-to-extract-india-stock-market-data-in-python-in-the-easiest-way-e20e7d4484c5

from datetime import date
from jugaad_data.nse import stock_csv, stock_df

# Download as pandas dataframe
df = stock_df(symbol="SBIN", from_date=date(2025,1,20),
            to_date=date(2025,1,20), series="EQ")
print(df.head())

# https://github.com/jugaad-py/jugaad-data
# https://github.com/NSEDownload/NSEDownload

# pip install jugaad_data pandas
# python histortical_data.py