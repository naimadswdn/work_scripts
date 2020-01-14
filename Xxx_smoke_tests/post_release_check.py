import sys
import os
import time
import json

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

from helpers.run_query_mssql import RunQueryMssql
from helpers.file_operations import read_file, append_file
from helpers.send_mail_status import send_email_status
from helpers.date_related import last_business_day
from helpers.file_operations import load_configs
from helpers.logging_function import logger_function


def get_mssql_connection():
    """
    Function is loading configuration and opening MSSQL connection.
    :return: RunQueryMssql class
    """
    logger = logger_function(current_directory)
    config_file = os.path.join(current_directory, 'login.config')

    user = load_configs(config_file).get('login')
    password = load_configs(config_file).get('pass')
    server = load_configs(config_file).get('server')
    database = load_configs(config_file).get('database')

    try:
        mssql_connection = RunQueryMssql(user, password, server, database)
        logger.info(f'Connected to {server}\\{database} as {user}. ')
        return mssql_connection

    except Exception as e:
        logger.error(e)


def define_portfolio_list():
    """
    Function is loading portfolios list from json config.txt file.
    :return: dictionary loaded from config.txt file.
    """
    config = read_file(os.path.join(current_directory, 'config.txt'))
    result = json.loads(config.read())
    return result


def insert_run_ids():
    """
    Function is getting data from directory returned from define_portfolio_list function
    and then it prepare list of inserts to be executed on xxx MSSQL database.
    :return: List of inserts (strings) to be executed on xxx MSSQL database.
    """
    logger = logger_function(current_directory)

    portfolios = define_portfolio_list()
    logger.info(f'Portfolios in scope of test: {portfolios}')

    inserts_list = []
    previous_date = last_business_day().strftime("%Y-%m-%d") + " 00:00:00.000"
    logger.info(f'Valuation date is {previous_date}')

    for k, v in portfolios['user_request_portfolios'].items():
        for value in portfolios['user_request_portfolios'][k]:
            for analysis in ('xxx', 'xxx'):
                blotter = ''
                curve_list = ''
                if analysis == 'xx':
                    blotter = 'xxx'
                    curve_list = 'xxx'
                elif analysis == 'xxx':
                    blotter = 'xxx xx'
                    curve_list = 'xxx'
                system = ''
                if k == 'xx_Portfolios':
                    system = 'xxx@'
                elif k == 'xxx':
                    system = 'xxx@'
                insert = """xxx
                    """.format(blotter, value, analysis, system, curve_list, previous_date).replace('\n','').replace ('                    ', ' ')
                # print(insert)
                inserts_list.append(insert)
    return inserts_list


def insert_to_db(inserts):
    """
    Function is inserting runs generated by insert_run_ids function.
    Procedure sp_get_seed is called to generate new run_id, just like xx do.
    :param inserts: List of inserts generated by insert_run_ids function.
    :return: inserts list # dummy return
    """
    logger = logger_function(current_directory)
    logger.info('Inserting runs into database...')
    for element in inserts:
        logger.info(element)
        mssql = get_mssql_connection()
        mssql.insert_update(element)
        logger.info('Inserted --------------------------')
        sp_get_seed = """
            xxx
            """
        mssql.insert_update(sp_get_seed)
        logger.info('xxx procedure executed.')
    return inserts


def select_inserted_run_ids():
    """
    Function is querying xxx MSSQL database to get inserted run_ids.
    :return: List of run_ids
    """
    logger = logger_function(current_directory)
    sql_res = []
    previous_date = last_business_day().strftime("%Y-%m-%d") + " 00:00:00.000"
    select_run_ids = "xxx".format(previous_date)
    mssql = get_mssql_connection()
    result = mssql.select(select_run_ids)
    del result[0]
    for record in result:
        sql_res.append(str(record).replace('(', '').replace(')', '').replace(',', ''))
    logger.info(f'Scheduled run ids are: {sql_res}.')
    return sql_res


def relaunch_position(run_ids):
    """
    Function is executing xxx procedure to relaunch run_ids on Kronos MSSQL database.
    :param run_ids: List of run_ids generated by select_inserted_run_ids function.
    :return: List of relaunched run_ids # dummy return
    """
    logger = logger_function(current_directory)
    run_ids_list = []
    mssql = get_mssql_connection()
    for run_id in run_ids:
        temp = "exec xxx {}".format(run_id)
        run_ids_list.append(temp)
    for element in run_ids_list:
        mssql.insert_update(element)
        logger.info('Procedure run -------------------------- {}'.format(element))
    return run_ids_list


