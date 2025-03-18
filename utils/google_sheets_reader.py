import gspread

def load_exchange_names(credentials_path, sheet_url):
    gc = gspread.service_account(filename=credentials_path)
    sheet = gc.open_by_url(sheet_url)
    worksheet = sheet.sheet1
    exchange_names = worksheet.col_values(1)  # Column A by default
    return [name.strip().lower() for name in exchange_names if name.strip()]
