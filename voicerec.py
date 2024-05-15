
#
import sys
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class SpeechRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Arabic Speech Recognition App')
        self.setGeometry(300, 300, 900, 400)
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.button = QPushButton('Start Recording')
        self.button.clicked.connect(self.start_recording)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def start_recording(self):
        self.text_edit.setPlaceholderText('Start Recording...')
        try:
            recognizer = sr.Recognizer()
            mic = sr.Microphone()
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            self.text_edit.setPlaceholderText('Recognizing...')
            recognized_text = recognizer.recognize_google(audio, language='ar-AR')

            if recognized_text:
                current_text = self.text_edit.toPlainText()
                if current_text:
                    self.text_edit.setPlainText(f'{current_text}\n Text: {recognized_text}')
                else:
                    self.text_edit.setPlainText(f' Text: {recognized_text}')
            else:
                self.text_edit.setPlainText('No speech detected.')

        except sr.UnknownValueError:
            self.text_edit.setPlainText('Sorry, could not understand the audio.')
        except sr.RequestError:
            self.text_edit.setPlainText('Sorry, there was an issue with the service.')
        except Exception as e:
            self.text_edit.setPlainText(f'Error: {str(e)}')

def main():
    app = QApplication(sys.argv)
    window = SpeechRecognitionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
