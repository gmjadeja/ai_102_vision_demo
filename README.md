# AI-102 Azure AI Vision Demo

## 📋 Overview
This comprehensive demo combines three key Azure AI Vision services for AI-102 exam preparation:

1. **Image Analysis** - Scene understanding, object detection, people detection
2. **OCR (Optical Character Recognition)** - Text extraction from images
3. **Face Detection & Analysis** - Face detection with attribute analysis

## 🎬 Story: "Smart Office Security System"
The demo follows a fictional scenario where these three services work together in a modern office building's security and automation system.

## 🚀 Quick Start

### 1. Azure Resource Setup
Create these Azure resources:

#### Computer Vision Resource (for Image Analysis + OCR)
1. Go to [Azure Portal](https://portal.azure.com/)
2. Create resource > AI + Machine Learning > Computer Vision
3. Configure:
   - **Name**: `ai102-vision-[yourname]`
   - **Region**: East US, West Europe, or Southeast Asia (for Azure AI Vision 4.0)
   - **Pricing**: Free F0 (20 calls/minute) or Standard S1

#### Face API Resource (for Face Detection)
1. Create resource > AI + Machine Learning > Face
2. Configure:
   - **Name**: `ai102-face-[yourname]`
   - **Region**: Same as Computer Vision
   - **Pricing**: Free F0 (20 calls/minute)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Update `.env` file with your Azure credentials:
```bash
# Computer Vision
AI_SERVICE_ENDPOINT=https://your-computer-vision.cognitiveservices.azure.com/
AI_SERVICE_KEY=your_computer_vision_key

# Face API
FACE_ENDPOINT=https://your-face-api.cognitiveservices.azure.com/
FACE_KEY=your_face_api_key
```

## 🎯 Running the Demo

### 🎪 Unified Demo (Recommended)
```bash
python demo.py all       # Complete storytelling demo (15-20 min)
python demo.py image     # Image Analysis only
python demo.py ocr       # OCR only
python demo.py faces     # Face Analysis (auto-detects Real vs Educational)
python demo.py tips      # AI-102 exam tips
python demo.py story     # Integration story
python demo.py setup     # Face API setup guide
```

**Smart Features:**
- 🤖 **Auto-Detection**: Automatically uses real Face API if configured, falls back to educational mode
- 📚 **Dual Mode**: Perfect for both learning and production testing
- 🎯 **One File**: All functionality in a single, streamlined demo

## 📖 Presentation Guide

**Duration**: 15-20 minutes  
**Flow**: "Smart office security system" story

1. **Opening** (2 min): Introduce the three Azure AI Vision services
2. **Image Analysis** (5 min): `python demo.py image` - Visitor enters lobby
3. **OCR** (5 min): `python demo.py ocr` - ID card scanning
4. **Face Analysis** (5 min): `python demo.py faces` - Access control
5. **Integration** (3 min): How services work together

### Key AI-102 Concepts to Highlight
- **Image Analysis**: Visual features, confidence scores, bounding boxes
- **OCR**: Read API vs Computer Vision OCR, language support
- **Face Analysis**: Detection vs recognition, attributes, privacy considerations

## 📁 Project Files

- **`demo.py`** - Unified demo with auto-detection (replaces both simple & enhanced)
- **`.env`** - Azure service credentials
- **`requirements.txt`** - Python dependencies

## ⚠️ Known Issues & Solutions

### Visualization Libraries (Optional)
**Issue**: MSYS2 Python has DLL loading conflicts with numpy/matplotlib
**Status**: Demo works perfectly without visualization (comprehensive text output)

**Solutions if you need visualization**:
1. **Standard Windows Python**: Install from python.org instead of MSYS2
2. **Conda**: Create conda environment with `conda install matplotlib pillow numpy`
3. **Continue as-is**: Text output covers all AI-102 requirements

## Current Status ✅

- **All Azure AI Vision services working perfectly**
- **Unified demo with intelligent auto-detection**
- **Ultra-clean project structure with 5 essential files**
- **Environment**: MSYS2 Python 3.12.10 (all AI services functional)

## 🎯 AI-102 Exam Focus Areas

### Image Analysis
- Visual Features selection (caption, tags, objects, people)
- Confidence scores and thresholds
- Bounding box coordinates
- Dense captions vs regular captions

### OCR (Optical Character Recognition)
- Read API vs Computer Vision OCR API
- Asynchronous vs synchronous processing
- Language detection and support
- Bounding polygon coordinates

### Face Analysis
- Face detection vs face recognition
- Face attributes (age, gender, emotion, accessories)
- Face landmarks and geometry
- Privacy and compliance considerations

## Additional Resources

- [AI-102 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-102)
- [Azure AI Vision Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
- [Microsoft Learn - Computer Vision](https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/)
