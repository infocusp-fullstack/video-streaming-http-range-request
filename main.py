from fastapi import Request, HTTPException, status
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os
from typing import BinaryIO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def iterfile(path: BinaryIO, start: int, end: int, chunk_size=1024 * 1024):
    with path as f:
        f.seek(start)
        while (pos := f.tell()) <= end:
            read_size = min(chunk_size, end + 1 - pos)
            yield f.read(read_size)


def get_range_header(range_header: str, file_size: int) -> tuple[int, int]:
    def invalid_range():
        return HTTPException(
            status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE,
            detail=f"Invalid request range (Range:{range_header!r})",
        )

    try:
        h = range_header.replace("bytes=", "").split("-")
        start = int(h[0]) if h[0] != "" else 0
        end = int(h[1]) if h[1] != "" else file_size - 1
    except ValueError:
        raise invalid_range()

    if start > end or start < 0 or end > file_size - 1:
        raise invalid_range()
    return start, end


@app.get("/video", response_class=StreamingResponse)
async def get_bucket_doc(request: Request):

    try:

        local_file_path = "temp" + "/" + "test.mp4"
        file_size = os.stat(local_file_path).st_size
        range_header = request.headers.get("range")

        start = 0
        end = file_size - 1
        status_code = status.HTTP_200_OK

        headers = {
            "content-type": "video/mp4",
            "content-encoding": "identity",
            "content-length": str(file_size),
            "accept-ranges": "bytes",
            "access-control-expose-headers": (
                "content-type, accept-ranges, content-length, "
                "content-range, content-encoding"
            ),
            "content-range": "bytes=0-",
        }

        if range_header is not None:
            start, end = get_range_header(range_header, file_size)
            size = end - start + 1
            headers["content-length"] = str(size)
            headers["content-range"] = f"bytes {start}-{end}/{file_size}"
            status_code = status.HTTP_206_PARTIAL_CONTENT

        return StreamingResponse(
            iterfile(path=open(local_file_path, "rb"), start=start, end=end),
            headers=headers,
            status_code=status_code,
            media_type="video/mp4",
        )

    except Exception:
        raise HTTPException(status_code=400, detail="Bad Request")
