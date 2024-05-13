from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Define la función para actualizar los datos del S&P 500
def actualizar_datos_sp500():
    # Descargar datos del S&P 500 usando Yahoo Finance
    sp500 = yf.download('^GSPC', start=datetime.now()-timedelta(days=1), end=datetime.now())
    
    # Cargar los datos en Snowflake
    sp500.to_sql("sp500_daily", con=snowflake_engine, schema="public", if_exists="append", index=True)
    print("Datos del S&P 500 actualizados exitosamente en Snowflake.")

# Define los argumentos por defecto del DAG
default_args = {
    'owner': 'jaga2408',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 5, 13),
}

# Define el DAG
dag = DAG(
    'actualizacion_sp500_diaria',
    default_args=default_args,
    description='Actualización diaria de datos del S&P 500 en Snowflake',
    schedule_interval=timedelta(days=1),
)

# Define el operador para actualizar los datos del S&P 500 en Snowflake
actualizar_sp500 = PythonOperator(
    task_id='actualizar_sp500',
    python_callable=actualizar_datos_sp500,
    dag=dag,
)

# Define la secuencia de tareas del DAG
actualizar_sp500
