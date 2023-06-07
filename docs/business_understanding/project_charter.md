# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Mercadotecnica Bancaria

## Objetivo del Proyecto

El objetivo es predecir si un cliente de una institución bancaria portuguesa aceptará atraves de una llamada telefonica un prestamo a largo plazo.

## Alcance del Proyecto

### Incluye:

El dataset contiene información relacionada con campañas de marketing directo de una institución bancaria portuguesa basadas en llamadas telefónicas, donde se les ofrecia a los clientes credito a largo plazo.

Información de las variables independiente:

Edad (numérico)

Trabajo : tipo de trabajo (categóricos: 'admin.', 'cuello azul', 'emprendedor', 'criada', 'gerencia', 'jubilado', 'autónomo', 'servicios', 'estudiante', ' técnico', 'desempleado', 'desconocido')

Civil: estado civil (categórico: 'divorciado', 'casado', 'soltero', 'desconocido'; nota: 'divorciado' significa divorciado o viudo)

Educación (categórico: 'básico.4 años', 'básico.6 años', 'básico.9 años', 'bachillerato', 'analfabeto', 'curso.profesional', 'título.universitario', 'desconocido')

Mora: ¿tiene crédito en mora? (categórico: 'no', 'sí', 'desconocido')

Vivienda: tiene préstamo de vivienda? (categórico: 'no', 'sí', 'desconocido')

Préstamo: tiene préstamo personal? (categórico: 'no', 'sí', 'desconocido')

Contacto: tipo de comunicación de contacto (categórico: 'celular', 'teléfono')

Mes: último mes de contacto del año (categóricos: 'ene', 'feb', 'mar', …, 'nov', 'dec')

Day_of_week: último día de contacto de la semana (categórico: 'lunes', 'martes', 'miércoles', 'jueves', 'vie')

Duración: duración del último contacto, en segundos (numérico). Nota importante : este atributo afecta en gran medida el objetivo de salida (por ejemplo, si la duración = 0 entonces y = 'no'). Sin embargo, la duración no se conoce antes de que se realice una llamada. Además, después del final de la llamada y es obviamente conocido. Por lo tanto, esta entrada solo debe incluirse con fines de referencia y debe descartarse si la intención es tener un modelo predictivo realista.

Campaña: número de contactos realizados durante esta campaña y para este cliente (numérico, incluye último contacto)

Pdays: número de días que pasaron después de que el cliente fue contactado por última vez de una campaña anterior (numérico; 999 significa que el cliente no fue contactado previamente)

Anterior: número de contactos realizados antes de esta campaña y para este cliente (numérico)

Poutcome: resultado de la campaña de marketing anterior (categórico: 'fracaso', 'inexistente', 'éxito')

Emp.var.rate: tasa de variación del empleo - indicador trimestral (numérico)

Cons.price.idx: índice de precios al consumidor - indicador mensual (numérico)

Cons.conf.idx: índice de confianza del consumidor - indicador mensual (numérico)

Euribor3m: tasa euribor 3 meses - indicador diario (numérico)

Nr.ocupados: número de empleados - indicador trimestral (numérico)

y - ¿El cliente ha suscrito un depósito a plazo? (binario: 'sí', 'no')

### Excluye:

- El alcance de este proyecto es construir un modelo de machine learning que sea capaz de ayudar al banco portugues a predecir si un cliente tomará un credito a largo plazo mediante una llamada telefonica.

## Metodología

Team Data Science Process

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 30 de mayo al 6 de junio |
| Preprocesamiento, análisis exploratorio | 1 semanas | del 6 de mayo al 13 de junio |
| Modelamiento y extracción de características | 1 semanas | del 14 de junio al 20 de junio |
| Despliegue | 1 semanas | del 21 de junio al 27 de junio |
| Evaluación y entrega final | 3 semanas | del 28 de junio al 19 de julio |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- Luis Rey Sanchez
- Christian España

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
