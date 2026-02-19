"""
FastAPI applications.
"""

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from fastapi import routing
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.encoders import DictIntStrAny, SetIntStr
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.params import Depends
from fastapi.types import ASGIApp, DecoratedCallable, IncEx


class FastAPI(routing.App):
    """
    The main **FastAPI** class.

    You would create an instance of this class as the main object of your
    application.

    ## Example

    ```python
    from fastapi import FastAPI

    app = FastAPI()
    ```
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[routing.BaseRoute]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        default_response_class: type = Default(JSONResponse),
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[ASGIApp]] = None,
        exception_handlers: Optional[Dict[Union[int, Type[Exception]], Any]] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Union[str, Any]]] = None,
        license_info: Optional[Dict[str, Union[str, Any]]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[Dict[str, Any]]] = None,
        webhooks: Optional[routing.APIRouter] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Optional[Callable[[routing.APIRoute], str]] = None,
        **extra: Any,
    ) -> None:
        """
        Create a FastAPI application instance.

        ## Parameters

        **debug**: Enable debug mode.

        **routes**: A list of routes to serve.

        **title**: The title of the API.

        **description**: A short description of the API.

        **version**: The version of the API.

        **openapi_url**: The URL for the OpenAPI schema.

        **openapi_tags**: A list of tags for the OpenAPI schema.

        **servers**: A list of servers for the OpenAPI schema.

        **dependencies**: A list of global dependencies.

        **default_response_class**: The default response class to use.

        **docs_url**: The URL for the Swagger UI documentation.

        **redoc_url**: The URL for the ReDoc documentation.

        **swagger_ui_oauth2_redirect_url**: The URL for the Swagger UI OAuth2 redirect.

        **swagger_ui_init_oauth**: OAuth2 configuration for Swagger UI.

        **middleware**: A list of middleware to add.

        **exception_handlers**: A dictionary of exception handlers.

        **on_startup**: A list of functions to run on startup.

        **on_shutdown**: A list of functions to run on shutdown.

        **terms_of_service**: The terms of service for the API.

        **contact**: Contact information for the API.

        **license_info**: License information for the API.

        **openapi_prefix**: The prefix for the OpenAPI schema.

        **root_path**: The root path for the API.

        **root_path_in_servers**: Whether to include the root path in the servers list.

        **responses**: A dictionary of default responses.

        **callbacks**: A list of callbacks for the OpenAPI schema.

        **webhooks**: An APIRouter for webhooks.

        **deprecated**: Whether the API is deprecated.

        **include_in_schema**: Whether to include the API in the OpenAPI schema.

        **swagger_ui_parameters**: Additional parameters for Swagger UI.

        **generate_unique_id_function**: A function to generate unique IDs for routes.

        **extra**: Additional keyword arguments.
        """
        super().__init__(
            debug=debug,
            routes=routes,
            title=title,
            description=description,
            version=version,
            openapi_url=openapi_url,
            openapi_tags=openapi_tags,
            servers=servers,
            dependencies=dependencies,
            default_response_class=default_response_class,
            docs_url=docs_url,
            redoc_url=redoc_url,
            swagger_ui_oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
            swagger_ui_init_oauth=swagger_ui_init_oauth,
            middleware=middleware,
            exception_handlers=exception_handlers,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            terms_of_service=terms_of_service,
            contact=contact,
            license_info=license_info,
            openapi_prefix=openapi_prefix,
            root_path=root_path,
            root_path_in_servers=root_path_in_servers,
            responses=responses,
            callbacks=callbacks,
            webhooks=webhooks,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            swagger_ui_parameters=swagger_ui_parameters,
            generate_unique_id_function=generate_unique_id_function,
            **extra,
        )
