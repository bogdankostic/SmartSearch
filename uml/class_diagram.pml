@startuml
title Class Diagram for SmartSearch

abstract class Document {
    -embedding: list
    -ID: int
}
class TextDocument {
    -text: string
    -meta: map
}
class ImageDocument {
    -blob: binary
    -textual_description: string
    -meta: map
}

abstract class BaseMatcher {
    +search(input: string): list
}
class NaiveMatcher {
    +search(input: string): list
}
class BoyerMooreMatcher {
    +search(input: string): list
}

abstract class Analyzer {
    +analyze(doc: Document): any
}
class SentimentAnalyzer {
    +analyze(doc: Document): any
}
class NERAnalyzer {
    +analyze(doc: Document): any
}

class QuestionAnswerer {
    +extract_answer(query: string): string
}
class SemanticSearcher {
    -vectorDB: VectorDB
    +search(query: string): list
}
class EmbeddingModel {
    -model: any
    +embed(text: string): list
}
class VectorDB {
    +add_document(doc: Document): void
    +delete_document(docID: int): void
}

abstract class User {
    -userID: int
    -username: string
}
class Admin {
    +invite_user(email: string): void
    +set_user_role(userID: int, role: string): void
}
class ContentProvider {
    +add_document(doc: Document): void
}
class SearchUser {
    +search(query: string): list
}

TextDocument -up-|> Document
ImageDocument -up-|> Document

NaiveMatcher -up-|> BaseMatcher
BoyerMooreMatcher -up-|> BaseMatcher

SentimentAnalyzer -up-|> Analyzer
NERAnalyzer -up-|> Analyzer

Admin -up-|> User
ContentProvider -up-|> User
SearchUser -up-|> User

SemanticSearcher ..> VectorDB : uses
SemanticSearcher ..> EmbeddingModel : uses
QuestionAnswerer ..> SemanticSearcher : uses
Document ..> EmbeddingModel : embedding update

@enduml
