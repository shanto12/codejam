import camelot




location = "C:\Users\shant\Downloads\Final Estimate.pdf"
tables = camelot.read_odf(location, pages=3)

print(tables)