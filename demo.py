"""
AI-102 Azure AI Vision Unified Demo
===================================

Comprehensive demonstration of Azure AI Vision services for AI-102 exam preparation.
Combines Image Analysis, OCR, and Face Detection with both educational and real API modes.

Features:
- Educational mode: Perfect for presentations and learning
- Production mode: Uses real Face API when credentials are available
- Automatic fallback: If Face API not configured, uses educational content
"""

import os
import sys
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential


def print_header():
    """Print demo header"""
    print("=" * 80)
    print("🎯 AI-102 Azure AI Vision Demo")
    print("=" * 80)
    print("\n🏢 Story: Smart Office Security System")
    print("Demonstrating three Azure AI Vision services:")
    print("1️⃣  Image Analysis - Scene understanding")
    print("2️⃣  OCR - Text extraction from images")
    print("3️⃣  Face Analysis - Face detection & attributes")
    print("\n" + "=" * 80)


def check_face_api_available():
    """Check if Face API credentials are configured"""
    try:
        load_dotenv()
        face_endpoint = os.getenv('FACE_ENDPOINT')
        face_key = os.getenv('FACE_KEY')
        
        if face_endpoint and face_key:
            # Try to import Face SDK
            from azure.ai.vision.face import FaceClient
            return True
        return False
    except ImportError:
        return False
    except Exception:
        return False


def demo_image_analysis():
    """Demo 1: Image Analysis with real Computer Vision API"""
    print("\n📖 CHAPTER 1: IMAGE ANALYSIS")
    print("=" * 60)
    print("🎬 Scenario: Visitor enters office lobby")
    print("🤖 AI Task: Analyze scene and detect objects/people")
    print("🔍 Analyzing: street.jpg")
    
    try:
        from azure.cognitiveservices.vision.computervision import ComputerVisionClient
        from msrest.authentication import CognitiveServicesCredentials
        load_dotenv()
        
        # Get Computer Vision credentials
        cv_endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')
        cv_key = os.getenv('COMPUTER_VISION_KEY')
        
        if not cv_endpoint or not cv_key:
            print("❌ Computer Vision credentials not found, using educational mode")
            demo_image_analysis_educational()
            return
            
        # Initialize Computer Vision client
        cv_credentials = CognitiveServicesCredentials(cv_key)
        cv_client = ComputerVisionClient(cv_endpoint, cv_credentials)
        
        # Use the actual image from the local images folder
        image_path = "images/street.jpg"
        
        # Real Computer Vision API call
        with open(image_path, "rb") as image_data:
            analysis = cv_client.analyze_image_in_stream(
                image_data,
                visual_features=[
                    'Categories', 'Description', 'Objects', 'Tags', 'Adult'
                ]
            )
        
        # Display real results
        if analysis.description.captions:
            caption = analysis.description.captions[0]
            confidence = caption.confidence * 100
            print(f"\n🏷️  CAPTION: '{caption.text}'")
            print(f"   Confidence: {confidence:.1f}%")
        
        if analysis.tags:
            print("\n🏷️  TOP TAGS:")
            for tag in analysis.tags[:5]:
                confidence = tag.confidence * 100
                print(f"   • {tag.name} ({confidence:.1f}%)")
        
        if analysis.objects:
            print(f"\n📦 OBJECTS: Found {len(analysis.objects)}")
            for obj in analysis.objects[:5]:
                confidence = obj.confidence * 100
                print(f"   • {obj.object_property} ({confidence:.1f}%)")
        
        # Count people in objects
        people_count = sum(1 for obj in analysis.objects
                          if 'person' in obj.object_property.lower())
        print(f"\n� PEOPLE: Detected {people_count}")
        
        print("\n✅ Real Computer Vision API working!")
        
    except FileNotFoundError:
        print(f"\n❌ Image file not found: {image_path}")
        demo_image_analysis_educational()
    except Exception as e:
        print(f"\n❌ Computer Vision API Error: {str(e)}")
        demo_image_analysis_educational()
    
    print("\n💡 AI-102 KEY CONCEPTS:")
    print("   🎯 Visual Features: Choose analysis type (caption, tags, objects)")
    print("   📊 Confidence Scores: 0.0 to 1.0 reliability measure")
    print("   📍 Bounding Boxes: Object locations (x, y, width, height)")
    print("   ⚡ Synchronous Processing: Real-time analysis")


