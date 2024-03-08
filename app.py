from methods.extract import Extract

url = "https://pt.wikipedia.org/wiki/Python"

extract = Extract(url)

# Mapeamento de tags HTML para um dict

tags = {
    "paragraph": "p",
    "title": "h1",
    "subtitle": "h2",
    "link": "a",
    "list": "ul",
    "list_item": "li",
    "image": "img",
    "table": "table",
    "table_row": "tr",
    "table_header": "th",
    "table_data": "td"
}


table = extract.get_tags(tags["table"])[1]
