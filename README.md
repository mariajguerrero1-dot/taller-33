# Taller Evaluativo – Procesamiento de Archivos DICOM en Python
 Maria Jose Guerrero  


## 1. Descripción del proyecto
Este proyecto desarrolla una aplicación en Python para cargar archivos DICOM desde un directorio, extraer sus metadatos principales, calcular la intensidad promedio de las imágenes y organizar toda la información en un DataFrame. El objetivo es simular parte del funcionamiento básico de un sistema PACS.

## 2. Tecnologías utilizadas
- Python 3  
- pydicom  
- numpy  
- pandas  


## 4. Funcionamiento general

### 4.1 Carga de archivos DICOM
El programa recorre la carpeta `data/` y carga los archivos mediante `pydicom.dcmread()`. Los archivos no compatibles se ignoran para evitar errores.

### 4.2 Extracción de metadatos
Se obtienen los siguientes campos cuando están disponibles:
- PatientID  
- PatientName  
- StudyInstanceUID  
- StudyDescription  
- StudyDate  
- Modality  
- Rows  
- Columns  

Si alguno no existe, se guarda como `None`.

### 4.3 Cálculo de intensidad promedio
Usando `pixel_array`, se calcula el promedio de intensidad de los píxeles y se agrega como una nueva columna llamada `IntensidadPromedio`.

### 4.4 Exportación de resultados
Los datos se organizan en un DataFrame de Pandas y se guardan en:

resultado_metadatos.csv

## 5. Preguntas teóricas

### 5.1 Importancia de DICOM y HL7 en la interoperabilidad
DICOM es el estándar para almacenar y transmitir imágenes médicas e incluye tanto la imagen como sus metadatos.  
HL7 es un estándar para el intercambio de información clínica como datos del paciente, órdenes médicas o resultados.  
DICOM se enfoca en imágenes; HL7 en información textual. Ambos permiten que distintos sistemas de salud puedan comunicarse correctamente.

### 5.2 Relevancia clínica del análisis de intensidades
La distribución de intensidades ayuda a evaluar la calidad de la imagen (contraste, ruido), identificar tejidos y preparar la imagen para procesos como segmentación o modelos de aprendizaje automático. También permite detectar problemas en la adquisición.

### 5.3 Dificultades encontradas y utilidad de Python
Las dificultades más comunes son metadatos faltantes, archivos anonimizados y variaciones entre equipos.  
Python simplifica este trabajo gracias a pydicom, numpy y pandas, que permiten leer imágenes, analizar datos y organizarlos de forma eficiente.

## 6. Ejecución del proyecto

1. Instalar dependencias:
pip install -r requirements.txt

2. Colocar archivos `.dcm` en la carpeta `data/`.

3. Ejecutar:
python src/main.py
