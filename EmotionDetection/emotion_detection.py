
"""Detect emotions in text using the IBM Watson NLP service."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion."""
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return empty_result.copy()

    payload = {
        "raw_document": {
            "text": text_to_analyze,
        }
    }

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=20,
        )

        if response.status_code == 400:
            return empty_result.copy()

        response.raise_for_status()
        data = response.json()

        emotions = data["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
        }

        result["dominant_emotion"] = max(
            result,
            key=result.get,
        )

        return result

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return empty_result.copy()
