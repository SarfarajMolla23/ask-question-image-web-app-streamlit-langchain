---

# Image Question Answering Web App

An interactive web application that allows users to upload an image, ask questions about it, and receive AI-generated responses. The app leverages advanced AI models for image captioning, object detection, and conversational question answering.

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/image-question-answering.git
   ```

2. **Navigate to the project directory**  
   ```bash
   cd ask-question-image-web-app-streamlit-langchain
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain an OpenAI API Key**  
   - Sign up for an API key at [OpenAI](https://platform.openai.com/).

5. **Set up your API Key**  
   Replace the placeholder `YOUR_API_KEY` in the `main.py` file with your actual OpenAI API key:  
   ```python
   llm = ChatOpenAI(
       openai_api_key='YOUR_API_KEY',
       temperature=0,
       model_name="gpt-3.5-turbo"
   )
   ```

6. **Run the Streamlit application**  
   ```bash
   streamlit run main.py
   ```

7. **Access the app**  
   Open your web browser and go to [http://localhost:8501](http://localhost:8501) to start using the application.

---

## Usage

1. **Upload an Image**  
   - Click the file upload button to upload an image.
   
2. **View the Image**  
   - The uploaded image will be displayed in the app.

3. **Ask a Question**  
   - Enter a question about the image in the text input field.

4. **Get a Response**  
   - The conversational AI agent will process the image and your question, generating a response displayed below the input field.

---

## Tools Used

The application utilizes the following tools for AI-based image understanding:

- **ImageCaptionTool**  
  Generates a textual caption for the uploaded image.

- **ObjectDetectionTool**  
  Performs object detection on the uploaded image to identify objects present in the scene.

---

## Contributing

Contributions are welcome! Feel free to:

- Fork the repository.
- Submit a pull request with your ideas, bug fixes, or enhancements.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **OpenAI GPT-3.5 Turbo**  
  This project uses OpenAI's GPT-3.5 Turbo model for conversational question answering. Learn more at [OpenAI](https://platform.openai.com/).

- **Streamlit**  
  The interactive user interface is powered by the Streamlit library. Visit the [Streamlit documentation](https://docs.streamlit.io/) for more details.

- **LangChain**  
  LangChain is used for managing the conversational AI agent and its tools. Explore more at the [LangChain GitHub repository](https://github.com/hwchase17/langchain).

- **Hugging Face Transformers**  
  The Transformers library is used for image captioning and object detection. Visit [Hugging Face](https://huggingface.co/transformers) for more details.

---


Demo images:

![Screenshot 2024-12-19 185022](https://github.com/user-attachments/assets/7cc18447-d95d-448c-82a2-d71ec1941538)

![Screenshot 2024-12-19 184613](https://github.com/user-attachments/assets/9b25b611-0ea2-455d-a5d9-18f18a5325fe)

![Screenshot 2024-12-19 184653](https://github.com/user-attachments/assets/4a90ac09-236f-48d0-995f-f82863c0791e)

![Screenshot 2024-12-19 184751](https://github.com/user-attachments/assets/d95627df-a59e-41ad-9452-5ee5cdf5fa53)
