# coding=utf-8
import utm
import pandas as pd
import math

def createJson():

    
    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8', dtype=object))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8', dtype=object))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8', dtype=object))
    result = pd.concat(general)
    posarComa=False
    fout= open("bombesTotes.js", 'w')
    fout.write('var bombes = {\n')
    fout.write('  "type": "FeatureCollection",\n')
    fout.write('  "features": [\n')
    for index, info in result.iterrows(): 
        if not '??' in info["COORDENADES"].encode('utf-8'):
            if posarComa:
                fout.write(',\n')
            posarComa=True
            fout.write('    {\n')
            fout.write('      "type": "Feature",\n')
            fout.write('      "properties": {\n')
            fout.write('        "avio": "'+str(info["AVIO"])+'",\n')
            if isinstance(info["CARRER"], float):
                fout.write('        "carrer": "'+str(info["CARRER"]).encode('utf-8')+'",\n')
            else:
                fout.write('        "carrer": "'+info["CARRER"].encode('utf-8')+'",\n')
            fout.write('        "unitat": "'+info["UNITAT"].encode('utf-8')+'",\n')
            #algo = tipus[i][info["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
            #fout.write('        "causes": "'+str(algo)+'",\n')
           
            
            fout.write('        "morts": "'+str(info["MORTS"])+'",\n')
            fout.write('        "ferits": "'+str(info["FERITS"])+'",\n')
            fout.write('        "hora": "'+str(info["HORA"])+'",\n')
            fout.write('        "data": "'+ "%02d" % ( int(info["DIA"]), )+"-"+ "%02d" % (int(info["MES"]),)+'-'+str(info["ANY"])+'"\n')
            fout.write('      },\n')
            fout.write('      "geometry": { \n')
            fout.write('        "type":"Point",\n')
            try:
                fout.write('        "coordinates":['+info["COORDENADES"] +']\n')
            except:
                print info["COORDENADES"]
            fout.write('      }\n')
            fout.write('    }')
    fout.write('\n  ]\n')
    fout.write('}\n')
    fout.close()
def algo(x):
    if math.isnan(float(x)):
        print 'ei'
        return str(99)
    return str(x)
def algoInt(x):
    if math.isnan(float(x)):
        print 'ei'
        return 99
    return int(x)
def createJS():

    
    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8'))
    result = pd.concat(general)
    result["DIA"] = result.DIA.map("{:02}".format)
    result["MES"] = result.MES.map("{:02}".format)
    result["ANY"] = result.ANY.map(algoInt)
    result['data']=result["ANY"].map(algo)+''+result["MES"].map(algo)+''+result["DIA"].map(algo)
    result.sort_values(by='data', ascending=False)
    dates=result.groupby(['data'])['data']
    print dates
    fout= open("bombes.js", 'w')
    for data in dates.groups:
        posarComa=False
        fout.write('var dia'+str(data)+' = {\n')
        fout.write('  "type": "FeatureCollection",\n')
        fout.write('  "features": [\n')
        
        for index, info in result[result['data'] == data].iterrows(): 
            if not '??' in info["COORDENADES"].encode('utf-8'):
                if posarComa:
                    fout.write(',\n')
                posarComa=True
                fout.write('    {\n')
                fout.write('      "type": "Feature",\n')
                fout.write('      "properties": {\n')
                fout.write('        "avio": "'+str(info["AVIO"])+'",\n')
                if isinstance(info["CARRER"], float):
                    fout.write('        "carrer": "'+str(info["CARRER"]).encode('utf-8')+'",\n')
                else:
                    fout.write('        "carrer": "'+info["CARRER"].encode('utf-8')+'",\n')
                fout.write('        "unitat": "'+info["UNITAT"].encode('utf-8')+'",\n')
                #algo = tipus[i][info["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
                #fout.write('        "causes": "'+str(algo)+'",\n')
               
                
                fout.write('        "morts": "'+str(info["MORTS"])+'",\n')
                fout.write('        "ferits": "'+str(info["FERITS"])+'",\n')
                fout.write('        "hora": "'+str(info["HORA"])+'",\n')
                fout.write('        "data": "'+ str(info["DIA"])+"-"+ str(info["MES"])+'-'+str(info["ANY"])+'"\n')
                fout.write('      },\n')
                fout.write('      "geometry": { \n')
                fout.write('        "type":"Point",\n')
                try:
                    tmp=str(info["COORDENADES"]).split(',')

                    fout.write('        "coordinates":['+tmp[1]+','+tmp[0] +']\n')
                except:
                    print info["COORDENADES"]
                fout.write('      }\n')
                fout.write('    }')
    fout.write('\n  ]\n')
    fout.write('};\n')
    fout.close()
