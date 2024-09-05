# multimodal_data_collector.py

import cv2
import speech_recognition as sr
from threading import Thread
import time

class MultimodalDataCollector:
    def __init__(self, student_id):
        self.student_id = student_id
        self.camera = cv2.VideoCapture(0)
        self.recognizer = sr.Recognizer()
        self.text_input = ""
        self.interaction_log = []
        self.collecting = False

    def start_data_collection(self):
        self.collecting = True
        Thread(target=self.capture_video).start()
        Thread(target=self.capture_audio).start()

    def capture_video(self):
        while self.collecting:
            ret, frame = self.camera.read()
            if ret:
                # Save frame or process it here
                cv2.imwrite(f'data/{self.student_id}_frame.jpg', frame)
                # Simulate frame rate
                time.sleep(0.1)
            else:
                break

    def capture_audio(self):
        with sr.Microphone() as source:
            while self.collecting:
                print("Listening...")
                audio_data = self.recognizer.record(source, duration=5)
                try:
                    text = self.recognizer.recognize_google(audio_data)
                    print(f"Student said: {text}")
                    self.text_input += text + " "
                    self.interaction_log.append({
                        "timestamp": time.time(),
                        "text": text
                    })
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

    def stop_data_collection(self):
        self.collecting = False
        self.camera.release()
        cv2.destroyAllWindows()
        print("Data collection stopped.")

    def get_collected_data(self):
        return {
            "text_input": self.text_input,
            "interaction_log": self.interaction_log,
            # Include other data as needed
        }

if __name__ == "__main__":
    collector = MultimodalDataCollector("student_1")
    collector.start_data_collection()
    time.sleep(20)  # Collect data for 20 seconds
    collector.stop_data_collection()
    data = collector.get_collected_data()
    print("Collected Data:", data)
