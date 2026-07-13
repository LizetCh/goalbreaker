import json
from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
from google import genai
from google.genai import types

from schemas import GoalPrompt, SubtaskModel, StoryModel, EpicModel

load_dotenv()

app = FastAPI()

# Initialize GenAI client
client = genai.Client()


@app.post("/breakdown")
async def breakdown_goal(request: GoalPrompt):

    if not request.goal.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Goal cannot be empty.")

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[
                "You are a Product Owner, expert in Agile methodologies."
                "Your task is to receive a goal and break it down"
                " into an Epic, Stories, and Subtasks."
                "Estimate story points for each story (using Fibonacci sequence: 1, 2, 3, 5, 8),"
                "if the story is bigger than 8 story points, break it down into smaller stories."
                "For each story, provide a list of subtasks."
                f"Break down this goal: {request.goal}"
            ],
            config=types.GenerateContentConfig(
                # json response following EpicModel schema
                response_mime_type="application/json",
                response_schema=EpicModel,
            ),
        )
        structured_data = json.loads(response.text)
        return structured_data

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error with Gemini API: {str(e)}")
