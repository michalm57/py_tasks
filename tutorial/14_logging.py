# Logging
# Purpose: Record progress and problems...
# Levels: Debug, Info, Warning, Error, Critical

import logging
import os
import math

current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logs.log", 
                    level = logging.DEBUG, #ERROR - only for error and criticals, DEBUG for everything
                    format = LOG_FORMAT, 
                    filemode='w') # Old log message will be overwritten
logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")
logger.info("Our second message.")

print(logger.level)

# Test messages
logger.debug("Debug first message.")
logger.info("Info first message.")
logger.warning("Warning first message.")
logger.error("Error first message.")
logger.critical("Critical first message.")


# Quadratic formula
def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))
    
    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    
    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc) / (2*a))
    root2 = (-b - math.sqrt(disc) / (2*a))
    
    #Return the roots
    logger.debug("# Return the roots")
    
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)