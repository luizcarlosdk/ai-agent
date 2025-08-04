from agents.AssistentAgent import AssistentAgent
from agents.ClientAgent import ClientAgent

class Conversation:
    def __init__(self, occurrence):
        self.occurrence = occurrence[0]
        
        self.assistent_agent = AssistentAgent(self.occurrence)
        self.client_agent = ClientAgent(self.occurrence, "palavra correta", "bem")
        
    
    def start_conversation(self):
        assistant_question = self.assistent_agent.initial_message()
        print(f"Resposta do assistente: {assistant_question}")
        client_response = self.client_agent.agent_conversation(assistant_question)
        print(f"Resposta do cliente: {client_response}")


        while True:
            assistant_question = self.assistent_agent.agent_conversation(client_response)
            print(f"Resposta do assistente: {assistant_question}")

            if "ESCALADO" in assistant_question or "FINALIZADO" in assistant_question:
                return {
                    "status": "Conversation ended",
                    "messages": self.assistent_agent.chat_history
                }

            client_response = self.client_agent.agent_conversation(assistant_question)
            print(f"Resposta do cliente: {client_response}")