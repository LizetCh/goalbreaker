
from pydantic import BaseModel, Field
from typing import List


# user's prompt (goal)
class GoalPrompt(BaseModel):
    goal: str = Field(
        ...,
        description="The high-level technical or business goal to decompose.",
        examples=[
            "Build a secure and scalable shopping cart system for an e-commerce platform."]
    )


# subtask model
class SubtaskModel(BaseModel):
    title: str


# story model
class StoryModel(BaseModel):
    title: str
    story_points: int
    subtasks: List[SubtaskModel]


# Epic model
class EpicModel(BaseModel):
    title: str
    stories: List[StoryModel]
