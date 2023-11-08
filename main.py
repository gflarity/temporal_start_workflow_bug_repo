from temporalio.client import Client
from my_workflow import GreetingWorkflow

async def create_greeting(client: Client) -> str:
    # Start the workflow
    handle = await client.start_workflow(GreetingWorkflow.run, "my name", id="my-workflow-id", task_queue="my-task-queue")
    # Change the salutation
    await handle.signal(GreetingWorkflow.update_salutation, "Aloha")
    # Tell it to complete
    await handle.signal(GreetingWorkflow.complete_with_greeting)
    # Wait and return result
    return await handle.result()

