import os
import wget
import pandas as pd

def generate_month(input) -> str:
    if type(input) == int:
        if input <= 12 and input > 0:
            return str(input).zfill(2)
        else :
            return "input error!"
    elif type(input) == str:
        if input.lower() in ["jan", "january", "januari", "1", "01"]:
            return "01"
        elif input.lower() in ["feb", "february", "februari","2", "02"]:
            return "02"
        elif input.lower() in ["mar", "march", "maret","3", "03"]:
            return "03"
        elif input.lower() in ["apr", "april", "4", "04"]:
            return "04"
        elif input.lower() in ["may", "mei","5", "05"]:
            return "05"
        elif input.lower() in ["jun", "june", "juni", "6", "06"]:
            return "06"
        elif input.lower() in ["jul", "july", "juli", "7", "07"]:
            return "07"
        elif input.lower() in ["aug", "august", "agustus", "8", "08"]:
            return "08"
        elif input.lower() in ["sept", "sep", "september", "9", "09"]:
            return "09"
        elif input.lower() in ["okt", "oct", "oktober", "october", "10"]:
            return "10"
        elif input.lower() in ["nov", "november", "11"]:
            return "11"
        elif input.lower() in ["des", "dec", "december", "desember", "12"]:
            return "12"

def download_data_from_url(url, dir):
    os.makedirs(dir, exist_ok = True)
    if url.split("/")[-1] in os.listdir(dir):
        print(f"{url} Already Exist")
    else:
        wget.download(url)
        print(f"Download {url} Done !")
    print()

def compile_parquetData_from_folder(dir):
    df = pd.DataFrame()
    for i in os.listdir(dir):
        temp_ = pd.read_parquet(dir + i)
        df = pd.concat([df, temp_])

    return df.reset_index(drop = True)



















