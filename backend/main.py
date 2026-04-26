"""
Backend API for Image Caption Generator using LLaVA via Ollama.

This FastAPI application accepts image uploads and generates descriptive
captions using the LLaVA (Large Language and Vision Assistant) model,
which can understand both text and images.
"""
#PIL Image is used to import an image.
#base64 is for 
#import io is for 
import base64 
from fastapi import FastAPI, UploadFile, File
import requests
import json
from PIL import Image
import io

app = FastAPI()
OLLAMA_TIMEOUT_SECONDS = 1800

OLLAMA_API_URL = "http://localhost:11434/api/generate"


def read_ollama_stream(response: requests.Response) -> str:
    """Read Ollama's streamed NDJSON chunks into one response string."""
    chunks = []
    for line in response.iter_lines(decode_unicode=True):
        if not line:
            continue
        data = json.loads(line)
        chunks.append(data.get("response", ""))
        if data.get("done"):
            break
    return "".join(chunks).strip()


def call_ollama(payload: dict) -> str:
    """Call Ollama with streaming enabled so long local generations stay alive."""
    streamed_payload = {**payload, "stream": True}
    with requests.post(
        OLLAMA_API_URL,
        json=streamed_payload,
        timeout=(10, OLLAMA_TIMEOUT_SECONDS),
        stream=True,
    ) as response:
        response.raise_for_status()
        return read_ollama_stream(response)

@app.post("/caption/")
async def generate_caption(file: UploadFile = File(...)):
    """
    Generate a caption for an uploaded image.

    Uses the LLaVA model to analyze the image and produce a
    human-readable description of its contents.

    Args:
        file: An uploaded image file (JPEG, PNG, etc.)

    Returns:
        A dictionary containing the generated caption
    """
    # Read the uploaded file contents into memory
    # Using async file reading for better performance with large files
    contents = await file.read()

    # Open the image using PIL for processing
    # This validates the file is a valid image and allows format conversion
    image = Image.open(io.BytesIO(contents))

    # Create a BytesIO buffer to hold the image data
    # We'll convert the image to JPEG format for consistent processing
    buffered = io.BytesIO()

    # Save the image to the buffer in JPEG format
    # JPEG is preferred for LLaVA as it handles it efficiently
    image.save(buffered, format="JPEG")

    # Encode the image bytes to base64 string
    # Ollama's API requires images as base64-encoded strings
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Send the image to Ollama's API for caption generation.
    # The helper streams chunks from Ollama, then returns one complete caption.
    result = call_ollama({
        "model": "llava",  # Using llava model for vision capabilities
        "prompt": "Describe this image in detail.",  # Instruction for the model
        "images": [img_base64],  # Pass image as base64 array
    })

    # Return the caption.
    return {"caption": result}
