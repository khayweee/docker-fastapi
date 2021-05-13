"""
Module for Logging
"""

import logging
import logging.handlers
from pathlib import Path, PurePath

def create_logger(name,
                  loglevel,
                  logfilename,
                  console = True,
                  file_handler = True,
                  logfile_maxbytes = 1000000,
                  logfile_backupcount=3):
    """ Create System logs """
    Path(PurePath(logfilename).parent).mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" %loglevel)

    #file handler
    filehandler = logging.handlers.RotatingFileHandler(
        filename=logfilename,
        mode="a",
        maxBytes=logfile_maxbytes,
        backupCount=logfile_backupcount,
        encoding=None,
        delay=False
    )
    filehandler.setLevel(logging.DEBUG)
    if file_handler == True:
        filehandler.setFormatter(logging.Formatter(
                fmt='''{"timestamp": %(asctime)s, "system":%(name)s, "loglevel":%(levelname)s, "msg":%(message)s, "length":%(length)s}''',
                datefmt="%Y-%m-%d %I:%M:%S",
            ))
    else:
        filehandler.setFormatter(logging.Formatter(
                fmt='''{"timestamp": %(asctime)s, "system":%(name)s, "module":%(module)s, "loglevel":%(levelname)s, "msg":%(message)s}''',
                datefmt="%Y-%m-%d %I:%M:%S",
            )) 
    #console handler
    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(
        logging.Formatter(
            fmt="{asctime} {name}-{module}-{funcName} [{levelname}]: {message}",
            datefmt="%Y-%m-%d %I:%M:%S",
            style="{"
        )
    )
    consolehandler.setLevel(logging.INFO)
    logger.setLevel(numeric_level)
    logger.addHandler(filehandler)
    if console == True:
        logger.addHandler(consolehandler)

    return logger