import logging

import pytest

logger = logging.getLogger(__name__)

logger.info("logging information")

if __name__ == '__main__':
    logging.debug("debug...")
    logging.info("info...")
    logging.warning("warning...")
    logging.error("error...")
    logging.critical("critical...")
    pytest.main()
