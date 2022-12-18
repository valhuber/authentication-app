from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger('api_logic_server_app')
app_logger.debug("\napi/expose_api_models.py - endpoint for each table")


def expose_models(api):
    """
        Declare API - on existing SAFRSAPI 
            This exposes each model (note: end point names are table names) 
            Including get (filtering, pagination, related data access) 
            And post/patch/update (including logic enforcement) 
        You typically do not customize this file 
            See https://valhuber.github.io/ApiLogicServer/Tutorial/#customize-and-debug 
    """
    api.expose_object(database.models.Api)
    api.expose_object(database.models.User)
    api.expose_object(database.models.Role)
    api.expose_object(database.models.UserRole)
    return api
