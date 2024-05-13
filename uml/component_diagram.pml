@startuml
title Component Diagram for SmartSearch

package "SmartSearch Application" {
    [Web Interface] as UI
    [Application Controller] as AC
    [SemanticSearcher] as SS
    [QuestionAnswerer] as QA
    [Document Management] as DM
    [EmbeddingModel] as EM
    [VectorDB] as VDB
    [User Management] as UM
    [Analyzer] as AN
    [Matcher] as MA

    UI --> AC : Uses
    AC --> SS : Queries
    AC --> MA : Queries
    AC --> QA : Queries
    AC --> UM : Authenticates
    AC --> DM : Updates/Retrieves

    SS --> EM : Embeds Queries
    SS --> VDB : Searches Vectors

    QA --> SS : Searches Documents

    DM --> EM : Uses to embed Documents
    DM --> VDB : Stores/Retrieves Documents
    DM --> AN : Sends Documents for Metadata Enrichment
    UM --> DM : Manages Document Permissions

    AN --> DM : Updates Documents with Metadata
    MA --> VDB : Retrieves Exact Matches
}

@enduml
