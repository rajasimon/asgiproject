from channels.generic.http import AsyncHttpConsumer


# Create your views here.
class BasicHttpConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        await asyncio.sleep(10)
        await self.send_response(200, b"Your response bytes", headers=[
            ("Content-Type", "text/plain"),
        ])