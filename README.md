# AI Data Access Application

## Overview

This application leverages AI agents to access and extract information from various data sources. The agents are built using `llama index` and `gpt-3.5-turbo`. The project includes two specialized agents:

1. **PDF Agent**: Reads and extracts information from PDF files.
2. **Tabular Data Agent**: Accesses and extracts information from tabular datasets (e.g., CSV files).

The AI agents determine the most appropriate data source based on the query and provide the relevant information. Additionally, the agents can save the extracted information to a notepad file if instructed.

## Features

- AI-powered data extraction from PDF and CSV files.
- Intelligent selection of data source based on query.
- Save extracted information to a notepad file.

## File Structure

├── main.py # Base code for the application
├── pdf.py # Code for extracting and parsing PDF files
├── prompt.py # Prompts used in the project
├── data
│ ├── population.csv # Population details of all countries
│ └── india.pdf # Information about India extracted from Wikipedia
├── requirements.txt # List of required packages
└── README.md # Project description and instructions


## Installation

To set up the application, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/ai-data-access.git
    cd ai-data-access
    ```

2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Running the Application**:

    Execute the main script to start the application:

    ```bash
    python main.py
    ```

2. **Querying the AI Agents**:

    - You can ask questions related to the population of countries or information about India.
    - Based on your query, the appropriate agent will be activated to fetch the information.

3. **Saving Information**:

    - If you want to save the extracted information, specify this in your query.
    - The information will be saved to a notepad file.

## Project Files

- **main.py**:
  - Contains the base code for running the application.
  - Initializes the AI agents and handles user queries.

- **pdf.py**:
  - Contains the code for extracting and parsing information from PDF files.
  - Utilizes the `llama index` and `gpt-3.5-turbo` for AI-driven extraction.

- **prompt.py**:
  - Contains the prompts used for querying the AI agents.
  - Centralizes prompt management for easy modification and updates.

- **data**:
  - `population.csv`: A CSV file containing population details of all countries.
  - `india.pdf`: A PDF file with information about India extracted from Wikipedia.

- **requirements.txt**:
  - Lists all the required packages for the project.
  - Ensures a consistent environment setup.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [gurjeet333@gmail.com](mailto:gurjeet333@gmail.com).

