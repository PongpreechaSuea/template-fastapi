from io import BytesIO

import pandas as pd


def csv_to_markdown(file_path: str) -> str:
    data = pd.read_csv(file_path)
    
    markdown_table = "| " + " | ".join(data.columns) + " | \n"
    markdown_table += "| " + " | ".join(["---"] * len(data.columns)) + " | \n"
    markdown_table = markdown_table.replace("Unnamed", "Columns")

    for _, row in data.iterrows():
        markdown_row = []
        for item in row:
            item_str = str(item).replace("\n", " ").replace("  ", "").strip()
            if item_str == "nan" or item_str == "-":
                continue
            markdown_row.append(item_str)
        if len(markdown_row) <= 0:
            continue
        markdown_table += "| " + " | ".join(markdown_row) + " |\n"

    return markdown_table

def extract_text_from_csv(file_bytes: BytesIO):
    markdown = csv_to_markdown(file_bytes)
    return [{
        "type": "text",
        "text": markdown
    }] , 0