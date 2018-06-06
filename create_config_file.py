from configparser import ConfigParser


def create_config():

    config = ConfigParser()

    # Create Sections

    config['mysql_credentials'] = {
        'db_username': 'root',
        'db_password': 'em7admin',
        'db_port': 7706,
        'db_timeout': 1000
    }

    config['snow_credentials'] = {
        'username': 'em7',
        'password': 'developer'
    }

    with open('./dev.ini', 'w') as f:
        config.write(f)


create_config()
