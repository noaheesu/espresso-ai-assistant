import os

def diagnose_espresso():
    print("☕ Welcome to Espresso Extraction & Recipe AI Assistant!")
    print("-" * 50)
    
    # Collect extraction variables from user
    bean_name = input("1. Coffee Bean Name (e.g., Seabright Blend): ")
    grind_size = input("2. Grind Size / Clicks (e.g., 14 clicks): ")
    extract_time = input("3. Extraction Time (e.g., 28 seconds): ")
    taste_note = input("4. Taste Profile / Issues (e.g., Too sour, Astringent, Channeling): ")
    
    print("\n" + "=" * 50)
    print(f"[{bean_name}] Analyzing extraction parameters...")
    
    # Placeholder for Gemini AI integration
    print(f"• Grind Size: {grind_size}")
    print(f"• Extraction Time: {extract_time}")
    print(f"• Taste Profile: {taste_note}")
    print("\n[Status]: Base structure ready! AI diagnostic model will be connected next.")

if __name__ == "__main__":
    diagnose_espresso()