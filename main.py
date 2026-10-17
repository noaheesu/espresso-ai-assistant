import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY is not set in the .env file.")
    exit(1)

# Initialize the official Google GenAI client
client = genai.Client(api_key=api_key)

def diagnose_espresso():
    print("☕ Welcome to Espresso Extraction & Recipe AI Assistant!")
    print("-" * 50)
    
    # Collect extraction variables from user
    bean_name = input("1. Coffee Bean Name (e.g., Seabright Blend): ")
    grind_size = input("2. Grind Size / Clicks (e.g., 14 clicks): ")
    extract_time = input("3. Extraction Time (e.g., 28 seconds): ")
    taste_note = input("4. Taste Profile / Issues (e.g., Too sour, Astringent, Channeling): ")
    
    print("\n" + "=" * 50)
    print(f"[{bean_name}] Analyzing extraction parameters with Gemini AI...")
    
    # Construct prompt for the AI barista
    prompt = f"""
    You are an expert barista and espresso machine technician.
    Analyze the following espresso extraction parameters and provide professional diagnosis and actionable recipes/adjustments:
    
    - Bean Name: {bean_name}
    - Grind Size: {grind_size}
    - Extraction Time: {extract_time}
    - Taste Profile / Issues: {taste_note}
    
    Please provide your response in English, structured with:
    1. Diagnosis (Why this taste happened)
    2. Recommended Adjustments (Grind size, dose, or ratio changes)
    """
    
    try:
        # Call Gemini model (updated to gemini-3.8-flash)
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=prompt,
        )
        
        print("\n✨ AI Barista Prescription:")
        print(response.text)
        
    except Exception as e:
        print(f"❌ An error occurred while communicating with Gemini: {e}")

if __name__ == "__main__":
    diagnose_espresso()