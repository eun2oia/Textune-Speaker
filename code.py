from google.cloud import translate_v2 as translate
from gtts import gTTS
import os

# Google Cloud Translate API를 사용하여 번역하기
def translate_text(text, target_language):
    # 여러분의 Google Cloud Project ID를 입력하세요
    project_id = "strategic-reef-407910"

    translate_client = translate.Client()

    result = translate_client.translate(
        text,
        target_language=target_language
    )

    return result['translatedText']

# gTTS를 사용하여 음성 출력하기
def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("start output.mp3")  # 윈도우 환경에서 음성 파일 재생

# 번역하고 음성 출력하기
text = "Hello, how are you?"
target_language = "ko"  # 번역할 언어 코드 (여기서는 한국어)

translated_text = translate_text(text, target_language)
print("번역된 텍스트:", translated_text,end='')

text_to_speech(translated_text, target_language)