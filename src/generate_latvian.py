# ==========================================================================================
# DISCLAIMER:                                                                              |
# This code generates synthetic Latvian SMS messages to help expand the training dataset.  |
# The messages are based on common patterns seen in real spam and legitimate texts,        |
# but are entirely fictional and not meant for any malicious use.                          |
# Since there aren’t many publicly available Latvian datasets, this is an attempt          |
# to bootstrap data for training a spam detection model.                                   |
# All Latvian text is translated via Google Translate and may not sound perfectly natural. |
# ==========================================================================================

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
    "Pērnavas iela",
    "Daugavgrīvas iela",
    "Ropažu iela",
    "Kārļa Ulmaņa gatve",
]

SAFE_URLS = ["www.latvija.lv", "www.ss.com", "www.delfi.lv", "www.manabalss.lv"]

SPAM_TEMPLATES = [
    "SVARĪGI: Jūsu {bank} konts ir bloķēts. Atjaunojiet piekļuvi: {url}",
    "{bank}: Konstatēta aizdomīga darbība. Apstipriniet identitāti 24h laikā: {url}",
    "Jūsu {bank} maksājumu karte tiks deaktivizēta. Zvaniet tūlīt: {phone}",
    "Apsveicam! Jūs laimējāt {amount} EUR. Pieprasiet balvu: {url}",
    "{store}: Jūs esat mūsu izlozē laimējis dāvanu karti {amount} EUR vērtībā. Aktivizējiet: {url}",
    "Latvijas Pasts: Jūsu sūtījums {parcel} gaida. Samaksājiet nodevu {card_amount} EUR: {url}",
    "CSDD: Jums ir nesamaksāts sods. Veiciet apmaksu tūlīt, lai izvairītos no kavējuma naudām: {url}",
    "Ātra nauda! Kredīts līdz {amount} EUR bez ķīlas un dokumentiem. SMS 'JĀ' uz 1234.",
    "Jūsu ierīcē konstatēts vīruss! Lejupielādējiet aizsardzību tūlīt: {url}",
    "Sveiki! Jūs esat izvēlēts ekskluzīvam piedāvājumam. Bezmaksas iPhone. Reģistrējieties: {url}",
    "{bank}: Jūsu parole ir jāatjauno drošības apsvērumu dēļ. Dodieties uz: {url}",
    "Laimīgais numurs! Jūsu tālrunis laimēja {amount} EUR loterijā. Zvaniet: {phone}",
    "UZMANĪBU {bank} klients! Jūsu konta limits ir pārsniegts. Rīkojieties: {url}",
    "Bezmaksas kredīts {amount} EUR. Bez atteikuma. Tikai šodien! Sīkāk: {url}",
    "Jūs saņemsiet {amount} EUR sociālo pabalstu. Apstipriniet datus: {url}",
    "{store} loterija: Laimējāt iepirkumu {amount} EUR vērtībā! Pārbaudiet: {url}",
    "Drošības brīdinājums: Kāds mēģināja piekļūt jūsu {bank} kontam. Bloķējiet: {url}",
    "Jūsu pakotne tika aizturēta muitā. Samaksājiet {card_amount} EUR nodevu: {url}",
    "VID: Jums ir nodokļu parāds. Izvairieties no soda — nomaksājiet: {url}",
    "Ekskluzīvs piedāvājums tikai šodien! {amount} EUR bonuss jauniem {bank} klientiem: {url}",
    "Jūsu {bank} kredītkartes informācija ir apdraudēta. Atjaunojiet drošību: {url}",
    "Paldies par jūsu pirkumu {store}! Jūsu čeks ir pieejams: {url}",
    "Jūsu {bank} konts ir bloķēts aizdomīgas aktivitātes dēļ. Atjaunojiet piekļuvi: {url}",
    "{store}: Jums ir jauns paziņojums vai neapmaksāts rēķins. Skatīt: {url}",
    "Drošības brīdinājums: Kāds mēģināja piekļūt jūsu {store} kontam. Bloķējiet: {url}",
]

