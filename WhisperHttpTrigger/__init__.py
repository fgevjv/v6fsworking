import logging
import azure.functions as func
import openai
import os

openai.api_key = os.environ.get("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")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing Whisper transcription request.")
    
    try:
        uploaded_file = req.files.get("file")
        if not uploaded_file:
            return func.HttpResponse("No file uploaded", status_code=400)

        response = openai.Audio.transcribe("whisper-1", uploaded_file)
        transcription = response.get("text", "")
        return func.HttpResponse(transcription, status_code=200)
    
    except Exception as e:
        logging.error(f"Transcription error: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
