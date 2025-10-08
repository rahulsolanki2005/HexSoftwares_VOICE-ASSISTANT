# Tom — Personal AI Voice Assistant 🤖

This is a simple AI Voice Assistant project** created for the **HexSoftwares Internship Task.
The assistant listens to your voice, understands the command, performs tasks like searching Wikipedia or opening websites, and responds using text-to-speech — similar to Google Assistant.

---

## 📌 Features
- Greets the user according to the time.
- Listens to voice commands using microphone.
- Speaks responses using **Text-to-Speech (pyttsx3)**.
- Can search **Wikipedia** and speak the summary.
- Can open popular websites like **YouTube**, **Google**, **Instagram**, etc.
- Can tell the current **time**.
- After completing a command, it asks:  
  👉 *“Do you want me to do something else?”*  
  - Say **“Yes”** → listens again  
  - Say **“No / Stop / Exit”** → ends the program

---

## 🧠 Libraries Used
- **pyttsx3** → for text-to-speech output  
- **speech_recognition** → for converting voice to text  
- **wikipedia** → to fetch information from Wikipedia  
- **webbrowser** → to open websites  
- **datetime** → to get the current time  

---

## ⚙️ How It Works
1. The assistant first greets you based on the current time.  
2. It then listens to your voice command using your microphone.  
3. The voice is converted into text and matched with specific commands.  
4. According to the command:
   - Opens websites  
   - Searches Wikipedia  
   - Speaks the current time  
   - Or performs a Google search  
5. After each task, it asks if you need more help.

---

## ▶️ How to Run
1. Install all required libraries:
   ```bash
   pip install pyttsx3 speechrecognition wikipedia
