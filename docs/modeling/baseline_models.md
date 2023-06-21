# Reporte del Modelo Baseline

## Descripción del modelo

Como modelo base se considera una Regresión Logistica y será el punto de refererencia para el desarrollo de los próximos modelos.

## Variables de entrada

 * age            
 * job            
 * marital        
 * education      
 * default        
 * housing        
 * loan           
 * contact        
 * month          
 * day_of_week    
 * duration       
 * campaign       
 * pdays          
 * previous       
 * poutcome       
 * emp.var.rate   
 * cons.price.idx 
 * cons.conf.idx  
 * euribor3m      
 * nr.employed    


## Variable objetivo

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
y | ¿El cliente ha suscrito un depósito a plazo? |binario|'sí', 'no'

## Evaluación del modelo

* Se ha realizado una optimización de hiperparámetros a partir de Optuna
* Metrica a maximizar: f1_score 

### Métricas de evaluación

* accuracy
* f1_score
* recall

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

| Métrica | Valor |
| accuracy_score     | 89.81% | 
| f1_score     | 89.12% | 
| recall_score     | 86.71% | 

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

* Fortalezas
    - Con un modelo sencillo (regresión logística) se ha logrado obtener buenos resultados.

    - Es modelo que permite identificar la contribución de cada feature de forma sencilla a diferencia de los modelos tipo "caja negra".

* Debilidades
    - Se podría obtener mejores resultados utilizando modelos más elaborados (no lineales).

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora

- Fue necesario realizar un ajuste a los datos por estar desbalanceados (La clase minoritaria tiene inicialmente un 11.3%)
- Se realizó una transformación de todos los features (numéricas y categóricas)

- Para lograr mejores resultados se realizó una optimización de parámetros con Optuna.
lograndose mejorar el f1_score de 89.03% a 89.12%.

## Referencias

* Regresion logistica: Modelo inicial

* Optuna: librería para optimizar parámetros (f1_score). https://optuna.org/

* f1_score: métrica considerada para evaluar el rendimiento y realizar la optimización. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

