import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "flask" / "backend"

sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(ROOT))