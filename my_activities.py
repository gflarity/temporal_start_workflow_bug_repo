from dataclasses import dataclass
from temporalio import activity

@dataclass
class GreetingInfo:
    salutation: str = "Hello"
    name: str = "<unknown>"

@activity.defn
def create_greeting_activity(info: GreetingInfo) -> str:
    return f"{info.salutation}, {info.name}!"
