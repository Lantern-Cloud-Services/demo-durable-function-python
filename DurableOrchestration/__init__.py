# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import time

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    start_time = time.time()

    parallel_tasks = []
    
    params = context.get_input()
    base = int(params["base"])
    exp = int(params["exp"])

    logging.warning(f"Orchestrator Triggered with params - base: " + base.__str__() + ", exp: " + exp.__str__())
    #results = []
    for x in range(2, exp+1):        
        data = {
            "base": base,
            "exp": x
        }        
        parallel_tasks.append(context.call_activity("DurableActivity", data))

    results = yield context.task_all(parallel_tasks)
    total = sum(results)

    end_time = time.time()
    total_time = end_time-start_time
    final_result = f"With the input values base: {base}, exp: {exp} we calculated a total result of {total} in {total_time} seconds using FOFI."

    return final_result

main = df.Orchestrator.create(orchestrator_function)