def demo_image_analysis_educational():
    """Fallback educational mode for image analysis"""
    print("\n🏷️  CAPTION: 'a man walking a dog on a leash'")
    print("   Confidence: 83.1%")
    
    print("\n🏷️  TOP TAGS:")
    print("   • outdoor (99.9%)")
    print("   • land vehicle (98.9%)")
    print("   • vehicle (98.8%)")
    print("   • building (98.3%)")
    print("   • road (96.8%)")
    
    print("\n📦 OBJECTS: Found 4")
    print("   • car (79.7%)")
    print("   • taxi (79.3%)")
    print("   • person (79.1%)")
    
    print("\n👥 PEOPLE: Detected 1")
    
    print("\n💡 Educational Mode: Computer Vision API not configured")
    print("   ⚡ Synchronous Processing: Real-time analysis")


def demo_ocr():
    """Demo 2: OCR Text Extraction with real Computer Vision API"""
    print("\n📖 CHAPTER 2: OCR (OPTICAL CHARACTER RECOGNITION)")
    print("=" * 60)
    print("🎬 Scenario: Security badge scanner at entrance")
    print("🤖 AI Task: Extract text from visitor's ID badge")
    print("🔍 Analyzing: Business-card.jpg")
    
    try:
        from azure.cognitiveservices.vision.computervision import ComputerVisionClient
        from msrest.authentication import CognitiveServicesCredentials
        import time
        load_dotenv()
        
        # Get Computer Vision credentials
        cv_endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')
        cv_key = os.getenv('COMPUTER_VISION_KEY')
        
        if not cv_endpoint or not cv_key:
            print("❌ Computer Vision credentials not found, using educational mode")
            demo_ocr_educational()
            return
            
        # Initialize Computer Vision client
        cv_credentials = CognitiveServicesCredentials(cv_key)
        cv_client = ComputerVisionClient(cv_endpoint, cv_credentials)
        
        # Use the actual image from the local images folder
        image_path = "images/Business-card.jpg"
        
        # Real OCR API call using Read API
        with open(image_path, "rb") as image_data:
            read_operation = cv_client.read_in_stream(image_data, raw=True)
        
        # Get operation ID from headers
        operation_id = read_operation.headers["Operation-Location"].split("/")[-1]
        
        # Poll for results
        print("   Processing text extraction...")
        while True:
            result = cv_client.get_read_result(operation_id)
            if result.status not in ['notStarted', 'running']:
                break
            time.sleep(1)
        
        # Display real results
        if result.status == 'succeeded':
            print("\n📝 EXTRACTED TEXT:")
            line_num = 1
            for page in result.analyze_result.read_results:
                for line in page.lines:
                    confidence = getattr(line, 'confidence', 0.95) * 100
                    print(f"   Line {line_num}: '{line.text}' "
                          f"(confidence: {confidence:.1f}%)")
                    line_num += 1
                    if line_num > 6:  # Limit output for demo
                        break
        else:
            print(f"\n❌ OCR failed with status: {result.status}")
            demo_ocr_educational()
            return
        
        print("\n✅ Real OCR API working!")
        
    except FileNotFoundError:
        print(f"\n❌ Image file not found: {image_path}")
        demo_ocr_educational()
    except Exception as e:
        print(f"\n❌ OCR API Error: {str(e)}")
        demo_ocr_educational()
    
    print("\n💡 AI-102 KEY CONCEPTS:")
    print("   📖 Read API: Best for documents and printed text")
    print("   🔄 Async Processing: For large documents")
    print("   🌍 Language Detection: 73+ languages supported")
    print("   📐 Bounding Polygons: Exact text location coordinates")


def demo_ocr_educational():
    """Fallback educational mode for OCR"""
    print("\n📝 EXTRACTED TEXT:")
    print("   Line 1: 'Dr. Sarah Chen' (confidence: 99.8%)")
    print("   Line 2: 'Senior Data Scientist' (confidence: 99.5%)")
    print("   Line 3: 'Microsoft Corporation' (confidence: 99.9%)")
    print("   Line 4: 'sarah.chen@microsoft.com' (confidence: 98.7%)")
    
    print("\n💡 Educational Mode: Computer Vision API not configured")
    print("   📐 Bounding Polygons: Exact text location coordinates")


def demo_face_analysis():
    """Demo 3: Face Analysis - Auto-detects API availability"""
    print("\n📖 CHAPTER 3: FACE ANALYSIS")
    print("=" * 60)
    print("🎬 Scenario: Facial recognition access control")
    print("🤖 AI Task: Detect faces and analyze attributes")
    
    # Check if real Face API is available
    if check_face_api_available():
        print("🔍 Using REAL Face API")
        demo_face_analysis_real()
    else:
        print("🔍 Using EDUCATIONAL mode (Face API not configured)")
        demo_face_analysis_educational()


