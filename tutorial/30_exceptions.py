import logging
import time

# Exception Clauses 
try:
    # Run first
    # <code>
    pass
except:
    # Run if exception occurs in try block
    # <code>
    pass
else:
    # Executes if try block *succeeds*
    # <code>
    pass
finally:
    # This code *always* executes
    # <code>
    pass


# Objective:
# Write function that reads binary file and returns data
# Measure time required
# Create logger
logging.basicConfig(filename="problems.log", 
                    level = logging.DEBUG)

logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time = start_time
        logger.info("Time required for {file} = {time}".format(file=path,
                                                               time=dt))

data = read_file_timed("audio_file.wav")