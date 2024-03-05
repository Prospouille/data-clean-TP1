import os
import requests
import numpy as np
import pandas as pd
import data_cleaning as fonctions


DATA_PATH = 'data/MMM_MMM_DAE.csv'


def download_data(url, force_download=False, ):
    # Utility function to donwload data if it is not in disk
    data_path = os.path.join('data', os.path.basename(url.split('?')[0]))
    if not os.path.exists(data_path) or force_download:
        # ensure data dir is created
        os.makedirs('data', exist_ok=True)
        # request data from url
        response = requests.get(url, allow_redirects=True)
        # save file
        with open(data_path, "w") as f:
            # Note the content of the response is in binary form: 
            # it needs to be decoded.
            # The response object also contains info about the encoding format
            # which we use as argument for the decoding
            f.write(response.content.decode(response.apparent_encoding))

    return data_path


def load_formatted_data(data_fname:str) -> pd.DataFrame:
    """ One function to read csv into a df with appropriate types/formats.
        Note: read only pertinent columns, ignore the others.
    """
    columns=["nom","lat_coor1","long_coor1","adr_num","adr_voie","com_cp","com_nom","dermnt","freq_mnt","tel1"] 
    df = pd.read_csv(
        data_fname,
        usecols=columns,
        encoding='latin-1'
        )
    
    df["nom"]=df["nom"].astype(str, errors='ignore')
    df["lat_coor1"]=df["lat_coor1"].astype(float, errors='ignore')
    df["long_coor1"]=df["long_coor1"].astype(float, errors='ignore')
    df["adr_num"]=df["adr_num"].astype(int, errors='ignore')
    df["adr_voie"]=df["adr_voie"].astype(str, errors='ignore')
    df["com_cp"]=df["com_cp"].astype(int, errors='ignore')
    df["com_nom"]=df["com_nom"].astype(str, errors='ignore')
    df["dermnt"]=df["dermnt"].astype(str, errors='ignore')  #a modif pour datetime
    df["freq_mnt"]=df["freq_mnt"].astype(str, errors='ignore') 
    df["tel1"]=df["tel1"].astype(str, errors='ignore')
    return df

# once they are all done, call them in the general sanitizing function
def sanitize_data(df:pd.DataFrame) -> pd.DataFrame:
    """ One function to do all sanitizing"""
    columns=["nom","lat_coor1","long_coor1","adr_num","adr_voie","com_cp","com_nom","dermnt","freq_mnt","tel1"]   
    columns_float=["lat_coor1","long_coor1","adr_num","com_cp"]
    for col in columns:
        df[col]=df[col].apply(fonctions.remplace_if_na)

    for col in columns_float:    
        df[col]=df[col].apply(fonctions.remplace_if_nan)

    df["freq_mnt"]=df["freq_mnt"].apply(fonctions.remplace_frq)


    df["com_cp"]=df["com_cp"].apply(fonctions.remplace_if_nan)
    df["long_coor1"]=df["long_coor1"].apply(fonctions.remplace_if_nan)
    df["lat_coor1"]=df["lat_coor1"].apply(fonctions.remplace_if_nan)
    df["adr_num"]=df["adr_num"].apply(fonctions.remplace_if_nan)

    df['adr_num']=df['adr_num'].apply(fonctions.replace_adress)
    df['adr_voie']=df['adr_voie'].apply(fonctions.replace_adress)

    df['Adresse'] = df['adr_num'].astype(str) + " " + df['adr_voie'].astype(str) + ", " + df['com_cp'].astype(str) + ", " + df['com_nom'].astype(str)
    # df['Adresse']=df['Adresse'].apply(replace_adress)
    df=df.drop('adr_num',axis=1)
    df=df.drop('adr_voie',axis=1)
    df=df.drop('com_cp',axis=1)
    df=df.drop('com_nom',axis=1)
    df["nom"]=df["nom"].str.upper()

    df['dermnt']=pd.to_datetime(df['dermnt'],errors='coerce')
    df['dermnt']=df['dermnt'].apply(fonctions.ValidateDate)
    return df


# Define a framing function
def frame_data(df:pd.DataFrame) -> pd.DataFrame:
    """ One function all framing (column renaming, column merge)"""
    df.rename(...)
    ...
    return df


# once they are all done, call them in the general clean loading function
def load_clean_data(df:pd.DataFrame)-> pd.DataFrame:
    """one function to run it all and return a clean df"""
    df =(load_formatted_data(df))
    #        .pipe(sanitize_data)
    #        .pipe(frame_data))
    return df


# if the module is called, run the main loading function
if __name__ == '__main__':
    df=load_clean_data(download_data("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_DAE.csv"))
    print(df)