from methods.extract import Extract
from methods.transform import Transform
from methods.load import Load
from methods.tags import tags

url = "https://pt.wikipedia.org/wiki/Python"

extract = Extract(url)
load = Load()

i = 0
for table in extract.get_tags(tags["table"]):
    transform = Transform(table)
    df = transform.transform()
    if df.is_empty():
        continue

    load.save(df, f"{i}.csv")
    i += 1