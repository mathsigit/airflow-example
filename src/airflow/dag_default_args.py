import datetime as dt

default_args = {
    'owner': 'someone', # DAG 擁有者的名稱，如上一篇說明的，通常是負責實作這個 DAG 的人員名稱
    'depends_on_past': False, # 每一次執行的 Task 是否會依賴於上次執行的 Task，如果是 False 的話，代表上次的 Task 如果執行失敗，這次的 Task 就不會繼續執行
    'start_date': dt.datetime(2020, 2, 24), # Task 從哪個日期後開始可以被 Scheduler 排入排程
    'email': ['stana@is-land.com.tw'], # 如果 Task 執行失敗的話，要寄信給哪些人的 email
    'email_on_failure': True, # 如果 Task 執行失敗的話，是否寄信
    'email_on_retry': True, # 如果 Task 重試的話，是否寄信
    'retries': 1, # 最多重試的次數
    'retry_delay': dt.timedelta(minutes=5) # 每次重試中間的間隔
    # 'end_date': datetime(2020, 2, 29), # Task 從哪個日期後，開始不被 Scheduler 放入排程
    # 'execution_timeout': timedelta(seconds=300), # Task 執行時間的上限
    # 'on_failure_callback': some_function, # Task 執行失敗時，呼叫的 function
    # 'on_success_callback': some_other_function, # Task 執行成功時，呼叫的 function
    # 'on_retry_callback': another_function, # Task 重試時，呼叫的 function
}