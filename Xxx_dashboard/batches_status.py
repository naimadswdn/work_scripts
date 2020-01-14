import os
import sys
from datetime import datetime

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.split(current_directory)[0]
if sys.path.__contains__(parent_directory):
    # logger.info('Checking path to import dependent packages: Parent directory already in path')
    pass
else:
    # logger.info('Checking path to import dependent packages: Parent directory added to path')
    try:
        sys.path.append(parent_directory)
    except Exception as e:
        # logger.error(e)
        print(e)

from helpers.file_operations import read_file
from helpers.run_query_oracle import RunQueryOracle
from grafana.send_data import send_json, execute_query


def get_batch_status(inf_db):
    """
    Function responsible for collecting xxx load status data from xxx database.
    Function is removing old results and inserting new one to InfluxDB database each execution time.
    :inf_db: InfluxDB database name, that that will be written.
    :return:
    """
    login_directory = os.path.join(current_directory, 'login_data.txt')
    login_data = read_file(login_directory).read().splitlines()

    user = login_data[0]
    password = login_data[1]
    database = login_data[2]
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    run_query = RunQueryOracle(user, password, database)

    query_batch_status = """
    xxx
"""

    batch_status = run_query.select(query_batch_status)
    del batch_status[0]  # remove column names

    query = 'xxx'
    try:
        execute_query(inf_db, query)
        print('Clean up statement done!')
    except Exception as e:
        print(e)

    # send data
    for i in range(0, 4):
        json_body = [
            {
                "measurement": "{}".format('BATCH_STATUS'),
                "tags": {
                    "COUNTRY": "{}".format(batch_status[i][0]),
                    "POSITION_DATE": "{}".format(batch_status[i][1]),
                    "STATUS": "{}".format(batch_status[i][2])
                },
                "time": current_time,
                "fields": {
                    "value": str(batch_status[i][4])
                    # "value": str(11)
                }
            }
        ]
        print(json_body)
        try:
            send_json(inf_db, json_body, 'xxx policy', '1d')
        except Exception as e:
            print(e)


# get_batch_status('xxx')
