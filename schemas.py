from pydantic import BaseModel


class TaskCreateS(BaseModel):
	title: str
	description: str
	

class TaskUpdateS(TaskCreateS):
	status: bool