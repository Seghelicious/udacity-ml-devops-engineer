import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    logger.debug("This is a debug message")
    # Mark the message as "info" importance
    logger.info("This is an info message")
    # Mark the message as "warning" importance
    logger.warning("This is a warning")
    # Mark the message as "error" importance
    logger.error("This is an error")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Use an artefact from W&B',
        fromfile_prefix_chars='@'
    )

    parser.add_argument(
        '--artefact name', type=str,
        help='Name and Version of W&B artefact', required=True
    )

    parser.add_argument(
        '--optional_arg', type=float,
        help='An optional argument', required=False,
        default=2.3
    )

    args = parser.parse_args()

    go(args)
