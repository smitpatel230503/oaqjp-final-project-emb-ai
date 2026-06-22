import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """ Unit tests validation suite tracking individual emotional scenarios """
    def test_emotion_detector(self):
        # Scenario check for Joy dominance
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')
        
        # Scenario check for Anger dominance
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')
        
        # Scenario check for Disgust dominance
        res_3 = emotion_detector("I am revolted by this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')
        
        # Scenario check for Sadness dominance
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')
        
        # Scenario check for Fear dominance
        res_5 = emotion_detector("I am really scared of this")
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()