#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from PIL import Image
import google.generativeai as genai

from image_analyzer.crew import ImageAnalyzer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def analyze_image_with_gemini(image_path):
    genai.configure(api_key=os.getenv("api key will be here"))

    model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17") 
    image = Image.open(image_path)

    prompt = (
        "What is happening in this screenshot? "
        "Describe the contents, charts, UI, graphs, and what the user is likely seeing or doing. "
        "If there is a graph, interpret it clearly."
    )

    response = model.generate_content([image, prompt])
    return response.text.strip()


def run():
    image_path = ("")
    #input("enter the path to your screenshot ->  ").strip()

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ The file at {image_path} does not exist.")

    print(f"[+] Analyzing image at: {image_path}")
    summary = analyze_image_with_gemini(image_path)

    inputs = {
        "image_summary": summary,
        "current_year": str(datetime.now().year)
    }

    try:
        ImageAnalyzer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# Optional CLI utilities (same as before)
def train():
    inputs = {
        "image_summary": "Placeholder summary for training.",
        "current_year": str(datetime.now().year)
    }
    try:
        ImageAnalyzer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred during training: {e}")


def replay():
    try:
        ImageAnalyzer().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Replay error: {e}")


def test():
    inputs = {
        "image_summary": "Placeholder summary for testing.",
        "current_year": str(datetime.now().year)
    }
    try:
        ImageAnalyzer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"Test error: {e}")


if __name__ == "__main__":
    run()

