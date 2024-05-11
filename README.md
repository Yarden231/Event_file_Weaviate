# Economic Events Database with Semantic Vectorization

This repository houses a solution for creating and managing an "economic events" database utilizing cutting-edge technologies. By leveraging OpenAI's powerful GPT-4 model via the StackAI framework, this project retrieves information on economic events, organizes it into a structured database, and enhances its accessibility through semantic vectorization using Weaviate.

## Problem Statement

Understanding and tracking economic events is crucial for making informed decisions in various fields such as finance, policy-making, and market analysis. However, manually curating and structuring this information can be time-consuming and error-prone. Moreover, traditional databases may not fully capture the semantic nuances of economic events, limiting their utility in advanced analytics and retrieval tasks.

## Solution Overview

This project offers a solution to address the challenges outlined above:

1. **Data Acquisition**: Utilizing OpenAI's GPT-4 model via the StackAI framework, economic events data is gathered by querying the model. GPT-4's advanced natural language processing capabilities ensure high-quality and relevant data retrieval.

2. **Database Management**: The retrieved economic events data is organized into a structured database, facilitating efficient storage, retrieval, and manipulation of information. This database serves as a reliable repository for economic events data.

3. **Semantic Vectorization**: Weaviate, a powerful semantic vector database, is employed to enhance the accessibility and utility of the economic events database. Each economic event is represented as a semantic vector object in Weaviate, capturing its contextual meaning and relationships.

4. **Semantic Querying**: Leveraging Weaviate's semantic querying capabilities, users can retrieve near-semantically related economic events based on specific criteria or contextual similarity. This enables intuitive and insightful exploration of the economic events database.

## Key Features

- **Automated Data Retrieval**: Seamless integration with OpenAI's GPT-4 model via StackAI enables automated querying of economic events data.
- **Structured Database**: The database is meticulously organized to ensure efficient storage and retrieval of economic events information.
- **Semantic Vectorization**: Economic events are transformed into semantic vectors in Weaviate, enabling advanced analytics and semantic querying.
- **Semantic Querying**: Users can retrieve economically relevant information based on semantic similarity, facilitating insightful analysis and decision-making.

## Usage

1. **Data Retrieval**: Run the provided code file to initiate data retrieval from GPT-4 using StackAI. Follow the prompts to specify the desired economic events criteria.
2. **Database Management**: Once the data is retrieved, execute the database arrangement script to organize the data into a structured format.
3. **Vector Database Creation**: Utilize the provided script to create a vector database in Weaviate, ensuring each economic event is represented as a semantic vector object.
4. **Querying**: Interact with the vector database in Weaviate to perform semantic queries and retrieve near-semantically related economic events.

## Requirements

- OpenAI API Key
- Weaviate Instance
- Python environment with necessary dependencies installed (specified in requirements.txt)


