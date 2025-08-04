from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import Dict, Any

from core.Conversation import Conversation

router = APIRouter()

occurrences_history = {}


# class OccurrenceRequest(BaseModel):
#     client_context: dict
#     events_details: dict


# class OccurrenceStatus(BaseModel):
#     status: str
#     history: list[str]

@router.post("/handle_occurrence")
async def handle_occurrence(occurrence):
    occurrence_hash = str(uuid4())    
    conversation_result = Conversation(occurrence).start_conversation()
    occurrences_history[occurrence_hash] = conversation_result

    return {"id": occurrence_hash}


@router.get("/status_occurrence")
async def status_occurrence(hash: str):
    if hash not in occurrences_history:
        raise HTTPException(status_code=404, detail="Ocorrência não encontrada")
    return occurrences_history[hash]