def cargar_mapa(nombre_mapa): #Lee un documento .txt  lo convierte en una matriz
	mapa_doc = open(nombre_mapa, "r")
	mapa = []
	for i in mapa_doc:
		mapa.append(list(i.strip()))
	mapa_doc.close()

	return mapa

def cargar_instrucciones(nombre_instrucciones): #Lee un documento .txt con las instrucciones
	instrucciones_doc = open(nombre_instrucciones, "r")
	instrucciones = []
	for j in instrucciones_doc:
		instrucciones.append(j.strip())
	instrucciones_doc.close()

	return instrucciones