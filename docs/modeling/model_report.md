# Reporte del Modelo Final

## Resumen Ejecutivo

Se ha comparado el modelo base utilizando la busqueda de hiperparametros con optuna con respecto al modelo final donde se ha realizado la busqueda de hiperparametros con gridsearch; en este momento el modelo base presenta un comportamiento ligeramente superior al modelo final, se espera mejorar este desface para la siguiente entrega.

## Descripción del Problema

El objetivo es predecir si un cliente de una institución bancaria portuguesa aceptará atraves de una llamada telefonica un prestamo a largo plazo. Se intento utilizar un modelo no lineal para medir su comportamiento en contra del modelo base que corresponde a un modelo de regresion logistica. 

## Descripción del Modelo

Se implemento un modelo de bosques aleatorios y con la ayuda de grid search se buscaron sus mejores hiperparametros.

## Evaluación del Modelo

En esta sección se presentará una evaluación detallada del modelo final. 
Se deben incluir las métricas de evaluación que se utilizaron y una interpretación detallada de los resultados.

* Se ha realizado una optimización de hiperparámetros a partir de Optuna y GridSearch los cuales fueron comparados con los resultados del modelo base.
* Metrica a maximizar: f1_score 

Métricas Finales Optimizadas

Resultados Optuna

| Métrica | Valor |
| accuracy_score     | 89.81% | 
| f1_score     | 89.12% | 
| recall_score     | 86.71% | 


Resultados GridSearch

| Métrica | Valor |
| accuracy_score     | 99.66% | 
| f1_score     | 90.13% | 
| recall_score     | 88.59% | 

## Conclusiones y Recomendaciones
Por la prescencia de un desbalanceo de clases es necesario evaluar el f1_score.

* Puntos Fuertes
    - De todos los modelos propuestos se ha logrado los mejores resultados utilizando GridSearch para un RandomForest.

* Puntos Débiles
    - Para lograr los mejores resultados es necesario un mayor tiempo de procesamiento.
    
En esta sección se presentarán las conclusiones y recomendaciones a partir de los resultados obtenidos. Se deben incluir los puntos fuertes y débiles del modelo, las limitaciones y los posibles escenarios de aplicación.

## Referencias

En esta sección se deben incluir las referencias bibliográficas y fuentes de información utilizadas en el desarrollo del modelo.

* https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
* https://optuna.org/
* https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
* https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing?resource=download