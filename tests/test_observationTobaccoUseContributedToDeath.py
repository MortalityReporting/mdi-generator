import orjson
from src.profiles.observationTobaccoUseContributedToDeath import generateObservationTobaccoUseContributedToDeath
import uuid
from fhirgenerator.helpers.helpers import default
from src.cannonicalUrls import observation_TobaccoUseContributedToDeath
from src.fixedCodes import code_TobaccoUseContributedToDeath

def testObservationTobaccoUseContributedToDeath():
    patient_id = '26774-827647-736278-3737646'
    performer_id = str(uuid.uuid4())
    start_date = '01-01-2022'
    days = 1

    resource = generateObservationTobaccoUseContributedToDeath(patient_id, performer_id, start_date, days)

    assert observation_TobaccoUseContributedToDeath in resource["meta"]["profile"]
    assert code_TobaccoUseContributedToDeath in resource["code"]["coding"]

    with open(f'tests/output/test_observation_tobacco_use_contributed_to_death.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))
