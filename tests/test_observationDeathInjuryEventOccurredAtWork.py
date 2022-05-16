import orjson
from src.profiles.observationDeathInjuryEventOccurredAtWork import generateObservationDeathInjuryEventOccurredAtWork
import uuid
from fhirgenerator.helpers.helpers import default


def testObservationDeathInjuryEventOccurredAtWork():
    patient_id = '26774-827647-736278-3737646'
    performer_id = str(uuid.uuid4())
    start_date = '01-01-2022'
    days = 1

    resource = generateObservationDeathInjuryEventOccurredAtWork(patient_id, performer_id, start_date, days)

    with open(f'tests/output/test_observation_death_injury_event_occurred_at_work.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
