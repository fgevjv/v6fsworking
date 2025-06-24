import logging
import openai
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing Whisper API transcription request.")
    try:
        file = req.files.get("file")
        if not file:
            return func.HttpResponse("No file uploaded", status_code=400)

        openai.api_key = "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"  # or use os.environ['OPENAI_API_KEY']

        transcript = openai.Audio.transcribe("whisper-1", file.stream)
        return func.HttpResponse(transcript['text'], status_code=200)
    except Exception as e:
        logging.error(f"Transcription error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
