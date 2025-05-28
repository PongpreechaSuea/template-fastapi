from io import BytesIO

import pandas as pd


def dataframe_to_markdown(df, sheet_name: str) -> str:
    df = df.dropna(axis=1, how='all').dropna(axis=0, how='all')
    df.columns = df.columns.str.strip().str.replace("Unnamed", "Columns", regex=False)
    
    markdown = f"### DataSheet: {sheet_name}\n\n| " + ' | '.join(df.columns) + ' |\n'
    markdown += '| ' + ' | '.join(['---' for _ in df.columns]) + ' |\n'

    for _, row in df.iterrows():
        markdown_row = []
        for item in row:
            item_str = str(item).replace("\n", " ").replace("  ", "").strip()
            if item_str == "nan" or item_str == "-":
                continue
            markdown_row.append(item_str)
        if len(markdown_row) <= 0:
            continue
        markdown += "| " + " | ".join(markdown_row) + " |\n"

    return markdown

def extract_text_from_xlsx(file_bytes: BytesIO):
    sheets_dict = pd.read_excel(file_bytes, sheet_name=None)
    content = []
    for sheet_name, data in sheets_dict.items():
        markdown = dataframe_to_markdown(data, sheet_name)
        content.append({
            "type": "text",
            "text": str(markdown)
        })
        
    return content, 0
