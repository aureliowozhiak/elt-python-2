
class Load:
    def __init__(self):
        pass

    def save(self, df, path_name):
        df.write_csv("csv/" + path_name, separator=",")