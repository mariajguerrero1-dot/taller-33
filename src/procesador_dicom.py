import os
import pydicom
import pandas as pd
import numpy as np

class ProcesadorDICOM:
    def __init__(self, ruta_directorio):
        self.ruta = ruta_directorio
        self.dicoms = []
        self.df = pd.DataFrame()

    def cargar_dicoms(self):
        archivos = os.listdir(self.ruta)
        for archivo in archivos:
            ruta_archivo = os.path.join(self.ruta, archivo)
            try:
                ds = pydicom.dcmread(ruta_archivo)
                self.dicoms.append(ds)
            except Exception:
                pass

    def extraer_metadatos(self):
        registros = []
        for ds in self.dicoms:
            registros.append({
                "PatientID": getattr(ds, "PatientID", None),
                "PatientName": getattr(ds, "PatientName", None),
                "StudyInstanceUID": getattr(ds, "StudyInstanceUID", None),
                "StudyDescription": getattr(ds, "StudyDescription", None),
                "StudyDate": getattr(ds, "StudyDate", None),
                "Modality": getattr(ds, "Modality", None),
                "Rows": getattr(ds, "Rows", None),
                "Columns": getattr(ds, "Columns", None)
            })
        self.df = pd.DataFrame(registros)

    def calcular_intensidad_promedio(self):
        intensidades = []
        for ds in self.dicoms:
            try:
                img = ds.pixel_array
                intensidades.append(np.mean(img))
            except:
                intensidades.append(None)
        self.df["IntensidadPromedio"] = intensidades

    def ejecutar(self):
        self.cargar_dicoms()
        self.extraer_metadatos()
        self.calcular_intensidad_promedio()
        return self.df
