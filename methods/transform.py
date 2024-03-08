import polars as pl
from methods.tags import tags

class Transform:

    def __init__(self, table):
        self.table = table

    # Get the data of the table
    def get_data_list(self):
        data_list = []
        for row in self.table.find_all(tags["table_row"]):
            row_data = []
            for data in row.find_all(tags["table_data"]):
                row_data.append(data.text)
            if not row_data:
                continue

            data_list.append(row_data)
        return data_list

    # Get the headers of the table
    def get_headers(self):
        headers = []
        for header in self.table.find_all(tags["table_header"]):
            headers.append(header.text)
        return headers
  
    # Transform a list into a dict
    def get_data_dict(self):
        data_dict = {}
        for i, header in enumerate(self.get_headers()):
            data_dict[header] = [row[i] for row in self.get_data_list()[1:]]
        return data_dict

    # Transform a dict into a DataFrame polars
    def transform(self):
        try:
            return pl.DataFrame(self.get_data_dict())
        except:
            return pl.DataFrame({})