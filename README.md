# Project 3: Image Caption Generator (LLaVA)

An AI-powered image caption generator that uses LLaMA vision-language model via Ollama to generate descriptive captions for uploaded images. Perfect for accessibility, content management, and AI training.

## Features

- **Vision-Language Model**: Uses LLaVA for accurate image understanding
- **Descriptive Captions**: Generates natural language descriptions
- **FastAPI Backend**: Efficient REST API for image processing
- **Streamlit Frontend**: User-friendly interface for image upload
- **Batch Processing**: Handle multiple images at once
- **Local Processing**: All analysis runs locally using Ollama LLMs - no external API dependencies

## Architecture

### Backend Components

1. **Image Processor** (`backend/main.py`)
   - Handles image file uploads
   - Manages image queue
   - Processes images for captioning

2. **Caption Generator** (`backend/main.py`)
   - Uses LLaVA vision-language model
   - Generates descriptive captions
   - Provides context and details

### Frontend Components

1. **Streamlit UI** (`frontend/app.py`)
   - User interface for image upload
   - Results display and visualization
   - Export functionality

2. **Reusable Components** (`frontend/components.py`)
   - Modular UI elements
   - Consistent styling and layout

## Installation

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running (for local LLM inference)

### Setup Steps

1. **Navigate to the project directory**:
   ```bash
   cd SchoolOfAI/Official/soai-03-image-caption
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and start Ollama** (if not already installed):
   ```bash
   # Install Ollama from https://ollama.com
   # Pull LLaVA model
   ollama pull llava
   # Start Ollama service
   ollama serve
   ```

## Running the Application

### Backend API

1. **Start the FastAPI backend**:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. **Access the API**: Navigate to `http://localhost:8000` for API documentation

### Frontend UI

1. **Start the Streamlit application** (in a new terminal):
   ```bash
   streamlit run frontend/app.py
   ```

2. **Open your browser**: Navigate to `http://localhost:8501`

## Usage

### 1. Upload Images

- Select one or multiple image files
- Supported formats: JPG, PNG, GIF, etc.
- Click "Upload" to process images

### 2. Generate Captions

- Click "Generate Captions" to start processing
- Wait for the AI to analyze images
- View the descriptive captions

### 3. Review Results

- **Captions**: Natural language descriptions of images
- **Context**: Additional details and information
- **Confidence**: AI confidence in caption accuracy

### 4. Export Results

- Copy captions for use
- Export as text or JSON
- Save for future reference

## Workflow

```
Upload Images → Backend API → LLaVA → Generate Captions → Display Results
     ↓               ↓            ↓                ↓                  ↓
  Select files    FastAPI      Call model      Extract        Show to
  or images       endpoint     with prompt   descriptions    user
```

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
OLLAMA_MODEL=llava
OLLAMA_API_URL=http://localhost:11434/api/generate
```

### Ollama Models

The system supports any Ollama model. Recommended models:
- `llava` - Vision-language model for image understanding (default)

## Project Structure

```
soai-03-image-caption/
├── backend/
│   └── main.py                  # FastAPI backend
├── frontend/
│   ├── app.py                    # Streamlit UI
│   └── components.py             # Reusable UI components
├── requirements.txt              # Python dependencies
└── README.md                   # This file
```

## Dependencies

- `fastapi` - Web API framework
- `uvicorn` - ASGI server
- `streamlit` - Web UI framework
- `requests` - HTTP client for Ollama API
- `python-dateutil` - Date/time parsing

## Troubleshooting

### Ollama Connection Issues

If you see connection errors:
1. Verify Ollama is running: `ollama list`
2. Check the API URL: `curl http://localhost:11434/api/generate`
3. Ensure the model is pulled: `ollama pull llava`

### Backend API Issues

If the backend isn't responding:
1. Verify uvicorn is running: `ps aux | grep uvicorn`
2. Check the port isn't in use: `lsof -i :8000`
3. Review backend logs for errors

### Frontend Connection Issues

If the frontend can't connect to the backend:
1. Verify both services are running
2. Check the API URL in frontend/app.py
3. Ensure CORS is configured correctly

### Caption Generation Issues

If captions aren't being generated:
1. Check that images are properly uploaded
2. Verify the LLaVA model is pulled
3. Review the prompts in backend/main.py
4. Try with a different model

### Slow Performance

For faster processing:
1. Use smaller image sizes
2. Reduce the number of images
3. Increase Ollama's GPU resources if available
4. Process images in smaller batches

## Use Cases

- **Accessibility**: Generate alt text for images
- **Content Management**: Create descriptions for image libraries
- **AI Training**: Generate caption datasets for training
- **Social Media**: Auto-generate captions for posts
- **E-commerce**: Product descriptions from images
- **Education**: Visual content descriptions for learning

## Important Notes

- All processing happens locally - no data is sent to external servers
- Caption quality depends on image clarity and content
- LLaVA is a vision-language model optimized for image understanding
- Captions are AI-generated and should be reviewed for accuracy
- This tool provides captions but not accessibility certification

## License

This project is part of the School of AI curriculum.