def demo_face_analysis_real():
    """Real Face API demonstration"""
    try:
        from azure.ai.vision.face import FaceClient
        load_dotenv()
        
        face_endpoint = os.getenv('FACE_ENDPOINT')
        face_key = os.getenv('FACE_KEY')
        
        face_client = FaceClient(
            endpoint=face_endpoint,
            credential=AzureKeyCredential(face_key)
        )
        
        print("🔍 Analyzing: people.jpg")
        
        # Use the actual image from the local images folder
        image_path = "images/people.jpg"
        
        # Real Face API call - basic face detection only
        # Note: Advanced features require Microsoft approval
        with open(image_path, "rb") as image_data:
            detected_faces = face_client.detect(
                image_data,
                detection_model="detection_03",
                recognition_model="recognition_04",
                return_face_id=False,
                return_face_attributes=["glasses", "headPose"],
                return_face_landmarks=True
            )
        
        print("\n👤 FACE DETECTION RESULTS:")
        print(f"   Faces detected: {len(detected_faces)}")
        
        for i, face in enumerate(detected_faces, 1):
            rect = face.face_rectangle
            attrs = face.face_attributes
            
            print("   ")
            print(f"   Face {i}:")
            print(f"   • Glasses: {attrs.glasses}")
            
            # Head pose information
            head_pose = attrs.head_pose
            print(f"   • Head Yaw: {head_pose.yaw:.1f}° "
                  f"(left/right turn)")
            
            coords = f"{rect.left}, {rect.top}, {rect.width}, {rect.height}"
            print(f"   • Location: ({coords})")
            
            # Show key landmarks if available
            if face.face_landmarks:
                landmarks = face.face_landmarks
                nose_tip = landmarks.nose_tip
                print(f"   • Nose Tip: ({nose_tip.x:.0f}, {nose_tip.y:.0f})")
                
                left_eye = landmarks.pupil_left
                right_eye = landmarks.pupil_right
                print(f"   • Eyes: Left({left_eye.x:.0f}, {left_eye.y:.0f}), "
                      f"Right({right_eye.x:.0f}, {right_eye.y:.0f})")
        
        print("\n✅ Real Face API working!")
        
        print("\n💡 AI-102 KEY CONCEPTS:")
        print("   👤 Face Detection: Locate faces in images")
        print("   📊 Face Attributes: Age, gender, emotion, accessories")
        print("   📍 Face Rectangle: Bounding box coordinates")
        print("   🔒 Privacy: Face detection ≠ face recognition")
        print("   ⚖️ Compliance: Follow responsible AI guidelines")
        
    except FileNotFoundError:
        print(f"\n❌ Image file not found: {image_path}")
        print("   Using sample data for demonstration...")
        demo_face_analysis_educational()
    except Exception as e:
        print(f"\n❌ Face API Error: {str(e)}")
        print("   Falling back to educational mode...")
        demo_face_analysis_educational()


def demo_face_analysis_educational():
    """Educational face analysis demonstration"""
    print("🔍 Analyzing: people.jpg")
    
    print("\n👤 FACE DETECTION RESULTS (Simulated):")
    print("   Faces detected: 2")
    print("   ")
    print("   Face 1:")
    print("   • Age: 32 ± 5 years")
    print("   • Gender: Female")
    print("   • Emotion: Happy (85.2%)")
    print("   • Glasses: None")
    print("   • Location: (145, 67, 120, 160)")
    print("   ")
    print("   Face 2:")
    print("   • Age: 28 ± 4 years")
    print("   • Gender: Male")
    print("   • Emotion: Neutral (76.8%)")
    print("   • Glasses: Reading")
    print("   • Location: (289, 73, 115, 154)")
    
    print("\n💡 AI-102 KEY CONCEPTS:")
    print("   👤 Face Detection: Locate faces in images")
    print("   📊 Face Attributes: Age, gender, emotion, accessories")
    print("   📍 Face Landmarks: 27-point facial feature coordinates")
    print("   🔒 Privacy: Face detection ≠ face recognition")
    print("   ⚖️ Compliance: Follow responsible AI guidelines")


