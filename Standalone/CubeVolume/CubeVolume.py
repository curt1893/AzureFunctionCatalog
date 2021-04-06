#Azure Fucntion Examples

#Trigger Type: HTTP
#Language: Python

#Purpuse: Take input, length of a side of a cube, from HTTP Request and return the volume. This is just an example
#of a working Azure Function.

import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    length = req.params.get('length')
    if not length:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            length = req_body.get('length')

    if length:
        volume = pow(float(length),3)
        return func.HttpResponse(str(volume), status_code=200)
    else:
        return func.HttpResponse(
             "Please provide a valid length argument.",
             status_code=500
        )