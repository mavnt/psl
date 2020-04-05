import time
from random import randint

from psl import psl


def main():
    items = [
        "Honujwa",
        "Ijicudik",
        "Beparhu",
        "Loewavac",
        "Tafjoiwo",
        "Gamufiolu",
        "Jagsajuno",
        "Wadigco",
        "Umpepit",
        "Kojsijneb",
        "Wuhfona",
        "Culehlo",
        "Juuwuvih",
    ]

    for item in items:
        psl(f"Processing {item}...")
        time.sleep(0.3)
    print()


if __name__ == "__main__":
    main()