def show_ai102_tips():
    """Show AI-102 exam tips"""
    print("\n📚 AI-102 EXAM TIPS")
    print("=" * 60)
    print("\n🎯 IMAGE ANALYSIS:")
    print("   • Know the difference between v3.2 and v4.0 APIs")
    print("   • Understand confidence thresholds (default 0.5)")
    print("   • Memorize visual feature types: Categories, Tags, Description, etc.")
    print("   • Practice bounding box coordinate interpretation")
    
    print("\n📖 OCR:")
    print("   • Read API vs Computer Vision OCR - know when to use each")
    print("   • Understand async operations for large documents")
    print("   • Know language support limitations")
    print("   • Practice polygon coordinate systems")
    
    print("\n👤 FACE API:")
    print("   • Face detection vs face recognition licensing")
    print("   • Understand emotion detection capabilities")
    print("   • Know privacy and compliance requirements")
    print("   • Practice face attribute interpretation")
    
    print("\n⚡ GENERAL:")
    print("   • Understand service limits and pricing tiers")
    print("   • Know regional availability for different versions")
    print("   • Practice error handling and status codes")
    print("   • Understand when to use batch vs single operations")


def show_integration_story():
    """Show how services integrate"""
    print("\n🔗 INTEGRATION STORY")
    print("=" * 60)
    print("\n🏢 Smart Office Security System:")
    print("   ")
    print("   📹 Step 1: Camera captures visitor at entrance")
    print("   🔍 Step 2: Image Analysis identifies 'person' in lobby")
    print("   📋 Step 3: OCR reads visitor badge information")
    print("   👤 Step 4: Face Analysis confirms human presence")
    print("   ✅ Step 5: System grants/denies access based on analysis")
    print("   ")
    print("   💡 All three services work together for comprehensive security!")


def show_face_setup_guide():
    """Show complete Azure setup instructions"""
    print("\n🛠️ COMPLETE AZURE SETUP GUIDE")
    print("=" * 60)
    print("\n📋 This demo requires three Azure AI services:")
    print("   ")
    print("   🔍 Computer Vision - Image Analysis + OCR")
    print("   👤 Face API - Face detection and attributes")
    print("   📍 Same resource group and region for all services")
    print("   ")
    print("   📚 Complete setup instructions with Microsoft Learn exercises:")
    print("   👉 See DEMO_GUIDE.md - 'COMPLETE AZURE SETUP GUIDE' section")
    print("   ")
    print("   ⚡ Quick Setup Summary:")
    print("   1. Create resource group: 'ai102-vision-rg'")
    print("   2. Create Computer Vision resource (East US recommended)")
    print("   3. Create Face API resource (same region)")
    print("   4. Copy endpoints and keys to .env file")
    print("   5. Install dependencies: pip install -r requirements.txt")
    print("   6. Test: python demo.py all")
    print("   ")
    print("   ✅ Demo auto-detects services and shows status!")
    print("   💡 Follow Microsoft Learn exercises for detailed walkthrough")


def main():
    """Main demo function with auto-detection"""
    if len(sys.argv) < 2:
        face_status = "✅ REAL API" if check_face_api_available() else "📚 EDUCATIONAL"
        
        print("AI-102 Azure Vision Demo")
        print(f"\nFace API Status: {face_status}")
        print("\nUsage: python demo.py <mode>")
        print("\nModes:")
        print("  all      - Complete demo (recommended)")
        print("  image    - Image analysis only")
        print("  ocr      - Text extraction only")
        print("  faces    - Face analysis (auto-detects API)")
        print("  tips     - AI-102 exam tips")
        print("  story    - Integration story")
        print("  setup    - Complete Azure setup guide")
        print("\nExample: python demo.py all")
        print("\n💡 Need Azure setup? See DEMO_GUIDE.md or run: python demo.py setup")
        return
    
    print_header()
    mode = sys.argv[1].lower()
    
    try:
        if mode == "all":
            face_mode = "real Face API" if check_face_api_available() else "educational mode"
            print(f"\n🎬 Running complete AI-102 demo with {face_mode}...")
            demo_image_analysis()
            demo_ocr()
            demo_face_analysis()
            show_integration_story()
            
        elif mode == "image":
            demo_image_analysis()
            
        elif mode == "ocr":
            demo_ocr()
            
        elif mode == "faces":
            demo_face_analysis()
            
        elif mode == "tips":
            show_ai102_tips()
            
        elif mode == "story":
            show_integration_story()
            
        elif mode == "setup":
            show_face_setup_guide()
            
        else:
            print(f"❌ Unknown mode: {mode}")
            print("Run 'python demo.py' for usage information")
            return
            
        print("\n" + "=" * 80)
        print("🎯 Demo complete! Ready for your AI-102 exam! 🚀")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Demo error: {str(e)}")
        print("💡 Run 'python test_credentials.py' to check your Azure setup")


if __name__ == "__main__":
    main()
