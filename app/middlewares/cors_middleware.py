from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """
    Configures CORS settings for the FastAPI application.

    Adds the CORSMiddleware to the application with specific settings allowing 
    all origins, credentials, methods, and headers. This setup is useful for 
    development and testing but may need to be restricted in a production environment 
    to enhance security.

    Args:
        app (FastAPI): The FastAPI application instance to which the middleware 
                       will be added.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
