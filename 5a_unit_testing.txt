from EmotionDetection import emotion_detector

print(emotion_detector("I am glad this happend")['dominant_emotion'])
print(emotion_detector("I am really mad about this")['dominant_emotion'])
print(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'])
print(emotion_detector("I am so sad about this")['dominant_emotion'])
print(emotion_detector("I am really afraid that his will happen")['dominant_emotion'])