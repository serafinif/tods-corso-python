from utils_io import setup_logger, load_data, save_json
from analysis import add_derived, compute_stats
from viz import (
    plot_hist_price,
    plot_price_by_bedrooms,
    plot_price_by_waterfront,
    plot_corr_heatmap,
)
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    log_path = Path(__file__).resolve().parents[1]/ "output" / "logs" / "app.log"
    logger = setup_logger(log_path=log_path)
    logger.info("=== DataHouse avviato ===")

    df = load_data("data/Housing.csv", logger)

    df = add_derived(df)
    stats = compute_stats(df)
    save_json(stats, "output/report.json")

    logger.info("Report generato in output/report.json")

    plot_hist_price(df)
    plot_price_by_bedrooms(df)
    plot_price_by_waterfront(df)
    plot_corr_heatmap(df)

    logger.info("Grafici salvati in output/grafici/")
    logger.info("=== Esecuzione completata ===")


if __name__ == "__main__":
    main()
