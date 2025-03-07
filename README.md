# baker-sigma-llm
# Assistant Baker

This project is an interactive application designed to help travelers communicate in foreign countries by generating useful phrases in the local language. Built with Gradio, it provides an easy-to-use interface where users can input tasks either by typing or recording their voice.

## Features

- **Input Methods**: Users can either type a task (e.g., "order food") or record their voice.
- **Language Detection**: Automatically detects the language spoken in a selected country.
- **Phrase Generation**: Generates a list of commonly used phrases for the selected task and country.
- **Audio Transcription**: Converts recorded audio to text using the Whisper model.
- **Interactive UI**: Built with Gradio for an intuitive and responsive user experience.

## Installation

To run this project, you'll need Python installed on your machine along with the following packages:

```bash
pip install gradio langchain_community whisper openai torch
```

## How to Use

1. **Start the Application**:
   - Ensure you have installed all necessary dependencies by running `pip install -r requirements.txt` if you have a requirements file, or manually install the dependencies as indicated in the installation section.
   - Run the main script with the command:

     ```bash
     python your_script_name.py
     ```

   - Open your browser and go to the local URL displayed in the terminal (e.g., `http://127.0.0.1:7860`).

2. **Interact with the Interface**:
   - **Select a Task**:
     - You can enter the task you want to perform in the text box, such as "order food" or "ask for directions."
     - Alternatively, you can record your voice using the recording button, and the application will automatically transcribe the audio to text.

   - **Choose a Country**:
     - Select the country you are traveling to in the "Location" section. This will determine the language in which the phrases are generated.

   - **Set the Number of Phrases**:
     - Use the slider to select how many phrases you want to generate.

3. **Generate Responses**:
   - Click the "Generate response" button to get a list of useful phrases in the language of the selected country.

4. **Clear Input**:
   - If you want to start over, use the "Clear" button to reset all inputs and start from scratch.

5. **Close the Application**:
   - Once you’re done, simply close the browser window and stop the script in the terminal with `Ctrl + C`.

