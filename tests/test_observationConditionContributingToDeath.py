import orjson
from src.profiles.observationConditionContributingToDeath import generateObservationConditionContributingToDeath
import uuid
from fhirgenerator.helpers.helpers import default


def testObservationCauseOfDeathCondition():
    patient_id = '26774-827647-736278-3737646'
    performer_id = str(uuid.uuid4())
    start_date = '01-01-2022'
    days = 1
    contributingConditionList = ["blurry brain holes", "previous pirate raid", "old football injury", "unstable biomass", "Fred", "working with really big bees", "super gout", "ancient curse", "modern curse", "future curse", "too many vitamins", "just generally not likable"]

    resource = generateObservationConditionContributingToDeath(contributingConditionList, patient_id, performer_id, start_date, days)

    with open(f'tests/output/test_observation_condition_contributing_to_death.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
