# Copyright 2020 TestProject (https://testproject.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import socket
import atexit

from urllib.parse import urlparse
from src.testproject.sdk.exceptions import AgentConnectException


class SocketManager:

    __instance = None

    __socket = None

    def __init__(self):
        """Create SocketManager instance and register shutdown hook"""
        atexit.register(self.close_socket)

    @classmethod
    def instance(cls):
        """Return the singleton instance of the SocketManager class"""
        if cls.__instance is None:
            logging.info("No SocketManager instance found, creating a new one...")
            cls.__instance = SocketManager()
        else:
            logging.info("SocketManager instance found, reusing it...")
        return cls.__instance

    def close_socket(self):
        """Close the connection to the Agent development socket"""
        logging.info("close_socket(): Trying to close socket connection...")
        if self.is_connected():
            logging.info("close_socket(): Socket was connected, closing now...")

            try:
                SocketManager.__socket.shutdown(socket.SHUT_RDWR)
                SocketManager.__socket.close()
                SocketManager.__socket = None
                logging.info(
                    f"Connection to Agent closed successfully"
                )
            except socket.error as msg:
                logging.error(
                    f"Failed to close socket connection to Agent: {msg}"
                )
        else:
            logging.info("close_socket(): Socket was already disconnected!")

    def open_socket(self, socket_address: str, socket_port: int):
        """Opens a connection to the Agent development socket

        Args:
            socket_address (str): The address for the socket
            socket_port (int): The development socket port to connect to
        """

        if SocketManager.__socket is not None:
            logging.info("open_socket(): Socket already exists")
            return

        if self.is_connected():
            logging.debug("open_socket(): Socket is already connected")
            return

        host = urlparse(socket_address).hostname

        SocketManager.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SocketManager.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        SocketManager.__socket.connect((host, socket_port))

        if not self.is_connected():
            raise AgentConnectException("Failed connecting to Agent socket")

        logging.info(f"Socket connection to {host}:{socket_port} established successfully")

    def is_connected(self) -> bool:
        """Sends a simple message to the socket to see if it's connected

            Returns:
                bool: True if the socket is connected, False otherwise
        """
        logging.info("is_connected(): Checking if socket is connected...")
        if SocketManager.__socket is None:
            logging.info("is_connected(): No SocketManager instance found")
            return False

        try:
            logging.info("is_connected(): Start sending test message...")
            SocketManager.__socket.send("test".encode("utf-8"))
            logging.info("is_connected(): Test message successfully sent, socket is connected")
            return True
        except socket.error as msg:
            logging.error(f"Socket not connected: {msg}")
            return False