def wait_until_user_requests_finish(inserted_run_ids):
    """
    Function is waiting till all scheduled run are calculated.
    :param inserted_run_ids: List of run_ids generated by select_inserted_run_ids function.
    :return: Int value - if 1 then calculations are still ongoing, if 0 all runs were calculated already
    """
    logger = logger_function(current_directory)
    finished = 0
    mssql = get_mssql_connection()
    for i in inserted_run_ids:
        result = mssql.select(
            "xxx".format(i))
        del result[0]  # remove headers
        for record in result:
            r = (str(record).replace("(", "").replace(")", "").replace(",", ""))
            r = int(r)
            logger.info(f'Runs to calculate left: {str(r)}' + '\n' + "++++++++++++++++++")
            if r > 0:
                finished = finished + 1
    return finished


def get_results(analysis, blotter):
    """
    Function is getting results for last EOD and for User Requested runs for defined portfolios and analysis.
    After that results are saved to result.txt file.
    :param analysis: analysis name eg xxx, xx
    :param blotter: blotter type eg. xxx, xxx
    :return: 0 # dummy return
    """
    logger = logger_function(current_directory)
    previous_date = last_business_day().strftime("%Y-%m-%d") + " 00:00:00.000"
    mssql = get_mssql_connection()
    portfolios = define_portfolio_list()
    if blotter == 'xx':
        sql_part = "xxx"
    else:
        sql_part = ""
    for k, v in portfolios['xxx'].items():
        for value in portfolios['xx'][k]:
            sql_query = """
            xxx
            """.format(value, previous_date, analysis,blotter, sql_part)
            result = mssql.select(sql_query)
            logger.info(f'Query used to find results {sql_query}')
            del result[0]
            for record in result:
                append_file(os.path.join(current_directory, 'result.txt'), str(record) + '\n')
    return 0


def compare_results():
    """
    Function responsible for comparing results read from result.txt file.
    If discrepances are greater then 0,5 %, it return red highlighted html string.
    :return: html string that is going to be send as email with results
    """
    logger = logger_function(current_directory)
    result_html_string = '<b>xxx test results:</b> <br><br><table border="1"><th>Portfolio</th><th>Analysis</th><th>EOD value</th><th>Requested value</th><th>Persentage change</th>'
    discreptancies = 0
    result_file = read_file(os.path.join(current_directory, 'result.txt'))
    check_file = result_file.read().replace('None', '0').splitlines()

    for row in check_file:
        row = row.replace("(", "").replace(")", "").replace(",", "").split(' ')
        result_html_string = result_html_string + "<tr>"
        value1 = float(row[2])
        value2 = float(row[3])
        logger.info(f'EOD value: {value1}')
        logger.info(f'User request value: {value2}')
        try:
            change_percent = ((value1/value2)-1)*100
            change_percent = round(change_percent, 5)
        except ZeroDivisionError:
            change_percent = 0
        logger.info(f'Percentage change is : {change_percent}')
        logger.info(str(value1) + ' vs ' + str(value2))

        if change_percent > 0.5 or change_percent < -0.5:
            discreptancies = discreptancies + 1
            result_html_string = result_html_string + '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><font color="red"><b><td>{}</td></b>'\
                .format(row[0], row[1], row[2], row[3], change_percent)
        else:
            result_html_string = result_html_string + '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><font color="green"><td>{}</td>'.\
                format(row[0], row[1], row[2], row[3], change_percent)
    result_html_string = result_html_string + "</table><br><i>Overall {} discreptancies found</i>. Difference in value is more than 1 percent".format(discreptancies)

    return result_html_string


def main():
    """
    Function is calling all above functions in proper order.
    Responsible for establishing status (RED or GREEN) and sending email.
    :return: no return here.
    """
    logger = logger_function(current_directory)

    if os.path.exists(os.path.join(current_directory, 'result.txt')):
        os.remove(os.path.join(current_directory, 'result.txt'))
        logger.info('Old result file removed.')

    run_ids = insert_run_ids()
    insert_to_db(run_ids)
    runs_to_relaunch = select_inserted_run_ids()
    relaunch_position(runs_to_relaunch)

    while True:
        number = wait_until_user_requests_finish(runs_to_relaunch)
        if number == 0:
            break
        else:
            time.sleep(20)
            continue

    get_results('xx', 'xx')
    get_results('xx', 'xx')
    email = compare_results()

    sender = 'xx'
    receivers = ['xxx']
    # receivers = ['xxx']
    topic = 'xxx test results'

    if '0 discreptancies' in email:
        status = 'GREEN'
    else:
        status = 'RED'

    send_email_status(sender, receivers, topic, email, status=status)


main()