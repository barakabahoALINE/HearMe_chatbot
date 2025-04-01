def recommend_videos(emotion):
    recommendations = {
        'Positive': ['https://youtu.be/positive_video1', 'https://youtu.be/positive_video2'],
        'Negative': ['https://youtu.be/meditation_video1', 'https://youtu.be/stress_relief_video2'],
        'Neutral': ['https://youtu.be/motivational_video1', 'https://youtu.be/motivational_video2']
    }
    return recommendations.get(emotion, [])
