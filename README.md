
# Emotion Detector

## Overview

Emotion Detector is a Python web application that uses the IBM Watson
NLP Emotion Prediction service to analyze text and identify five
emotions: anger, disgust, fear, joy, and sadness.

The application determines the dominant emotion and presents the
results through a Flask web interface.

## Features

- Emotion detection using IBM Watson NLP
- Structured emotion scores and dominant emotion
- Python package organization
- Unit tests using unittest and mocks
- Flask web deployment
- Error handling for blank input and API failures
- Static code analysis using Pylint

## Project Structure

```text
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3
- Flask
- Requests
- Pylint

The Watson NLP endpoint must be accessible for live emotion analysis.

## Installation

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python server.py
```

Open http://127.0.0.1:5000 in your browser.

## Run Unit Tests

```bash
python -m unittest -v test_emotion_detection
```

## Static Code Analysis

```bash
python -m pylint server.py
```

## Error Handling

The application rejects blank input, handles HTTP 400 responses,
and returns an invalid result when the service fails or returns
an unexpected response.

## Technologies

- Python
- IBM Watson NLP
- Flask
- Requests
- unittest
- Pylint

## Author

Atharvmulik