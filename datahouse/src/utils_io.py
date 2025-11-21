import json
import logging
from pathlib import Path
import pandas as pd


def setup_logger(log_path: str = "app.log", overwrite: bool = True) -> logging.Logger:
    """Crea un logger che scrive sia su file che su console."""

    if overwrite:
        Path(log_path).write_text("")

    logger = logging.getLogger("datahouse")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Formato uniforme
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S")

        # File handler
        fh = logging.FileHandler(log_path)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(ch)

    return logger


def load_data(path: str, logger) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        logger.info(f"✅ Caricato dataset: {len(df)} righe")
        return df
    except FileNotFoundError:
        logger.error(f"❌ File non trovato: {path}")
        raise
    except Exception as e:
        logger.error(f"Errore lettura CSV: {e}")
        raise


def save_json(data: dict, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
