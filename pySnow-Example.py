import pysnow
from pysnow import exceptions
from datetime import datetime
from configparser import ConfigParser

# snow api ref: https://developer.servicenow.com/app.do#!/rest_api_doc?v=jakarta&id=c_TableAPI
# pysnow library ref: https://github.com/rbw0/pysnow
# pysnow documentation: https://media.readthedocs.org/pdf/pysnow/latest/pysnow.pdf


# globals

INSTANCE = 'datapipeuat'
USER = 'EM7'
PASSWORD = 'developer'
API_PATH_INCIDENT = '/table/incident'


def snow_get_incident(number):

    # Create client object

    c = pysnow.Client(instance=INSTANCE, user=USER, password=PASSWORD)

    # Define resource, here we will use the incident table API

    incident = c.resource(api_path=API_PATH_INCIDENT)

    # Query for incident with number X
    # INC1088598
    # response = incident.get(query={'number': number})

    try:
        # response = incident.get(query={'state': 1})
        response = incident.get(query={'number': number})
    except exceptions.MultipleResults:
        print 'Multiple Records'
        return None

    return response.one_or_none()


def snow_create_incident(new_record):
    """
    This method calls pysnow.Resource.one() if the record was created successfully,
    returning a dictionary of the created record.
    """

    # Create client object
    c = pysnow.Client(instance=INSTANCE, user=USER, password=PASSWORD)

    # Define a resource, here we'll use the incident table API
    incident = c.resource(api_path='/table/incident')

    # Create a new incident record
    result = incident.create(payload=new_record)

    return result


def main():

    parser = ConfigParser()
    # parser.read_file('dev.ini')
    parser.read(u'dev.ini')

    print 'sections: {}'.format(parser.sections())
    print 'username: {}'.format(parser.get('snow_credentials', 'username'))

    db_port = parser.getint('mysql_credentials', 'db_port', fallback=7706)

    print 'db_port: {} - type: {}'.format(db_port, type(db_port))

    exit()

    incident = snow_get_incident('INC1088598')
    if incident is not None:
        print 'sys_id: {} - company: {}'.format(incident['sys_id'], incident['company'])

    new_record = {
        'short_description': 'Test Incident - {}'.format(datetime.now()),
        'description': 'Testing Table API'
    }

    incident = snow_create_incident(new_record)

    if incident is not None:
        print 'number: {} - sys_id: {} - company: {}'\
            .format(incident['number'], incident['sys_id'], incident['company'])


if __name__ == "__main__":
    main()

