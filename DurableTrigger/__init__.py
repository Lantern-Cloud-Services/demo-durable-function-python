# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging

import azure.functions as func
from azure.durable_functions import DurableOrchestrationClient
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str, message):
    function_name = req.route_params.get('functionName')
    base = req.params.get('base')
    exp = req.params.get('exp')
    logging.warning(f"Durable fuction triggered with base: " + base + ", exp: " + exp)
    
    logging.info(starter)
    client = DurableOrchestrationClient(starter)
    data = {
        "base": base,
        "exp": exp
    }
    instance_id = await client.start_new(function_name, client_input=data)
    response = client.create_check_status_response(req, instance_id)
    message.set(response)