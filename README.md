# Medicolegal Death Investigation FHIR Record Generator

This is a randomized test record generator for the Medicolegal Death Investigation (MDI) FHIR Implementation Guide (IG) using the [FHIR Generator Python Package](https://pypi.org/project/fhirgenerator/). It will generate a complete MDI Document bundle.

This tool is under development and currently only available as a python script by cloning this repository.

## Running the Generator
To run this project, in the root directory use:
```
python mdigen.py
```
## Configuration Options
Due to the nature of MDI FHIR documents, there is less customization available for this project than the base FHIR Generator. This is all handled in the `config.json`, which is required for the project to run. Core areas of configuration involve basic record details such as the date of the record, a range for relative time of death, number of records to generate, and basic subject related demographics. Custom lists of causes of death, contributing conditions, and how death injury occurred may also be provided.

```
{
    "recordCount": 1,
    "startDate": "01-01-2022",
    "deathDateRange": [-7, -1],
    "subject": {
        "ageMin": 18,
        "ageMax": 76,
        "genderMFOU": [47, 47, 1, 5]
    },
    "causeOfDeathList": [
        "cause 1",
        "cause 2"
    ],
    "contributingConditionList": [
        "condition 1",
        "condition 2"
    ],
    "howDeathInjuryOccurredList": [
        "how occurred 1",
        "how occurred 2"
    ]
}
```
* `recordCount` - Controls the number of records generated.
* `startDate` - Inherited from FHIR Generator, this sets the baseline date for the record.
* `deathDateRange` - The range in which the date of death may occur relative to the record baseline (start) date. Negative values should be used to establish a date of death prior to record generation. For example, given a start date of November 10th and a deathDateRange of -7 and -1, the death date may fall between November 3rd through November 9th.
* `subject`
  * `ageMin` and `ageMax` - The subject's minimum and maximum age.
  * `genderMFOU` - This is a 4 integer list that determines the weighting of the `Patient.gender` field (Administrative Gender), in order of: Male, Female, Other, Unknown. The default of `\[47, 47, 1, 5\]` will give a 47% chance of Male, 47% chance of Female, 1% chance of Other, and 5% chance of Unknown.
* `causeOfDeathList` - This is a list of causes of death that will populate the Observation - Cause of Death Condition profile randomly. Note: This currently only allows a list of strings which are used to populate the the `valueCodeableConcept.text` field.
* `contributingConditionList` - This is a list of contributing conditions that will populate the Observation - Condition Contributing to Death profile randomly. (Note: This currently only allows a list of strings which are used to populate the the `valueCodeableConcept.text` field.)
* `howDeathInjuryOccurredList` -  This is a list of potential values that will randomly be set in the Observation - How Death Injury Occurred profile. (Note: This profile uses `valueString`.)

## To Do List

* Allow Coding for conditions to be passed for the `causeOfDeathList` and `contributingConditionList` to populate the respectives resources.
* FAST API Endpoint to allow for backend service generation of records.
* Option to generate errors in records for testing workflows.
* US Core Practitioner Generation (current a static resource "placeholder").