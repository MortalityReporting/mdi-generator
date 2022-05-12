from src.profiles.bundleDocumentMDItoEDRS import generateBundleDocumentMDItoEDRS, addEntry, addEntries, insertComposition
from src.profiles.observationCauseOfDeathCondition import generateObservationCauseOfDeathCondition
from src.profiles.listCauseOfDeathPathway import generateListCauseOfDeathPathway
from src.helpers.subject import generateSubject
from src.helpers.uscorepractitioner import getUsCorePractitioner
from src.profiles.compositionMDItoEDRS import addSection, generateCompositionMDItoEDRS
from fhirgenerator.helpers.helpers import default
from src.cannonicalUrls import CodeSystem_mdi_codes
from src.helpers.section import generateCompositionSection
import orjson
import os
import json
import random

def main():
    config = openConfig()
    record_count = config["recordCount"]
    start_date = config["startDate"]

    print(f"Generating {record_count} MDI Record(s)...")

    for recordIndex in range(record_count):
        # Step 1 - Generate New Bundle
        bundle = generateBundleDocumentMDItoEDRS() # Empty Document Bundle Structure
    
        # Step 2 - Generate Subject (US Core Patient)
        subject = generateSubject(config["subject"], start_date) # The Subject helper class provides a means to manage MDI specific considerations of the US Core Patient.
        subject_id = subject["id"]

        # Step 3 - Get Static Practitioner (US Core Practitioner) - TODO: Generate Dynamically
        practitioner = getUsCorePractitioner()
        practitioner_id = practitioner["id"]
        
        # Step 3 - Generate Composition
        composition = generateCompositionMDItoEDRS(subject_id, practitioner_id, start_date)
        
        # Step 4 - For Each Section of Composition, Generate Resources
        # Step 4a
        circumstancesSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "circumstances"}, [])
        composition = addSection(composition, circumstancesSection)
      
        # Step 4b
        jurisdictionSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "jurisdiction"}, [])
        composition = addSection(composition, jurisdictionSection)

        # Step 4c - Cause and Manner
        causeCount = int(random.randint(1, 5))
        observationCauseOfDeathConditionList = []
        for x in range(causeCount):
            observationCauseOfDeathConditionList.append(generateObservationCauseOfDeathCondition(
                config["causeOfDeathList"], subject_id, practitioner_id, start_date, 1))
        causeOfDeathPathway = generateListCauseOfDeathPathway(observationCauseOfDeathConditionList, subject_id, practitioner_id)
        causeMannerSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "cause-manner"}, [causeOfDeathPathway])
        composition = addSection(composition, causeMannerSection)

        # Step 4d - Medical History
        medicalHistorySection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "medical-history"}, [])
        composition = addSection(composition, medicalHistorySection)

        # Insert Composition to document bundle, append each other resource.
        bundle = insertComposition(bundle, composition)
        bundle = addEntry(bundle, subject)
        bundle = addEntry(bundle, practitioner)
        bundle = addEntries(bundle, observationCauseOfDeathConditionList)
        bundle = addEntry(bundle, causeOfDeathPathway)

        subject_name = getSubjectName(subject)
        writeFile(bundle, subject_name)
        print(f"Generated Record #{recordIndex + 1}: {subject_name}")

def getSubjectName(subject: dict):
    family = subject["name"][0]["family"]
    given = subject["name"][0]["given"][0]
    return f"{family}, {given}"

def openConfig() -> dict:
    file = open('config.json')
    file_contents = json.load(file)
    file.close()
    return file_contents

def writeFile(resource, subject_name: str):
    output_path = "output/"
    output_path_exists = os.path.isdir(output_path)
    if not output_path_exists:
        os.makedirs(output_path)
    
    file_name = f"{subject_name} - {resource['id']}"
    with open(f'{output_path}{file_name}.json', 'wb') as outfile:
        outfile.write(orjson.dumps(resource, default=default, option=orjson.OPT_NAIVE_UTC))


if __name__ == "__main__":
    main()