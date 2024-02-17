import os
import logging
import yaml
import logging.config


def setup_logging(default_path=os.path.join(__name__, '../logging.conf'), default_level=logging.INFO):
    """Configure logging for the application.

    This function looks for a configuration file specified in the arguments,
    and sets up the logging module for the application with it. If no file was
    found, the function falls back to a basic configuration.

    Parameters
    ----------
    default_path : <str>
        The location of the logging configuration file

    default_level : <int>
        One of the log-levels defined in the logging module

    env_key : <str>
        The environment variable locating the log-configuration file

    Returns
    -------
    None
    """

    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as log_conf_file:
            config = yaml.safe_load(log_conf_file.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    logger = logging.getLogger('.'.join([__name__, 'setup_logging']))
    logger.debug('Logging has been set up.')