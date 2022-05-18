import orjson
from src.profiles.observationHowDeathInjuryOccurred import generateObservationHowDeathInjuryOccurred
import uuid
from fhirgenerator.helpers.helpers import default


def testObservationHowDeathInjuryOccurred():
    patient_id = '26774-827647-736278-3737646'
    performer_id = str(uuid.uuid4())
    start_date = '01-01-2022'
    days = 1
    howDeathInjuryOccurredList = [
        "was being haunted",
        "ingested all sorts of stuff",
        "wind surfing",
        "regular surfing (not wind)",
        "apple picking",
        "attended an overly enthusiastic murder mystery party",
        "being a jerk to Fred",
        "attending a talk show taping"
    ]
    resource = generateObservationHowDeathInjuryOccurred(howDeathInjuryOccurredList, patient_id, performer_id, start_date, days)

    with open(f'tests/output/test_observation_how_death_injury_event_occurred.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
