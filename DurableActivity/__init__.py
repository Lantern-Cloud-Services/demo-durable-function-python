# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(activity: str):
    logging.warning(f"Activity Triggered: {activity}")

    base = activity["base"]
    exp = activity["exp"]
    return base**exp