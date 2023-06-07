# Diccionario de datos

## 1. Datos del cliente del banco

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
|Age| Edad |numeric|
|Job        | Tipo de trabajo   |categorico         | 'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'
|Marital    | estado civil      |categorical        | 'divorced', 'married', 'single', 'unknown' ; note: 'divorced' means divorced or widowed
|Education  | Educación         |categorical        |'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown'
|Default    | Mora              | Tiene un crédito en mora?| categorical| Respuesta:'no', 'yes', 'unknown'
|Housing    | vivienda          |tiene prestamo de vivienda? |categorical | Respuesta:'no', 'yes', 'unknown'
|Loan       | prestamo          | tiene prestamo personal? |categorical | Respuesta:'no', 'yes', 'unknown'


## 2. Relacionado con el último contacto de la campaña actual:

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
|Contact| tipo de comunicación de contacto| categórico| 'celular', 'teléfono'
|Month| último mes de contacto del año |categórico| 'ene', 'feb', 'mar',…, 'nov', 'dec'
|Day_of_week| último día de contacto de la semana| categórico | 'lunes', 'martes', 'miércoles', 'jueves', 'vie'
|Duration| duración del último contacto, en segundos |numérico|


## 3. Contacto

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
|Campaign| número de contactos realizados durante esta campaña. incluye último contacto |numérico
|Pdays| número de días que pasaron después de que el cliente fue contactado por última vez de una campaña anterior. 999 significa que el cliente no fue contactado previamente (numérico)
|Previous| número de contactos realizados antes de esta campaña |numérico
|Poutcome| resultado de la campaña de marketing anterior |categórico |'fracaso', 'inexistente', 'éxito'

## 4. Atributos del Contexto Social y Economico

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
|Emp.var.rate|tasa de variación del empleo - indicador trimestral |numérico
|Cons.price.idx|índice de precios al consumidor - indicador mensual |numérico
|Cons.conf.idx| índice de confianza del consumidor - indicador mensual |numérico
|Euribor3m| tasa euribor 3 meses - indicador diario |numérico
|Nr.employed| número de empleados - indicador trimestral |numérico


## 5. Variable de salida (objetivo)

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
y | ¿El cliente ha suscrito un depósito a plazo? |binario|'sí', 'no'