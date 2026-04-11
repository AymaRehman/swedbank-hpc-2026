import random
import pandas as pd
from pathlib import Path
from config import DATA_PROCESSED_PATH

random.seed(24)

BANKS = [
    "Swedbank",
    "SEB Banka",
    "Citadele",
    "Luminor",
    "Revolut",
    "BlueOr Bank",
    "Rietumu Banka",
    "Signet Banka",
    "Industra Banka",
]

STORES = [
    "Maxima",
    "Rimi",
    "Lidl",
    "Bolt",
    "Tet",
    "Latvijas Pasts",
    "CSDD",
    "LMT",
    "Tele2",
    "Bite",
    "Circle K",
    "Smart-ID",
    "Latvija.lv",
    "VID",
]

AMOUNTS = [
    "50",
    "100",
    "150",
    "200",
    "500",
    "1000",
    "2000",
    "50.00",
    "99.99",
    "149.49",
    "199.99",
    "499.00",
    "999.00",
    "1999.00",
    "49.99",
    "149.99",
    "249.99",
    "499.99",
    "999.99",
    "1999.99",
]

CARD_AMOUNTS = [
    "1.49",
    "1.99",
    "2.49",
    "3.99",
    "4.99",
    "5.99",
    "9.99",
    "19.99",
    "29.99",
    "49.99",
    "99.99",
    "149.99",
    "199.99",
    "249.99",
    "499.99",
    "999.99",
]

FAKE_URLS = [
    "swdbnk-lv.com",
    "secure-latvija.net",
    "citadele-verify.lv",
    "luminor-support.com",
    "seb-login-lv.com",
    "pasts-lv.delivery",
    "tet-lv-support.com",
    "bolt-lv.com",
    "maxima-win.lv",
    "rimi-promo.lv",
    "latvija-kredits.com",
    "drogas-lv.com",
    "csdd-samaksa.lv",
    "id-verify-lv.net",
    "loto-lv.com",
    "lmt-lv.com",
]

NAMES = [
    "Anna",
    "Jānis",
    "Pēteris",
    "Marta",
    "Ilze",
    "Andris",
    "Laura",
    "Toms",
    "Zane",
    "Edgars",
    "Inese",
    "Mārtiņš",
    "Dace",
    "Līga",
    "Raimonds",
    "Agnese",
    "Kaspars",
    "Evija",
    "Valdis",
    "Ieva",
]

STREETS = [
    "Brīvības iela",
    "Krišjāņa Valdemāra iela",
    "Tērbatas iela",
    "Dzirnavu iela",
    "Elizabetes iela",
    "Aspazijas bulvāris",
    "Kr. Barona iela",
    "Miera iela",
    "Blaumaņa iela",
    "Stabu iela",
    "Alberta iela",
    "Merķeļa iela",
    "Kārļa Ulmaņa gatve",
    "Pērnavas iela",
    "Daugavgrīvas iela",
    "Ropažu iela",
    "Kārļa Ulmaņa gatve",
]

SAFE_URLS = ["www.latvija.lv", "www.ss.com", "www.delfi.lv", "www.manabalss.lv"]

SPAM_TEMPLATES = []

HAM_TEMPLATES = []


def get_random_url():
    pass


def clean_text():
    pass


def fill(template, is_spam=True):
    pass


def generate(n_spam=2000, n_ham=3000):
    pass


if __name__ == "__main__":
    generate()
