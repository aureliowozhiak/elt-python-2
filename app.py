from methods.extract import Extract
from methods.transform import Transform
from methods.load import Load
from methods.tags import tags
import sys

def run(url):
    extract = Extract(url)
    load = Load()

    file_name = "_".join(url.split("/")[2::]).replace(".", "_")

    i = 0
    for table in extract.get_tags(tags["table"]):
        transform = Transform(table)
        df = transform.transform()
        if df.is_empty():
            continue

        load.save(df, f"{file_name}_{i}.csv")
        i += 1

for url in sys.argv[1:]:
    run(url)