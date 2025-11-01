import logging as log



# Now configure logging again
log.basicConfig(
    filename='app1.log',
    filemode='w',
    level=log.DEBUG,
    format="%(asctime)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)