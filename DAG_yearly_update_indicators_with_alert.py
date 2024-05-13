from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Función para enviar correo electrónico de alerta
def send_alert_email(context, **kwargs):
    subject = "Alerta: DAG ejecutado sin éxito"
    html_content = f"""
    <h3>El DAG {context['task_instance'].dag_id} ha fallado</h3>
    <p>Fecha de ejecución: {context['execution_date']}</p>
    <p>Tarea fallida: {context['task_instance'].task_id}</p>
    """
    send_email('jorgeaga2408@hotmail.com', subject, html_content)

# Define la función para calcular y actualizar los agregados anuales
def actualizar_agregados_anuales():
    # Consultar los datos diarios de la tabla principal
    query = """
    SELECT 
        YEAR(date) AS year,
        NAME AS name,
        AVG(open) AS avg_open,
        AVG(high) AS avg_high,
        AVG(low) AS avg_low,
        AVG(close) AS avg_close,
        AVG(volume) AS avg_volume,
        SUM(volume) AS tot_volume
    FROM 
        public.all_stocks
    GROUP BY 
        YEAR(date),
        NAME
    """
    daily_data = snowflake_hook.get_pandas_df(query)

    # Cargar los resultados en la tabla de agregados anuales
    daily_data.to_sql("avg_indicators_per_year", con=snowflake_engine, schema="public", if_exists="replace", index=False)
    print("Agregados anuales del S&P 500 actualizados exitosamente en Snowflake.")

# Define los argumentos por defecto del DAG
default_args = {
    'owner': 'jaga2408',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['jorgeaga2408@hotmail.com']
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 5, 13),
}

# Define el DAG
dag = DAG(
    'actualizacion_agregados_anuales_sp500',
    default_args=default_args,
    description='Actualización anual de agregados del S&P 500 en Snowflake',
    schedule_interval=timedelta(days=365),  # Ejecutar una vez al año
)

# Define el operador para calcular y actualizar los agregados anuales
actualizar_agregados = PythonOperator(
    task_id='actualizar_agregados_anuales',
    python_callable=actualizar_agregados_anuales,
    dag=dag,
)

# Define la secuencia de tareas del DAG
actualizar_agregados_anuales
