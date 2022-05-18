from src.profiles.bundleDocumentMDItoEDRS import generateBundleDocumentMDItoEDRS, addEntry, addEntries, insertComposition
from src.profiles.observationCauseOfDeathCondition import generateObservationCauseOfDeathCondition
from src.profiles.observationConditionContributingToDeath import generateObservationConditionContributingToDeath
from src.profiles.observationDeathInjuryEventOccurredAtWork import generateObservationDeathInjuryEventOccurredAtWork
from src.profiles.observationDecedentPregnancy import generateObservationDecedentPregnancy
from src.profiles.observationHowDeathInjuryOccurred import generateObservationHowDeathInjuryOccurred
from src.profiles.observationMannerOfDeath import generateObservationMannerOfDeath
from src.profiles.observationTobaccoUseContributedToDeath import generateObservationTobaccoUseContributedToDeath
from src.profiles.listCauseOfDeathPathway import generateListCauseOfDeathPathway
from src.profiles.observationDeathDate import generateObservationDeathDate
from src.helpers.subject import generateSubject
from src.helpers.uscorepractitioner import getUsCorePractitioner
from src.helpers.location import generateLocation
from src.profiles.compositionMDItoEDRS import addSection, generateCompositionMDItoEDRS, generateCompositionSection
from fhirgenerator.helpers.helpers import default
from src.cannonicalUrls import CodeSystem_mdi_codes
import orjson
import os
import json
import random

def main():
    config = openConfig()
    record_count = config["recordCount"]
    start_date = config["startDate"]
    days = config["days"]

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
        ## Step 4a - Demographics (Occupation History)
        ## Step 4b - Circumstances (Death Location, Work Injury, Tobacco Use Contributed To Death, Decedent Pregnancy)
        ### TODO: Death Location (US Core Location)
        deathLocation = generateLocation() # TODO: Link to US Core Death Date
        location_id = deathLocation["id"]

        observationDeathInjuryEventOccurredAtWork = generateObservationDeathInjuryEventOccurredAtWork(subject_id, practitioner_id, start_date, days)
        observationTobaccoUseContributedToDeath = generateObservationTobaccoUseContributedToDeath(subject_id, practitioner_id, start_date, days)
        observationDecedentPregancy = generateObservationDecedentPregnancy(subject_id, practitioner_id, start_date, days)

        circumstancesSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "circumstances"},
            [
                deathLocation,
                observationDeathInjuryEventOccurredAtWork,
                observationTobaccoUseContributedToDeath,
                observationDecedentPregancy
            ])
        composition = addSection(composition, circumstancesSection)
      
        ## Step 4c - Juridiction (Death Date)
        observationDeathDate = generateObservationDeathDate(config, location_id, subject_id, practitioner_id, start_date, days)
        jurisdictionSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "jurisdiction"}, [observationDeathDate])
        composition = addSection(composition, jurisdictionSection)

        # Step 4d - Cause and Manner (Cause of Death Pathway, Condition Contributing to Death, Manner of Death, How Death Injury Occurred)
        causeCount = int(random.randint(1, 5))
        observationCauseOfDeathConditionList = []
        for x in range(causeCount):
            observationCauseOfDeathConditionList.append(generateObservationCauseOfDeathCondition(
                config["causeOfDeathList"], subject_id, practitioner_id, start_date, days))
        causeOfDeathPathway = generateListCauseOfDeathPathway(observationCauseOfDeathConditionList, subject_id, practitioner_id)

        contributingCount = int(random.randint(1, 5))
        observationConditionContributingToDeathList = []
        for x in range (contributingCount):
            observationConditionContributingToDeathList.append(generateObservationConditionContributingToDeath(
                config["contributingConditionList"], subject_id, practitioner_id, start_date, days))
        
        observationMannerOfDeath = generateObservationMannerOfDeath(subject_id, practitioner_id, start_date, days)
        observationHowDeathInjuryEventOccurred = generateObservationHowDeathInjuryOccurred(config["howDeathInjuryOccurredList"], subject_id, practitioner_id, start_date, days)

        causeMannerSection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "cause-manner"},
            [causeOfDeathPathway, observationMannerOfDeath, observationHowDeathInjuryEventOccurred] + observationConditionContributingToDeathList)
        composition = addSection(composition, causeMannerSection)

        # Step 4e - Medical History (US Core Condition)
        medicalHistorySection = generateCompositionSection({"system": CodeSystem_mdi_codes, "code": "medical-history"}, [])
        composition = addSection(composition, medicalHistorySection)

        # Step 5 - Add Resource to Bundle
        ## Core Resources
        bundle = insertComposition(bundle, composition)
        bundle = addEntries(bundle, [subject, practitioner])
        
        ## Demographics Resources
        ## Circumstances Resources
        bundle = addEntries(bundle, [
            deathLocation,
            observationDeathInjuryEventOccurredAtWork,
            observationTobaccoUseContributedToDeath,
            observationDecedentPregancy
            ])

        ## Jurisdiction Resources
        bundle = addEntry(bundle, observationDeathDate)
        
        ## Cause-Manner Resources
        bundle = addEntries(bundle, observationCauseOfDeathConditionList)
        bundle = addEntry(bundle, causeOfDeathPathway)
        bundle = addEntries(bundle, observationConditionContributingToDeathList)
        bundle = addEntries(bundle, [observationMannerOfDeath, observationHowDeathInjuryEventOccurred])

        ## Medical History Resources
        ## Exam-Autopsy Resources
        ## Narratives Resources


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