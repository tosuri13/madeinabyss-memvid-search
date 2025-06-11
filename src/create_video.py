from pathlib import Path

from memvid import MemvidEncoder

DEFAULT_CHUNK_SIZE = 512
DEFAULT_CHUNK_OVERLAP = 256

encoder = MemvidEncoder.from_file(
    file_path=str(Path("assets", "madeinabyss-document.md")),
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_CHUNK_OVERLAP,
)
encoder.build_video(
    output_file=str(Path("assets", "madeinabyss-contents.mp4")),
    index_file=str(Path("assets", "madeinabyss-index.json")),
    auto_build_docker=False,
)
