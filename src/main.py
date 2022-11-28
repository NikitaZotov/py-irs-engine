import logging

import argparse

from server.server import IrsServer

IRS_SERVER_HOST = 'host'
IRS_SERVER_PORT = 'port'
IRS_SERVER_HOST_DEFAULT = '127.0.0.1'
IRS_SERVER_PORT_DEFAULT = 7080


def main(args: dict):
    server = IrsServer(host=args[IRS_SERVER_HOST], port=args[IRS_SERVER_PORT], loglevel=logging.INFO)
    server.run_forever()
    server.server_close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--host', type=str, dest=IRS_SERVER_HOST, default=IRS_SERVER_HOST_DEFAULT, help="Irs-server host")
    parser.add_argument(
        '--port', type=int, dest=IRS_SERVER_PORT, default=IRS_SERVER_PORT_DEFAULT, help="Irs-server port")
    args = parser.parse_args()

    main(vars(args))
