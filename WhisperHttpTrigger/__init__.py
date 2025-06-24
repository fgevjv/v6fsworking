import logging
import azure.functions as func
import whisper
import tempfile

model = whisper.load_model("base")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Whisper HTTP trigger function processed a request.")
    try:
        uploaded_file = req.files.get("file")
        if not uploaded_file:
            return func.HttpResponse("No file uploaded", status_code=400)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name
        result = model.transcribe(temp_path)
        transcription = result.get("text", "")
        return func.HttpResponse(transcription, status_code=200)
    except Exception as e:
        logging.error(f"Error during transcription: {str(e)}")
        return func.HttpResponse(f"Internal Server Error: {str(e)}", status_code=500)
