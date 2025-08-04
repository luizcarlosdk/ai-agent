from agents.AssistentAgent import AssistentAgent
from agents.ClientAgent import ClientAgent

class Conversation:
    def __init__(self, occurrence):
        self.occurrence = occurrence
        
        self.assistent_agent = AssistentAgent(self.occurrence)
        self.client_agent = ClientAgent(self.occurrence)
        
    
    def start_conversation(self):
        status = False
        assistant_question = self.assistent_agent.initial_message()
        client_response = self.client_agent.agent_conversation(assistant_question)

        iteration_counter = 0
        while iteration_counter < 10:
            assistant_question = self.assistent_agent.agent_conversation(client_response)
            if "ESCALADO" in assistant_question:
                status = "ESCALADO"
            elif "FINALIZADO" in assistant_question:
                status = "FINALIZADO"
            
            if status:    
                self.assistent_agent.chat_history.pop(0)
                return {
                    "status_final": status,
                    "mensagens": self.assistent_agent.chat_history
                }

            client_response = self.client_agent.agent_conversation(assistant_question)
            iteration_counter += 1
        
        return {
            "status_final": "Máximo de iterações atingido",
            "mensagens": self.assistent_agent.chat_history
        }
