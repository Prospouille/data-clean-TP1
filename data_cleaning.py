import csv 
import pandas as pd 
import numpy as np
# import unicode
import datetime

def remplace_if_nan(cell):
    if pd.notna(cell) and isinstance(cell, (float, int)): 
        #print(cell)       
        return np.nan
    return cell

def remplace_if_na(cell):
    if not isinstance(cell, str) or cell == " " or cell == "-" or cell =="":
        return pd.NA
    return cell

def remplace_frq(cell):
    #print(cell)
    if pd.notna(cell):
        if cell.lower()=="tous les ans":
            return "Annuel"
        elif cell.lower()=="tous les mois":
            return "Mensuel"
        elif cell.lower()=="tous les jours":
            return "Quotidien"
        elif cell.lower()=="toutes les semaines":
            return "Hebdomadaire"
        elif cell.lower()=="tous les trimestres":
            return "Trimestrielle"
        elif cell.lower()=="tous les semestres":
            return "Semestrielle"
        else:
            return pd.NA
        
    return cell

def Validate_Com_Nom(cell):
    if pd.notna(cell): 
        cell= cell.lower().capitalize()
    return cell


def ValidateName(cell_name):
    if pd.notna(cell_name):
        if "montpellier" in cell_name.lower():
            return pd.NA
        else: 
            liste=list(cell_name)
            for letter in range (len(liste)):
                liste[letter] = liste[letter].lower()
            liste[0]=liste[0].upper()
            for letter in range (len(liste)-1):
                if liste[letter]== " " or liste[letter]=='"':
                    liste[letter + 1] = liste[letter + 1].upper()
            cell_name= ''.join(liste)
    return cell_name

def ValidateDate(cell_date):
    if not isinstance(cell_date,pd.Timestamp):
        return pd.NA
    else:
        cell_date = cell_date.date()
    return cell_date

def suppr_space(cell):
    if pd.notna(cell):
        liste=list(cell)
        if liste[0]==" ":
            liste=liste[1:]
        if liste[-1]==" ":
            liste=liste[:-1]
        for i in range(len(liste)-1):

            if liste[i]==" " and liste[i+1]== " ":
                liste=liste[:i] + liste[i:]
    return cell
    

    


def replace_adress(cell):
    if pd.notna(cell):
        list=cell.split(" ")
        for word in list:
            if word == "Montpellier" or word =="34000" or word =="34070" or word =="34090":
                return pd.NA
    return cell

def remplace_if_notadate(cell):
    pass


def telephone(cell):
    if pd.notna(cell):
        
        if cell[0]!="+":
            cell = '+' + cell
        cell=cell[:3] + " " + cell[3:]
    return cell
    
    

# type_cols={"nom":str,"lat_coor1":str,"long_coor1":str,"adr_num":str,"adr_voie":str,"com_cp":str,"com_nom":str,"freq_mnt":str,"tel1":str}
columns=["nom","lat_coor1","long_coor1","adr_num","adr_voie","com_cp","com_nom","dermnt","freq_mnt","tel1"]   
columns_float=["lat_coor1","long_coor1","adr_num","com_cp"]

# dataframe=pd.read_csv("C:/Users/Le Cornec/Desktop/data_cleaning/MMM_MMM_DAE.csv", sep=",", usecols=columns,dtype=type_cols)

# for col in columns:
#     dataframe[col]=dataframe[col].apply(remplace_if_na)




# for col in columns_float:    
#     dataframe[col]=dataframe[col].apply(remplace_if_nan)

# dataframe["freq_mnt"]=dataframe["freq_mnt"].apply(remplace_frq)


# dataframe["com_cp"]=dataframe["com_cp"].apply(remplace_if_nan)
# dataframe["long_coor1"]=dataframe["long_coor1"].apply(remplace_if_nan)
# dataframe["lat_coor1"]=dataframe["lat_coor1"].apply(remplace_if_nan)
# dataframe["adr_num"]=dataframe["adr_num"].apply(remplace_if_nan)

# dataframe['adr_num']=dataframe['adr_num'].apply(replace_adress)
# dataframe['adr_voie']=dataframe['adr_voie'].apply(replace_adress)

# dataframe['Adresse'] = dataframe['adr_num'].astype(str) + " " + dataframe['adr_voie'].astype(str) + ", " + dataframe['com_cp'].astype(str) + ", " + dataframe['com_nom'].astype(str)
# # dataframe['Adresse']=dataframe['Adresse'].apply(replace_adress)
# dataframe=dataframe.drop('adr_num',axis=1)
# dataframe=dataframe.drop('adr_voie',axis=1)
# dataframe=dataframe.drop('com_cp',axis=1)
# dataframe=dataframe.drop('com_nom',axis=1)
# dataframe["nom"]=dataframe["nom"].str.upper()

# dataframe['dermnt']=pd.to_datetime(dataframe['dermnt'],errors='coerce')
# dataframe['dermnt']=dataframe['dermnt'].apply(ValidateDate)

## dataframe["freq_mnt"]=dataframe["freq_mnt"].replace("Tous les ans", "tous les ans")
## dataframe["freq_mnt"]=dataframe["freq_mnt"].replace("tous les ans", "annuel")

##  print(len(dataframe["lat_coor1"][1]))




