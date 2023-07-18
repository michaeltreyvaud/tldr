import os
import uvicorn
from dotenv import load_dotenv
from src.dependencies.Environment import Environment

load_dotenv()
environment = Environment(dict(os.environ))


def main():
    uvicorn.run(
        app="src.app.app:app",
        port=environment.get_port(),
        reload=True if environment.get_environment() == "dev"
            else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
