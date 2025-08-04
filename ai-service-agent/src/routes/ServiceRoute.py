from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from core.Conversation import Conversation

router = APIRouter()

occurrences_history = {}

class TestCase(BaseModel):
    test_cases: list[dict]
    test_suite_id: str
    
def _process_occurrence(occurrence, occurrence_id):
    agents_conversation = Conversation(occurrence)
    conversation_result = agents_conversation.start_conversation()
    occurrences_history[occurrence_id] = conversation_result

@router.post("/handle_occurrence")
async def handle_occurrence(tests: TestCase, background_tasks: BackgroundTasks):
    ids = []
    for occurrence in tests.test_cases:
        occurrence_id = str(uuid4())
        background_tasks.add_task(_process_occurrence, occurrence, occurrence_id)
        ids.append(occurrence_id)

    return ids


@router.get("/status_occurrence")
async def status_occurrence(hash: str):
    if hash not in occurrences_history:
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada")
    return occurrences_history[hash]