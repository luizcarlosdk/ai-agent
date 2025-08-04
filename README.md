# Ai-agent

## Description

The project implements two AI Agents (Client and Assistant) that interacte with each other simulating a security application verification

## Architecture

  **src/agents**: Implementation of Client and Assistant Agents
  
  **src/config**: Holds enviroment variables
  
  **src/core**: Responsible for administrate the conversation between the agents
  
  **src/routes**: Makes 2 API ENDPOINTS: 
  
  - **POST** /handling_occurrence: starts processing an occurrence given in the body of a POST, and store the result with a hash code
  - **GET** /status_occurrence?hash=<id>: returns the conversation status and history
  

## How to Run

### Pre-requisites

- docker and docker-compose
- OpenRouter API key

Before running the project, make sure the .env is filled

## Running the application
```
  docker-compose --profile project build
  docker-compose --profile project up
```
