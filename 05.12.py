import streamlit as st 

st.title("환영합니다 !")
# pip install streamlit 

st.code("x=2021")
st.video("https://youtu.be/NKmWtsBAhek?si=CcXLw6FJ7fFVOZej")

import streamlit as st
import requests

API_KEY = "YOUR_API_KEY"  # ← 본인의 API 키 입력

# YouTube 검색 함수
def search_youtube_videos(query, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        return []
        