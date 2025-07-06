import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

def main() -> None:
    """
    Simple example.
    """
    logger.info("Hello from {{ cookiecutter.project_name }}!")

if __name__ == "__main__":
    main()
    
