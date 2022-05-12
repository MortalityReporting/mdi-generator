from src.cannonicalUrls import bundle_DocumentMDItoEDRS
import uuid
from fhir.resources.bundle import Bundle
from src.helpers.unique_identifier import generateUniqueIdentifier
from datetime import datetime

def generateBundleDocumentMDItoEDRS():
    bundle = {}
    bundle["resourceType"] = "Bundle"
    bundle["id"] = str(uuid.uuid4())
    bundle["meta"] = {}
    bundle["meta"]["profile"] = [ bundle_DocumentMDItoEDRS ]
    bundle["identifier"] = generateUniqueIdentifier()
    bundle["type"] = "document"
    bundle["entry"] = []
    
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+00:00")
    bundle["timestamp"] = str(timestamp)

    bundle = Bundle(**bundle).dict()

    return bundle

def insertComposition(bundle, composition):
    fullUrl = f"{composition['resourceType']}/{composition['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = composition
    if not "entry" in bundle.keys():
        bundle["entry"] = []
    bundle["entry"].insert(0, bundle_entry)
    return bundle

def addEntry(bundle, entry):
    #bundle = dict(bundle)
    fullUrl = f"{entry['resourceType']}/{entry['id']}"
    bundle_entry = {}
    bundle_entry["fullUrl"] = fullUrl
    bundle_entry["resource"] = entry
    if not "entry" in bundle.keys():
        bundle["entry"] = []
    bundle["entry"].append(bundle_entry)
    return bundle

def addEntries(bundle, entries):
    for entry in entries:
        fullUrl = f"{entry['resourceType']}/{entry['id']}"
        bundle_entry = {}
        bundle_entry["fullUrl"] = fullUrl
        bundle_entry["resource"] = entry
        if not "entry" in bundle.keys():
            bundle["entry"] = []
        bundle["entry"].append(bundle_entry)
    return bundle