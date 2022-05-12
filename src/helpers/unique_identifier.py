import uuid
from src.cannonicalUrls import unique_identifier_system

def generateUniqueIdentifier() -> dict:
    return {"system": unique_identifier_system, "value": f"urn:uuid:{str(uuid.uuid4())}" }