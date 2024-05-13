@startuml
title Sequence Diagram for the scenario that a user wants to find an answer for their question

actor SearchUser
participant QuestionAnswerer
participant SemanticSearcher
participant EmbeddingModel
participant VectorDB

SearchUser -> QuestionAnswerer : extract_answer(question)
activate QuestionAnswerer

QuestionAnswerer -> SemanticSearcher : search relevant documents(question)
activate SemanticSearcher

SemanticSearcher -> EmbeddingModel : embed(question)
activate EmbeddingModel
EmbeddingModel -> SemanticSearcher : return vector
deactivate EmbeddingModel

SemanticSearcher -> VectorDB : find documents(vector)
activate VectorDB
VectorDB -> SemanticSearcher : return documents
deactivate VectorDB

SemanticSearcher -> QuestionAnswerer : return documents
deactivate SemanticSearcher

QuestionAnswerer -> QuestionAnswerer : process documents to extract answer
QuestionAnswerer -> SearchUser : return answer
deactivate QuestionAnswerer

@enduml
