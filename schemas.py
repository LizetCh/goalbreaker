from pydantic import BaseModel
from typing import List


# user's prompt (goal)
class GoalPrompt(BaseModel):
    goal: str


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
