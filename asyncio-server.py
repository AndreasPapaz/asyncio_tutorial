import sys
import asyncio

from charfinder import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'?> '

imdex = UnicodeNameIndex()

@asyncio.corotine
def handle_queries(reader, writer):
    while True:
        writer.write(PROMPT) # cant yield from!
        yield from writer.drain() # must yield from!
        data = yield from reader.readline()

        try:
            query = data.decode().strip()
        except UnivodeDecodeError:
            query = '\x00'
        client = writer.get_extra_info('peername')

        print('Received from {} : {!r}'.format(client, query))

        if query:
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_str(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)

            yield from writer.drain()
            print('Sent {} results'.format(len(lines)))

    print('Close the client SOCKET')
    writer.close()
