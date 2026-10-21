
"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the emotion detector's response handling."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_all_five_emotions(self, mock_post):
        """Test dominant emotions and the returned dictionary."""
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted by this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am afraid this will happen", "fear"),
        ]

        for sentence, expected_emotion in test_cases:
            with self.subTest(expected_emotion=expected_emotion):
                scores = {
                    "anger": 0.05,
                    "disgust": 0.05,
                    "fear": 0.05,
                    "joy": 0.05,
                    "sadness": 0.05,
                }
                scores[expected_emotion] = 0.95

                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.json.return_value = {
                    "emotionPredictions": [
                        {"emotion": scores}
                    ]
                }
                mock_response.raise_for_status.return_value = None
                mock_post.return_value = mock_response

                result = emotion_detector(sentence)

                self.assertEqual(
                    result["dominant_emotion"],
                    expected_emotion,
                )
                self.assertEqual(
                    set(result),
                    {
                        "anger", "disgust", "fear",
                        "joy", "sadness", "dominant_emotion",
                    },
                )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        """Return None values when the API returns status 400."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("Invalid test input")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, mock_post):
        """Reject blank input without calling the API."""
        result = emotion_detector("   ")

        self.assertIsNone(result["dominant_emotion"])
        mock_post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_service_failure(self, mock_post):
        """Handle a network failure without crashing."""
        import requests

        mock_post.side_effect = requests.ConnectionError(
            "Test connection failure"
        )

        result = emotion_detector("Test sentence")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
