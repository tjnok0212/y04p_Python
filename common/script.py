import sys
from pathlib import Path

# 親ディレクトリ（top）のパスを sys.path の先頭に強制追加する
current_dir = Path(__file__).resolve().parent
root_dir = current_dir.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))
