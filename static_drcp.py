import asyncio
from pypresence import AioPresence
from pypresence.exceptions import InvalidID

from static_data import presence_data


class StaticDRP:
    """
    A class for creating and managing a static Discord Rich Presence (DRP) using the pypresence library.

    Attributes:
        rpc (AioPresence): An asynchronous client for Discord Rich Presence.
        presence_data (dict): A dictionary containing data to be displayed on Discord Rich Presence.

    Methods:
        connect(): Asynchronously connects to Discord's RPC server.
        update_presence(): Updates the current Discord Rich Presence with the provided data.
        disconnect(): Clears and disconnects the Rich Presence.
        run(): Runs the Discord Rich Presence service.
        async_start(): Asynchronously starts the Rich Presence service.
        start(): Starts the Rich Presence service synchronously.
    """

    def __init__(self, client_id: str, presence_data: dict):
        self.rpc = AioPresence(client_id=client_id)
        self.presence_data = presence_data
        self.connected = False

    async def connect(self):
        """
        Asynchronously connects to Discord's Rich Presence Client.
        Raises an exception if the connection fails.
        """
        try:
            await self.rpc.connect()
        except Exception as e:
            print(f'There was an error connecting to Discord: {e}')
            raise

    async def update_presence(self):
        """
        Asynchronously updates the Discord Rich Presence with the data specified in 'presence_data'.
        """
        data = self.presence_data
        await self.rpc.update(
            details=data.get('details'),
            state=data.get('state'),
            start=data.get('start'),
            end=data.get('end'),
            large_image=data.get('large_image'),
            large_text=data.get('large_text'),
            small_image=data.get('small_image'),
            small_text=data.get('small_text'),
            buttons=data.get('buttons'),
            instance=data.get('instance'),
            party_id=data.get('party_id'),
            party_size=data.get('party_size'),
            join=data.get('join'),
            match=data.get('match'),
            spectate=data.get('spectate'),
        )

    async def disconnect(self):
        """
        Asynchronously clears and disconnects the Discord Rich Presence.
        Prints a message when the Rich Presence server is stopped.
        """
        await self.rpc.clear()
        print("Static Rich Presence Server stopped!")

    async def run(self):
        """
        Asynchronously runs the Discord Rich Presence service.
        Handles connection, updating presence, and gracefully handles termination signals.
        """

        try:
            await self.connect()
            self.connected = True

            await self.update_presence()
            print("Static Rich Presence Server running...")

            try:
                print("Terminate the Rich Presence Server with [STRG] + [C]!")
                await asyncio.Future()
            except asyncio.exceptions.CancelledError:
                pass

        except (KeyboardInterrupt, InvalidID):
            pass

        finally:
            if self.connected:   
                await self.disconnect()

    async def async_start(self):
        """
        Asynchronously starts the Discord Rich Presence service using the 'run' method.
        """
        await self.run()

    def start(self):
        """
        Synchronously starts the Discord Rich Presence service.
        This is the entry point when the script is run directly.
        """
        asyncio.run(self.async_start())


if __name__ == "__main__":
    drp = StaticDRP(
        client_id = presence_data.get("client_id"),
        presence_data = presence_data
    )
    drp.start()
