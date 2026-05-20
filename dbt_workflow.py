import os
import subprocess

print("==================================================")
print("AIRFLOW SIMULATION: RUNNING DAG dbt_workflow")
print("==================================================\n")

# Path menuju project dbt lu
dbt_path = "C:/belajar_dbt_airflow/dbt_project/toko_elektronik"

print("TASK 1: Running dbt model...")
result_run = subprocess.run(f"cd {dbt_path} && dbt run", shell=True, capture_output=True, text=True)
print(result_run.stdout)

print("\nTASK 2: Running dbt test...")
result_test = subprocess.run(f"cd {dbt_path} && dbt test", shell=True, capture_output=True, text=True)
print(result_test.stdout)

print("\n==================================================")
print("DAG otomasi_dbt_toko_elektronik COMPLETED SUCCESSFULLY")
print("==================================================")