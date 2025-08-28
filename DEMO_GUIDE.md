# AI-102 Vision Demo: Complete Presentation Guide

## 🎯 Demo Overview
**Duration**: 20-25 minutes  
**Audience**: AI-102 exam study group  
**Objective**: Master all three Azure AI Vision services through storytelling  
**Story**: Smart Office Security System

---

## 🛠️ COMPLETE AZURE SETUP GUIDE
### All Three AI Vision Services (15 minutes setup)

This setup follows the official Microsoft Learn exercises and creates all resources needed for the demo.

### **Prerequisites**
- Azure subscription (free tier works fine)
- Azure CLI or Azure Portal access
- Basic understanding of Azure resource groups

---

### **Step 1: Create Resource Group** (2 minutes)

**Portal Method:**
1. Go to [Azure Portal](https://portal.azure.com/)
2. Click **Resource groups** → **Create**
3. **Resource group name**: `ai102-vision-rg`
4. **Region**: **East US** (recommended for AI-102)
5. Click **Review + create** → **Create**

**Azure CLI Method:**
```bash
az group create --name ai102-vision-rg --location eastus
```

---

### **Step 2: Computer Vision Resource** (5 minutes)
*For Image Analysis + OCR services*

**Based on**: [Microsoft Learn - Analyze images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/)

**Portal Setup:**
1. **Create resource** → **AI + Machine Learning** → **Computer Vision**
2. **Resource details:**
   - **Subscription**: Your subscription
   - **Resource group**: `ai102-vision-rg`
   - **Region**: **East US** (for Azure AI Vision 4.0 support)
   - **Name**: `ai102-computer-vision` (must be globally unique)
   - **Pricing tier**: **Free F0** (20 transactions/minute) or **Standard S1**

3. **Review + create** → **Create**
4. **Wait for deployment** (2-3 minutes)

**Get Credentials:**
1. Go to your Computer Vision resource
2. **Keys and Endpoint** (left menu)
3. **Copy**:
   - **KEY 1** (or KEY 2)
   - **Endpoint** (e.g., `https://ai102-computer-vision.cognitiveservices.azure.com/`)

**Azure CLI Method:**
```bash
# Create Computer Vision resource
az cognitiveservices account create \
  --name ai102-computer-vision \
  --resource-group ai102-vision-rg \
  --kind ComputerVision \
  --sku F0 \
  --location eastus \
  --yes

# Get endpoint and key
az cognitiveservices account show \
  --name ai102-computer-vision \
  --resource-group ai102-vision-rg \
  --query "properties.endpoint"

az cognitiveservices account keys list \
  --name ai102-computer-vision \
  --resource-group ai102-vision-rg
```

---

### **Step 3: Face API Resource** (5 minutes)
*For Face Detection and Analysis*

**Based on**: [Microsoft Learn - Detect faces in images](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/)

**Portal Setup:**
1. **Create resource** → **AI + Machine Learning** → **Face**
2. **Resource details:**
   - **Subscription**: Your subscription
   - **Resource group**: `ai102-vision-rg`
   - **Region**: **East US** (same as Computer Vision)
   - **Name**: `ai102-face-api` (must be globally unique)
   - **Pricing tier**: **Free F0** (20 transactions/minute) or **Standard S1**

3. **Review + create** → **Create**
4. **Wait for deployment** (2-3 minutes)

**Get Credentials:**
1. Go to your Face resource
2. **Keys and Endpoint** (left menu)
3. **Copy**:
   - **KEY 1** (or KEY 2)
   - **Endpoint** (e.g., `https://ai102-face-api.cognitiveservices.azure.com/`)

**Azure CLI Method:**
```bash
# Create Face API resource
az cognitiveservices account create \
  --name ai102-face-api \
  --resource-group ai102-vision-rg \
  --kind Face \
  --sku F0 \
  --location eastus \
  --yes

# Get endpoint and key
az cognitiveservices account show \
  --name ai102-face-api \
  --resource-group ai102-vision-rg \
  --query "properties.endpoint"

az cognitiveservices account keys list \
  --name ai102-face-api \
  --resource-group ai102-vision-rg
```

---

### **Step 4: Configure Environment Variables** (3 minutes)

**Update your `.env` file:**
```bash
# Computer Vision (for Image Analysis + OCR)
AI_SERVICE_ENDPOINT=https://ai102-computer-vision.cognitiveservices.azure.com/
AI_SERVICE_KEY=your_computer_vision_key_here

# Face API (for Face Detection)
FACE_ENDPOINT=https://ai102-face-api.cognitiveservices.azure.com/
FACE_KEY=your_face_api_key_here
```

**Security Best Practices:**
- Never commit `.env` file to version control
- Use `.env.example` as a template for team members
- Consider Azure Key Vault for production deployments

---

### **Step 5: Install Dependencies & Test** (2 minutes)

**Install Required Packages:**
```bash
pip install -r requirements.txt
```

**Test All Services:**
```bash
# Test complete setup
python demo.py all

# Test individual services
python demo.py image    # Test Computer Vision
python demo.py ocr      # Test OCR
python demo.py faces    # Test Face API
```

**Expected Output:**
- **Image Analysis**: Should show caption, tags, objects, people
- **OCR**: Should extract text with confidence scores
- **Face API**: Should show "✅ REAL API" and detect faces with attributes

---

### **Troubleshooting Common Issues**

#### **1. "Access Denied" or "401 Unauthorized"**
- **Check**: Endpoint URLs are correct (no trailing slashes)
- **Check**: API keys are copied correctly (no extra spaces)
- **Check**: Resource region matches your subscription region

#### **2. "Resource Not Found" or "404"**
- **Check**: Resource names are globally unique
- **Check**: Resources are in the same region
- **Check**: Deployment completed successfully

#### **3. "Face API Not Working"**
- **Check**: Face API has stricter regional availability
- **Check**: Some regions require additional permissions
- **Check**: Face SDK is installed: `pip install azure-ai-vision-face`

#### **4. "Rate Limit Exceeded"**
- **Free tier**: 20 calls/minute limit
- **Solution**: Wait 1 minute or upgrade to Standard tier
- **Demo tip**: Don't run commands too rapidly

---

### **Cost Management & Cleanup**

#### **Free Tier Limits:**
- **Computer Vision F0**: 5,000 transactions/month, 20/minute
- **Face API F0**: 30,000 transactions/month, 20/minute
- **Perfect for**: Learning, demos, AI-102 exam prep

#### **After Demo/Study:**
```bash
# Delete all resources to avoid charges
az group delete --name ai102-vision-rg --yes --no-wait
```

#### **Cost Monitoring:**
- Set up billing alerts in Azure Portal
- Monitor usage in Azure Cost Management
- Free tier usually sufficient for AI-102 prep

---

### **Reference: Microsoft Learn Exercises**

#### **📚 Computer Vision Exercises:**
1. **[Exercise - Analyze images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/3-analyze-images)**
2. **[Exercise - Generate thumbnails with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/5-generate-thumbnails)**

#### **📖 OCR Exercises:**
1. **[Exercise - Extract text from images](https://learn.microsoft.com/en-us/training/modules/read-text-computer-vision/3-ocr-azure)**
2. **[Exercise - Read text with Read API](https://learn.microsoft.com/en-us/training/modules/read-text-computer-vision/5-read-api)**

#### **👤 Face API Exercises:**
1. **[Exercise - Detect faces with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/3-detect-faces)**
2. **[Exercise - Understand face analysis](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/5-face-analysis)**

#### **🔗 Integration Examples:**
1. **[Build a computer vision solution](https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/)**
2. **[AI-102 Learning Path](https://learn.microsoft.com/en-us/training/browse/?products=azure&roles=ai-engineer)**

---

### **✅ Setup Verification Checklist**

**Before your demo, verify:**
- [ ] Resource group `ai102-vision-rg` created
- [ ] Computer Vision resource deployed and accessible
- [ ] Face API resource deployed and accessible  
- [ ] `.env` file configured with correct endpoints and keys
- [ ] All Python dependencies installed
- [ ] `python demo.py all` runs successfully
- [ ] Face API shows "✅ REAL API" status
- [ ] All three services return data (not just educational mode)

**Your setup is complete when `python demo.py` shows:**
```
Face API Status: ✅ REAL API
```

**Now you're ready for the complete AI-102 vision services demo!** 🚀

---

## 🎬 THE COMPLETE OFFICE SECURITY STORY

### **Opening Script** (3 minutes)

**Say This:**
> "Today we're going to explore the three core Azure AI Vision services for the AI-102 exam through a real-world story. Imagine you're designing a smart office security system for Microsoft's headquarters. We need three AI capabilities working together."

**Key Points to Emphasize:**
- These three services often work together in production
- Understanding their integration is crucial for AI-102
- Each service has specific strengths and use cases

**Show the services:**
1. **Azure AI Vision (Image Analysis)** - Scene understanding, object detection
2. **Azure AI Vision (OCR)** - Text extraction from documents  
3. **Azure Face API** - Face detection and attribute analysis

---

## 🏢 CHAPTER 1: VISITOR ENTERS LOBBY
### Image Analysis Demo (7 minutes)

**Story Setup:**
> "It's Monday morning. A visitor approaches the Microsoft office building. Our security camera captures them entering the lobby. The AI system needs to understand: What's happening in this scene?"

**Run Command:**
```bash
python demo.py image
```

**What You'll See & What to Explain:**

#### 1. **Caption Generation**
```
🏷️ CAPTION: 'a man walking a dog on a leash'
   Confidence: 83.1%
```

**Explain to Group:**
- **AI-102 Key Concept**: Caption vs Description features
- **Confidence Scores**: Range 0.0-1.0, default threshold usually 0.5
- **Real-world Use**: Automated security logs, accessibility features

#### 2. **Tag Detection**
```
🏷️ TOP TAGS:
   • outdoor (99.9%)
   • land vehicle (98.9%)
   • vehicle (98.8%)
```

**Explain to Group:**
- **AI-102 Key Concept**: Tags vs Objects - tags are general concepts, objects have locations
- **Confidence Hierarchy**: Higher confidence = more reliable detection
- **Exam Tip**: Know the difference between tags, categories, and objects

#### 3. **Object Detection**
```
📦 OBJECTS: Found 4
   • car (79.7%)
   • taxi (79.3%)
   • person (79.1%)
```

**Explain to Group:**
- **AI-102 Key Concept**: Bounding boxes provide (x, y, width, height) coordinates
- **Use Case**: Object tracking, automated counting, spatial analysis
- **Important**: Objects have locations, tags don't

#### 4. **People Detection**
```
👥 PEOPLE: Detected 1
```

**Explain to Group:**
- **AI-102 Key Concept**: Specialized people detection vs general object detection
- **Privacy Consideration**: People detection ≠ face recognition
- **Azure AI Vision 4.0**: Enhanced people detection capabilities

**Story Transition:**
> "Great! Our system detected a person entering. Now we need to verify their identity by reading their visitor badge..."

---

## 📋 CHAPTER 2: ID BADGE SCANNING
### OCR Demo (7 minutes)

**Story Setup:**
> "The visitor approaches the reception desk and presents their visitor badge. Our OCR system needs to extract the text information to verify their identity and log their visit."

**Run Command:**
```bash
python demo.py ocr
```

**What You'll See & What to Explain:**

#### 1. **Text Extraction Results**
```
📝 EXTRACTED TEXT:
   Line 1: 'Dr. Sarah Chen' (confidence: 99.8%)
   Line 2: 'Senior Data Scientist' (confidence: 99.5%)
   Line 3: 'Microsoft Corporation' (confidence: 99.9%)
   Line 4: 'sarah.chen@microsoft.com' (confidence: 98.7%)
```

**Explain to Group:**
- **AI-102 Key Concept**: Read API vs Computer Vision OCR API differences
- **Confidence Per Line**: Each text line has individual confidence scores
- **Real-world Use**: Document processing, form automation, badge scanning

#### 2. **OCR Technology Deep Dive**

**Critical AI-102 Exam Points:**

**Read API vs Computer Vision OCR:**
- **Read API**: Better for documents, supports more languages (73+)
- **Computer Vision OCR**: Real-time, synchronous, good for signs/short text
- **Exam Tip**: Know when to use which API

**Language Support:**
- **Read API**: 73+ languages including handwriting
- **Auto-detection**: Automatically detects language
- **Exam Tip**: Understand regional availability and language limitations

**Processing Modes:**
- **Synchronous**: Real-time processing for small images
- **Asynchronous**: Batch processing for large documents
- **Exam Tip**: Know the file size and processing time limits

#### 3. **Bounding Polygon Coordinates**

**Explain to Group:**
- **AI-102 Key Concept**: Text has polygon coordinates (not just rectangles)
- **Use Case**: Precise text location for form field extraction
- **Integration**: Combine with other services for complete document understanding

**Story Transition:**
> "Perfect! We've identified Dr. Sarah Chen from Microsoft. Now our final security check - facial analysis to confirm this is a human visitor and not a photo or fake ID..."

---

## 👤 CHAPTER 3: FACIAL SECURITY CHECK
### Face Analysis Demo (8 minutes)

**Story Setup:**
> "As our final security verification, we need to analyze the visitor's face. This isn't face recognition - we're just detecting face attributes to ensure this is a real person and gather basic demographic data for our security logs."

**Run Command:**
```bash
python demo.py faces
```

**What You'll See & What to Explain:**

#### 1. **Auto-Detection Feature**
The demo will show either:
- `🔍 Using REAL Face API` (if configured)
- `🔍 Using EDUCATIONAL mode` (if not configured)

**Explain to Group:**
- **Smart Demo Feature**: Automatically detects available services
- **Real-world Relevance**: Production systems need graceful fallbacks

#### 2. **Face Detection Results**
```
👤 FACE DETECTION RESULTS:
   Faces detected: 2

   Face 1:
   • Age: 32 ± 5 years
   • Gender: Female
   • Emotion: Happy (85.2%)
   • Glasses: None
   • Location: (145, 67, 120, 160)
```

**Critical AI-102 Exam Points to Explain:**

#### **Face Detection vs Face Recognition**
- **Face Detection**: Locates faces, analyzes attributes (what we're doing)
- **Face Recognition**: Identifies specific individuals (requires special permissions)
- **Exam Tip**: Know the licensing and compliance differences

#### **Face Attributes Available**
- **Age**: Range estimation with confidence intervals
- **Gender**: Male/Female classification
- **Emotion**: Happy, sad, neutral, angry, surprise, fear, contempt, disgust
- **Accessories**: Glasses, headwear, mask detection
- **Facial Hair**: Beard, mustache, sideburns detection

#### **Privacy and Compliance**
- **Responsible AI**: Face API has strict usage guidelines
- **Data Retention**: Microsoft doesn't store face data
- **Regional Restrictions**: Some regions have limited access
- **Exam Tip**: Understand compliance requirements for face services

#### 3. **Bounding Box Coordinates**
```
• Location: (145, 67, 120, 160)
```

**Explain to Group:**
- **Format**: (x, y, width, height) in pixels
- **Use Case**: Cropping faces, privacy masking, overlay graphics
- **Integration**: Combine with other vision services for complete analysis

**Story Conclusion:**
> "Excellent! Our smart office security system has successfully: (1) Detected a person entering, (2) Read and verified their visitor badge, and (3) Confirmed human presence through facial analysis. Dr. Sarah Chen is cleared for entry!"

---

## 🔗 CHAPTER 4: INTEGRATION STORY
### How Services Work Together (3 minutes)

**Run Command:**
```bash
python demo.py story
```

**Integration Explanation:**
> "In production, these three services work together seamlessly. Let me show you the complete workflow..."

**Walk Through The Flow:**
1. **Camera captures** → Image Analysis identifies "person in lobby"
2. **Badge scanner** → OCR extracts visitor information
3. **Security checkpoint** → Face detection confirms human presence
4. **System decision** → Grant/deny access based on all three analyses

**AI-102 Exam Integration Points:**
- **Service Chaining**: Output of one service feeds into another
- **Confidence Thresholds**: Each service has configurable confidence levels
- **Error Handling**: What happens when one service fails?
- **Cost Optimization**: Understand pricing for each service call

---

## 🎯 CHAPTER 5: AI-102 EXAM PREPARATION
### Key Concepts Review (2 minutes)

**Run Command:**
```bash
python demo.py tips
```

**Review These Critical Points:**

### **Image Analysis**
- **API Versions**: v3.2 vs v4.0 capabilities and regional availability
- **Visual Features**: Caption, Description, Tags, Categories, Objects, Faces, Adult content
- **Confidence Thresholds**: Default 0.5, configurable 0.0-1.0
- **Service Limits**: 16MB file size, 16,000x16,000 pixel maximum

### **OCR Services**
- **Read API**: Asynchronous, 73+ languages, handwriting support
- **Computer Vision OCR**: Synchronous, faster for short text
- **Language Detection**: Automatic detection and confidence scores
- **Output Formats**: JSON with text, confidence, and polygon coordinates

### **Face API**
- **Detection vs Recognition**: Licensing and capability differences
- **Attribute Analysis**: Age, gender, emotion, accessories, facial hair
- **Face Landmarks**: 27-point facial coordinate mapping
- **Compliance**: Responsible AI guidelines and regional restrictions

### **General Service Knowledge**
- **Pricing Tiers**: Free (F0) vs Standard (S1) limits and costs
- **Regional Availability**: Not all features available in all regions
- **Error Codes**: Common HTTP status codes and their meanings
- **Batch Operations**: When to use batch vs single image processing

---

## 📝 PRESENTATION TIPS

### **Before You Start**
1. **Complete Azure Setup**: Follow the "COMPLETE AZURE SETUP GUIDE" section above (15 minutes)
2. **Test Everything**: Run `python demo.py all` to ensure all services work
3. **Check Face API**: Verify if you'll get "✅ REAL API" or "📚 EDUCATIONAL" mode
4. **Practice Timing**: Run through once to get comfortable with flow
5. **Review Microsoft Learn**: Quick refresher on the three exercises mentioned in setup

### **During Presentation**
1. **Engage the Audience**: Ask "What do you think this detects?"
2. **Explain While Running**: Don't just read the output, explain the concepts
3. **Connect to Exam**: Always tie back to "This is what you need to know for AI-102"
4. **Show Integration**: Emphasize how services work together

### **After Each Service Demo**
1. **Summarize Key Points**: What did we just learn?
2. **Ask Questions**: "Any questions about confidence scores?"
3. **Preview Next**: "Now let's see how we extract text..."

### **Closing Strong**
> "You now understand the three core Azure AI Vision services. You know when to use each one, how they work together, and what the AI-102 exam expects you to know. Practice these concepts, understand the integration patterns, and you'll be ready for the vision services section of your exam!"

---

## 🎓 POST-DEMO STUDY RESOURCES

### **Microsoft Learn Modules**
1. **[Analyze images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/)**
2. **[Read text in images and documents with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/read-text-computer-vision/)**
3. **[Detect faces in images with Azure AI Vision](https://learn.microsoft.com/en-us/training/modules/detect-analyze-faces/)**

### **Official Documentation**
1. **[Azure AI Vision Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)**
2. **[Face API Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/face/)**
3. **[AI-102 Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-102)**

### **Practice Exercises**
- Run all demo modes: `image`, `ocr`, `faces`, `tips`, `story`
- Try different images if you have them available
- Practice explaining confidence scores and bounding boxes
- Review the integration story multiple times

---

## ✅ SUCCESS CHECKLIST

**Your study group should be able to:**
- [ ] Explain the difference between Image Analysis, OCR, and Face Detection
- [ ] Understand confidence scores and thresholds
- [ ] Know when to use Read API vs Computer Vision OCR
- [ ] Explain face detection vs face recognition
- [ ] Describe how services integrate in real applications
- [ ] Answer AI-102 questions about Azure AI Vision services

**After this demo, your group is ready for the Azure AI Vision section of AI-102!** 🚀