def createJSMulti():

    
    general=[]
    i="3"

    general.append(pd.read_csv("geolocalització bombes - 1937.csv",sep=',',na_values='', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1938.csv",sep=',', na_values = '', encoding='utf8'))
    general.append(pd.read_csv("geolocalització bombes - 1939.csv",sep=',', na_values='', encoding='utf8'))
    result = pd.concat(general)
    result["DIA"] = result.DIA.map("{:02}".format)
    result["MES"] = result.MES.map("{:02}".format)
    result["ANY"] = result.ANY.map(algoInt)
    result['data']=result["ANY"].map(algo)+''+result["MES"].map(algo)+''+result["DIA"].map(algo)
    result.sort_values(by='data', ascending=False)
    dates=result.groupby(['data'])['data']
    print dates
    fout= open("bombesMulti.js", 'w')
    for data in dates.groups:
        posarComa=False
        fout.write('var dia'+str(data)+' = {\n')
        fout.write('  "type": "FeatureCollection",\n')
        fout.write('  "features": [\n')
        dataInfo=result[result['data'] == data]
        
        fout.write('    {\n')
        fout.write('      "type": "Feature",\n')
        fout.write('      "properties": {\n')
        fout.write('        "avio": "'+str(dataInfo["AVIO"].iloc[0])+'",\n')
        if isinstance(dataInfo["CARRER"].iloc[0], float):
            fout.write('        "carrer": "'+str(dataInfo["CARRER"].iloc[0]).encode('utf-8')+'",\n')
        else:
            fout.write('        "carrer": "'+dataInfo["CARRER"].iloc[0].encode('utf-8')+'",\n')
        fout.write('        "unitat": "'+dataInfo["UNITAT"].iloc[0].encode('utf-8')+'",\n')
        #algo = tipus[i][dataInfo(0["Numero dexpedient"]== tipus[i]["Numero dexpedient"]]["Descripcio tipus accident"].iloc(0)
        #fout.write('        "causes": "'+str(algo)+'",\n')
       
        
        fout.write('        "morts": "'+str(dataInfo["MORTS"].iloc[0])+'",\n')
        fout.write('        "ferits": "'+str(dataInfo["FERITS"].iloc[0])+'",\n')
        fout.write('        "hora": "'+str(dataInfo["HORA"].iloc[0])+'",\n')
        fout.write('        "data": "'+ str(dataInfo["DIA"].iloc[0])+"-"+ str(dataInfo["MES"].iloc[0])+'-'+str(dataInfo["ANY"].iloc[0])+'"\n')
        fout.write('      },\n')
        fout.write('      "geometry": { \n')
        fout.write('        "type":"MultiPoint",\n')
        fout.write('        "coordinates":[')
        for index, info in result[result['data'] == data].iterrows(): 
            if not '??' in info["COORDENADES"].encode('utf-8'):
                if posarComa:
                    fout.write(', ')
                posarComa=True
                try:
                    tmp=str(info["COORDENADES"]).split(',' )
                    fout.write('['+tmp[1]+','+tmp[0] +']')
                except:
                    print str(info["COORDENADES"])
                    posarComa=False
        fout.write(']\n      }\n')
        fout.write('    }')            
        fout.write('\n  ]\n')
        fout.write('};\n')
    fout.close()
createJson()
createJS()
createJSMulti()