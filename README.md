# Contexto del problema: 
Se requiere construir un modelo que sea capaz de predecir, dados los datos de síntomas de un paciente, si es posible o no que este sufra de alguna enfermedad. Esto se requiere tanto para enfermedades comunes (muchos datos) como para enfermedades huérfanas (pocos datos). 

Para el problema anterior, proponga un pipeline de ML en donde describa, de manera general, el proceso completo end-to-end para el desarrollo del modelo requerido.

Considerando el mismo problema, se necesita desarrollar un servicio que permita a un médico usar el modelo para obtener una respuesta

### Importante: 
Para reutilizar este pipeline en mi proyecto de grado, usare parte del codigo y datos de este para el desarollo, tratandose asi de una clasificacion de tumores. 

# Guia de uso:

## Instalacion 

1. Instalar Docker. 

recurso: https://docs.docker.com/engine/install/

2. Lanzar el sistema

estando en la carpeta root del proyecto, abra una terminal y ejecute el comando: docker-compose up -d 

Posterior a esto, se desplegaran automaticamente las aplicaciones de front y back-end.  


## Uso del producto

Entrar en el navegador a http://127.0.0.1:5000 para conectarse a la web app. 

Una vez dentro, encontrara 3 opciones desplegables, cada una indicando una funcion entre clasificar un archivo, varios, o reentrenar. Hasta ahora solo se ha desarrollado la de cargar un unico archivo. El resto estan fuera de servicio. 

Ahora puede proceder a cargar el archivo csv y probar on los datos que se encuentran en la carpeta data. 


# Pipeline

El pipeline recibe directamente archivos que pasaron anteriormente por una primera etapa de feature extraction. Estos archivos corresponden a datos radiomicos extraidos de resonancias magneticas de tumores cerebrales. Es por esta razon que no se puede evidenciar el frature extraction en el pipeline. El pipeline realizara un analisis de datos y procesamiento de tal forma que se puedan entrenar los modelos habiendo almacenado registros estadisticos sobre sus datos de entrenamiento. 

El entrenamiento se hara sobre los modelso random forest y XGBoost dinamicamente para determinar cual tienen mejores resultados especialmente en precision y recall. Luego se valida el modelo respecto a las metricas requeridas por el hospital, y luego el despliegue propuesto en esta entrega. 