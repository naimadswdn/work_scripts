from influxdb import InfluxDBClient
from datetime import datetime


def send_data(database, metric_name, tag, value, policy_name, policy_duration):
    client = InfluxDBClient(host='xxx')
    client.create_retention_policy(policy_name, policy_duration, '2', database)
    client.switch_database(database)
    current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    json_body = [
            {
                "measurement": "{}".format(metric_name),
                "tags": {
                    "tag": "{}".format(tag),
                },
                "time": current_time,
                "fields": {
                    "values": value,
                }
            }
        ]

    try:
        client.write_points(json_body)
    except Exception as e:
        print(e)


def send_json(database, json_data, policy_name, policy_duration):
    client = InfluxDBClient(host='xxx')
    client.create_retention_policy(policy_name, policy_duration, '2', database)
    client.switch_database(database)

    try:
        client.write_points(json_data)
    except Exception as e:
        print(e)


def execute_query(database, query):
    client = InfluxDBClient(host='xxx',)
    client.switch_database(database)

    try:
        client.query(query)
    except Exception as e:
        print(e)
