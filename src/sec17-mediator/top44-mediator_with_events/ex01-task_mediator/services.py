from i_service import IService
from i_task import ITask
from tasks import PrintTask


class PrintService(IService):
    def perform_task(self, task: ITask):
        if isinstance(task, PrintTask):
            print(f"Executing task '{task.name}': {task.message}")
