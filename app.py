# import os
# import sys

# from fastapi import FastAPI

# SRC_DIR = os.path.join(os.path.dirname(__file__), "src")
# if SRC_DIR not in sys.path:
#     sys.path.insert(0, SRC_DIR)

# from mlProject import logger

# app = FastAPI(title="YouTube Fake Thumbnail Detector")


# @app.get("/health")
# def health_check() -> dict:
#     logger.info("Health check requested")
#     return {"status": "ok"}


# @app.get("/")
# def root() -> dict:
#     return {"message": "YouTube Fake Thumbnail Detector API"}


# if __name__ == "__main__":
#     try:
#         import uvicorn
#     except Exception as exc:  # pragma: no cover - runtime convenience
#         raise SystemExit(
#             "uvicorn is required to run app.py directly. "
#             "Install with `pip install uvicorn`."
#         ) from exc

#     uvicorn.run(app, host="0.0.0.0", port=8000)
