import argparse
import pandas as pd

def partsParser(path):

    keys_template = ['ImporterAccount','FilerCode','PartNumber','Description','Country','UnitPrice','IsDutyExempt','IsDutyReduced','IsMPFExempt','IsOtherFeesExempt','Tariff #','UnitsShipped','UnitsShipped2','UnitsShipped3','SI','SI2','SICountry','Value','CountryOfOrigin','IsGlobalPart','ZoneStatus','PrivilegedFilingDate','PGA AGENCY','AGENCY PROGRAM CODE','AGENCY PROCESSING CODE','PRODUCT CODE  QUALIFIER','PRODUCT CODE NUMBER','PACKAGING QUALIFIER 1','UNIT OF MEASURE 1','PACKAGING QUALIFIER 2','UNIT OF MEASURE 2', 'PACKAGING QUALIFIER 3', 'UNIT OF MEASURE 3', 'PACKAGING QUALIFIER 4', 'UNIT OF MEASURE 4', 'PACKAGING QUALIFIER 5', 'UNIT OF MEASURE 5', 'PACKAGING QUALIFIER 6', 'UNIT OF MEASURE 6','PGA Disclaim Code','Manufacturer','PartAlias']

    try:
        parts_download = pd.read_excel(f'files/{path}')
    except:
        print(f'Error loading file {path}, please check the correct file name and file extension to be .xlsx')
        print(f'Also remember to use files in the files/ folder only')
        return 0
    
    parts_download.rename(columns={
        'Tariff' : 'Tariff #',
        'IsGlobal' : 'IsGlobalPart',
        'PrivilegedStatusFilingDate' : 'PrivilegedFilingDate',
        'UOM' : 'UNIT OF MEASURE 1'
    }, inplace=True)

    #Method to change the bool list display to be 0 or 1 depending on false or true
    parts_download['IsGlobalPart'] = [int(x) for x in parts_download['IsGlobalPart']]

    result_df = pd.DataFrame(columns=keys_template)

    for column in keys_template:

        if column in parts_download.columns:
            result_df[column] = parts_download[column]

    result_df.to_excel('output/parts_converted.xlsx', index=False)

    print('File saved under output/parts_converted.xlsx')
    return 1


parser = argparse.ArgumentParser(description='Process an .xlsx file for parts.')
parser.add_argument('path', type=str, help='Path of the xlsx file to process')
args = parser.parse_args()

partsParser(args.path)