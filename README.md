<h1 align="center"> Challenge DE: Desarrollo de proyecto end-to-end </h1>

A continuación se detallan las instrucciones para la ejecución del proyecto end-to-end que generan insights para la empresa ACME.

1. Primeramente se creó la estructura de la tabla principal llamada all_stocks, la cual contendrá el histórico diario de los indicadores correspondientes al S&P500. El DDL de
   la tabla se encuentra en el archivo llamado "create_table_all_stocks" que se encuentra en este repositorio.
2. Una vez creada la tabla se debe cargar la información proporcionada en el dataset S&P500, el cual se puede encontrar en el siguiente link: https://www.kaggle.com/datasets/camnugent/sandp500
3. Posteriormente se crearon dos tablas agregadas: i. avg_indicators_per_month - contiene los promedios mensuales de los indicadores y ii. avg_indicators_per_year - contiene los promedios
   anuales de los indicadores. Los DDL's de las tablas se encuentran en los archivos "create_table_avg_indicators_per_month" y "create_table_avg_indicators_per_year" respectivamente, los cuales
   se encuentran en este repositorio.
4. Tanto la tabla principal como las dos tablas agregadas se actualizarán mediante DAG's de Airflow, el código de los DAG's se encuentra en los siguientes archivos:
   
   I. DAG_daily_update_indicators.py
   
   II. DAG_monthly_update_indicators.py
   
   III. DAG_yearly_update_indicators.py
   
   Estos DAG's son simples, es decir, no cuentan con monitorización y notificación de fallo.
   
5. Si se desea implementar los DAG's con monitorización y notificación de fallo via email, se deben ocupar los siguientes archivos:
   
   I. DAG_daily_update_indicators_with_alert.py
   
   II. DAG_monthly_update_indicators_with_alert.py
   
   III. DAG_yearly_update_indicators_with_alert.py
   
   Estos DAG's contienen el código necesario para enviar un email que notifica el fallo de la ejecución via email.

6. Finalmente para poder obtener insights sobre los indicadores, se agregaron dos consultas en lengiaje SQL que se pueden ejecutarse directamente en Snowflake, las consultas
   se encuentran en el archivo llamado "Consultas_SQL_Insights" que al igual que los demàs archivos se encuentra en este repositorio.

7. La liga de la instancia en Snowflake donde se encuentran las tablas antes explicadas es la siguiente: https://app.snowflake.com/east-us-2.azure/qda17191/#/data/databases/SP_500

8. Finalmente la documentación para la configuración de la infraestructura y la integración de Snowflake y Airflow con Azure se encuentra en el archivo "Configuraciòn de Azure, Snowflake y Airflow".
   

