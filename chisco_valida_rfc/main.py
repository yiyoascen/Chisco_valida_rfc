import urllib.request
import pandas as pd
import argparse
from os import path
sat_url = 'http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv'


def getCSV(csvURL):
    urllib.request.urlretrieve(csvURL, 'listado.csv')


if __name__ == '__main__':
    if not path.exists("listado.csv"):
        getCSV(sat_url)
    parser = argparse.ArgumentParser()
    parser.add_argument("rfc")
    args = parser.parse_args()
    df = pd.read_csv('listado.csv')
    if args.rfc in df['Unnamed: 1'].values:
        informacion_del_rfc = [value for value in df.iloc[
            df['Unnamed: 1'].values == args.rfc].values][0]

        print('{} con rfc: {} aparece en la lista con el numero {}'.format(
            informacion_del_rfc[2], args.rfc, informacion_del_rfc[0]))
    else:
        print(args.rfc, "no aparece")
