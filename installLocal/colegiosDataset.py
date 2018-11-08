# -*- coding: utf-8 -*-
"""colegiosDataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/128lwOS7PTPDcjVH9NPN33hv2WVS2whwP
"""

import pandas as pd
import sys
from hdfs3 import HDFileSystem

reload(sys)
sys.setdefaultencoding('utf-8')

hdfs = HDFileSystem(host='sandbox-hdp.hortonworks.com', port=8020)

inpath=sys.argv[1]
oupath=sys.argv[2]

# Cargamos nuestro dataset
with hdfs.open(inpath) as f:
    df = pd.read_csv(f, sep=';', encoding = 'ISO-8859-1')

# Eliminamos columnas que no vamos a necesitar
df = df.drop(['DESCRIPCION-ENTIDAD', 'HORARIO', 'EQUIPAMIENTO', 'ACCESIBILIDAD', 'CONTENT-URL', 'PLANTA', 'PUERTA', 'ESCALERAS', 'LOCALIDAD', 'PROVINCIA',
              'ORIENTACION', 'TELEFONO', 'FAX', 'EMAIL', 'TIPO', 'Unnamed: 30'], axis=1)


# Cambiamos caracteres con acentes
df = df.replace({'á': 'a'}, regex=True)
df = df.replace({'é': 'e'}, regex=True)
df = df.replace({'í': 'i'}, regex=True)
df = df.replace({'ó': 'o'}, regex=True)
df = df.replace({'ú': 'u'}, regex=True)


# Borramos aquellas filas que en el campo Nombre están vacías
data = df.loc[df['NOMBRE'] != '']


# Exportamos dataframe a fichero .csv
with hdfs.open(oupath) as f:
    data.to_csv(f, sep=';', encoding='utf-8', index=False)


