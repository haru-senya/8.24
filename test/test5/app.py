import logging


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s"
)


logging.info("program start")

x = 10
y = 2

logging.info(f"x={x}, y={y}")

try:
    result = x / y
    logging.info(f"result={result}")

except Exception as e:
    logging.error(e)

logging.info(f"result={result}")

print("finish")