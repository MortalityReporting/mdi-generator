import orjson
from src.profiles.observationCauseOfDeathCondition import generateObservationCauseOfDeathCondition
import uuid
from fhirgenerator.helpers.helpers import default


def testObservationCauseOfDeathCondition():
    patient_id = '26774-827647-736278-3737646'
    performer_id = str(uuid.uuid4())
    start_date = '01-01-2022'
    days = 1
    causeOfDeathList = ["blow to the head", "stolen kidney", "some sort of fungus", "unexploded ordinance", "Fred", "scared watching horror movies", "mercury poisoning", "miner's lung", "premature autospy", "alien abduction"]

    resource = generateObservationCauseOfDeathCondition(causeOfDeathList, patient_id, performer_id, start_date, days)

    with open(f'tests/output/test_observation_cause_of_death_condition.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
