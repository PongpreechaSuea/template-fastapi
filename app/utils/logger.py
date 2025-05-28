import logging

GREEN = "\033[92m"   # INFO
YELLOW = "\033[93m"  # WARNING
RED = "\033[91m"     # ERROR, CRITICAL
BLUE = "\033[94m"    # DEBUG
RESET = "\033[0m"

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelname == "DEBUG":
            color = BLUE
        elif record.levelname == "INFO":
            color = GREEN
        elif record.levelname == "WARNING":
            color = YELLOW
        elif record.levelname in ["ERROR", "CRITICAL"]:
            color = RED
        else:
            color = RESET
        
        log_fmt = f"{color}%(asctime)s [%(levelname)s]{RESET} [%(filename)s:%(lineno)d] %(message)s"
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(CustomFormatter())
logger.addHandler(console_handler)

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.handlers = logger.handlers
uvicorn_logger.setLevel(logging.INFO)