HAM_TEMPLATES = [
    "Sveiki {name}! Vai vari šovakar atnākt uz vakariņām ap septiņiem?",
    "Atgādinājums: rītdienas tikšanās pulksten 10:00, {street} {num}.",
    "Paldies par pasūtījumu! Prece tiks piegādāta 2-3 darba dienu laikā.",
    "Jūsu {bank} maksājums {amount} EUR ir veiksmīgi apstrādāts.",
    "{name}, es aizkavēšos. Būšu mājās ap 20:00. Neuztraucies!",
    "Vai esi gatavs šodienas prezentācijai? Tikamies pie ieejas.",
    "Jūsu Bolt brauciens pabeigts. Summa: {card_amount} EUR. Paldies!",
    "Labdien! Atgādinām par vizīti pie ārsta rīt pulksten 14:30.",
    "Kolēģi, lūdzu iesniedziet atskaites līdz piektdienai. Paldies!",
    "Sveiki! Pusdienas šodien? Varu tikties pie universitātes.",
    "Jūsu biļetes uz pasākumu ir nosūtītas uz e-pastu. Labu izklaidi!",
    "Lidosta: Jūsu reiss iekāpšana 14. vārtā. Lūdzu ierodieties laicīgi.",
    "Rītdienas sporta treniņš ir pārcelts uz 19:00. Vai der?",
    "{name}, vai esi redzējis šīs nedēļas lekciju sarakstu?",
    "Jūsu interneta abonements ir atjaunots. Nākamais maksājums: 1. aprīlī.",
    "Piegāde veiksmīga! Jūsu sūtījums {parcel} ir saņemts.",
    "Labdien, lūdzu apstipriniet tikšanos ceturtdien pulksten 15:00.",
    "{store} čeks: Paldies par pirkumu! Kopā: {amount} EUR.",
    "Sveiki! Projekta sanāksme pārcelta uz trešdienu. Visi informēti?",
    "Jūsu {bank} konta izraksts ir pieejams internetbankā.",
    "{name}, vai vari aizdot man 20 EUR līdz rītdienai? Atdošu nākamnedēļ.",
    "Lūdzu, atbildi, kad redzēsi šo ziņu.",
    "Sveiki! Vai vēlies pievienoties manai dzimšanas dienas ballītei sestdien? Būs jautri!",
    "{store} atlaide! Jūsu iepirkums {amount} EUR ir apstiprināts. Paldies, ka izvēlējāties mūs!",
    "{name}, es aizkavēšos. Būšu mājās ap 20:00.",
    "Svarīgi: Jūsu pieraksts rīt ir pārcelts uz 16:00. Lūdzu apstipriniet.",
]


def get_random_url():
    tlds = [".com", ".net", ".lv", ".info", ".online", ".click"]
    name = "".join(
        random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(8, 15))
    )
    return f"{name}{random.choice(tlds)}/login"


def get_lookalike_url():
    target = random.choice(
        ["swedbank", "citadele", "luminor", "seb", "pasts", "smart-id", "latvija"]
    )
    suffix = random.choice(["-login", "-verify", "-safe", "-lv", "24", "-portal"])
    tld = random.choice([".net", ".com", ".online", ".info"])
    path = random.choice(["", "/login", "/index.php", "/secure"])
    return f"{target}{suffix}{tld}{path}"


def clean_text(text, prob=0.4):
    if random.random() > prob:
        return text
    rep = str.maketrans("āčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ", "acegiklpsuzACEGIKLPSUZ")
    return text.translate(rep)


def fill(template, is_spam=True):
    if is_spam:
        url_raw = get_lookalike_url() if random.random() < 0.8 else get_random_url()
        text_clean_prob = 0.5
    else:
        url_raw = random.choice(SAFE_URLS)
        text_clean_prob = 0.1

    url_final = f"https://{url_raw.replace('https://', '').replace('http://', '')}"

    phone_num = f"2{random.randint(1000000, 9999999)}"
    phone_val = f"+371 {phone_num}" if random.random() > 0.5 else f"{phone_num}"

    data = {
        "bank": random.choice(BANKS),
        "store": random.choice(STORES),
        "amount": random.choice(AMOUNTS),
        "card_amount": random.choice(CARD_AMOUNTS),
        "phone": phone_val,
        "url": url_final,
        "parcel": f"LV{random.randint(10000000, 99999999)}",
        "name": random.choice(NAMES),
        "street": random.choice(STREETS),
        "num": random.randint(1, 100),
    }

    formatted_text = template.format(**data)
    return clean_text(formatted_text, prob=text_clean_prob)


def generate(n_spam=2000, n_ham=3000):
    spam = [fill(random.choice(SPAM_TEMPLATES), is_spam=True) for x in range(n_spam)]
    ham = [fill(random.choice(HAM_TEMPLATES), is_spam=False) for y in range(n_ham)]

    df = pd.DataFrame(
        [(x, 1) for x in spam] + [(y, 0) for y in ham], columns=["message", "label"]
    )
    df = df.sample(frac=1, random_state=24).reset_index(drop=True)

    out_path = Path(DATA_PROCESSED_PATH).parent / "latvian_sms.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Generated {len(df)} messages: {out_path} (Spam: {n_spam}, Ham: {n_ham})")


if __name__ == "__main__":
    generate()
