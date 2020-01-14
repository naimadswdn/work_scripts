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


def get_fpml_status(inf_db):
    """
    Function responsible for collecting xx fmpl that need to be received yet from xx.
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

    query_fpml_status = """xxx
"""

    fpml_status = run_query.select(query_fpml_status)
    del fpml_status[0]  # remove column names


    # send data
    for i in range(0, 2):
        json_body = [
            {
                "measurement": "{}".format('FPML_STATUS'),
                "tags": {
                    "WHAT": "{}".format(fpml_status[i][0]),

                },
                "time": current_time,
                "fields": {
                    "value": str(fpml_status[i][1])
                    # "value": str(11)
                }
            }
        ]
        print(json_body)
        try:
            send_json(inf_db, json_body, 'xx_policy', '1d')
        except Exception as e:
            print(e)


# get_fpml_status('xxx')
