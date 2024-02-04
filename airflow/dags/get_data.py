from datetime import datetime,timedelta
import subprocess

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


def _install_packages(package_list):
    for package in package_list: 
        try:
            subprocess.check_call(['pip3', 'install', package])
            print(f'Successfully install {package}')
        except subprocess.CalledProcessError:
            print(f'Error install {package}')
        except Exception as e:
            print(f'Something went wrong {e}')
            
    
def _get_data_covid(ti):
    packages_to_install = ['requests']
    _install_packages(packages_to_install)
    
    import requests
    
    api_url = 'http://103.150.197.96:5005/api/v1/rekapitulasi_v2/jabar/harian?level=kab'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()        
        ti.xcom_push(key="dataset", value=data["data"]["content"])
        return "get_data_covid"
    else:
        print(f"Request failed with status code: {response.status_code}")
        return "end"

with DAG(
    dag_id='final_project_keizia',
    start_date=datetime(2024, 2, 1),
    schedule_interval='0 0 * * *',
    catchup=False,
    default_args={
        'retries': 1,
        'retry_delay': timedelta(minutes=5)
    }
) as dag:

    start_task=EmptyOperator(
        task_id='start_task'
    )

    get_data_covid=PythonOperator(
        task_id='get_data_covid',
        python_callable=_get_data_covid,
        execution_timeout=timedelta(minutes=5)
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    start_task >> get_data_covid