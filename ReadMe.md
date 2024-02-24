# Django Sentiment Analysis Web App
=================================

This Django web application performs sentiment analysis on user-provided sentences. It allows users to input sentences and analyzes the sentiment of the input using a sentiment analysis module.

## Features

*   **Input Sentence Analysis**: Users can input a sentence which will be analyzed for sentiment.
*   **Sentiment Analysis**: The application performs sentiment analysis on the input sentence.
*   **Tokenization and Stopword Removal**: Before analysis, the input sentence is tokenized and stopwords are removed.
*   **Part-of-Speech Tagging**: The application also provides part-of-speech tagging for the words in the input sentence.
*   **Frequency Distribution**: It calculates and displays the frequency distribution of words in the input sentence.

## Installation

```bash
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
```

## Usage

1.  Run the Django server:
    
    `python manage.py runserver`
    
2.  Access the application in your web browser at `http://localhost:8000/`.
    
3.  Enter a sentence in the provided input field and submit for analysis.
    
4.  View the sentiment score, tokenized words, stopwords removed, part-of-speech tagging, and frequency distribution of words in the analyzed sentence.
    

## Files and Structure

*   `analyse/` directory:
    *   `forms.py`: Contains the form definition for user input.
    *   `templates/analyse/` directory: Contains HTML templates for rendering views.
        *   `index.html`: Template for the homepage with the input form.
        *   `analyse.html`: Template for displaying the analysis results.
*   `sentiment_analyser.py`: Module for sentiment analysis and related functions.
*   `phrase.json`: JSON file to store input sentences and their details.

## Dependencies
------------

*   Django
*   Python (>=3.x)

### Contribution Guidelines

Contributions to the repository are welcome. If you find any issues or would like to add new features, please follow these guidelines:

- Fork the repository and create a new branch for your feature or bug fix.
- Ensure that your code follows PEP 8 style guidelines.
- Submit a pull request with a clear description of the changes you have made.

[Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please contact [meghamgarg@gmail.com](mailto:meghamgarg@gmail.com).
