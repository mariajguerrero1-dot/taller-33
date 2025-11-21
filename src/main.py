from procesador_dicom import ProcesadorDICOM

ruta = "./data"

procesador = ProcesadorDICOM(ruta)
df = procesador.ejecutar()

print(df)
df.to_csv("resultado_metadatos.csv", index=False)
