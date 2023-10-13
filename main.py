import logging

from connectors.binance_futures import BinanceFuturesClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient("fc4517046570d7c034344ee567b4c00c1093c2b18db41a06d818fc67d36bbb4f",
                                   "26bc4f9c9fd34825408b461e9901c5b8fe0af3cfc6b49e4fa8f74e0263a88c07", True)

    root = Root(binance)
    root.mainloop()

