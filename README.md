# AutoSort – Automātisks failu sakārtotājs

## Projekta uzdevums
Šī programmatūra automātiski sakārto failus lietotāja norādītajā mapē, pamatojoties uz failu paplašinājumiem. Programma nolasa konfigurāciju no `config.json`, pārbauda failus, pārvieto tos uz atbilstošām apakšmapēm un ieraksta darbības žurnālā `log.txt`.

Mērķis ir atvieglot failu pārvaldību datorā un novērst nesakārtotu lejupielāžu vai jebkuru citu mapi.

---

## Izmantotās Python bibliotēkas

- **`os`** – darbs ar failu sistēmu (ceļiem, failu sarakstiem, pārbaudēm).
- **`json`** – konfigurācijas faila (`config.json`) nolasīšanai.
- **`shutil`** – failu pārvietošanai uz citām mapēm.
- **`datetime`** – žurnālā pieraksta darbību laiku.

Šīs bibliotēkas ir izvēlētas, jo tās ir iebūvētas Python valodā un labi piemērotas koda praktiskajām vajadzībām.

---

## Datu struktūras

Programmas darbībā tiek izmantotas šādas datu struktūras:

- **Vārdnīca (`dict`)** – `extension_map`, ir strukturēts pāru saraksts, kur katram faila paplašinājumam ir piesaistīta mape, uz kuru attiecīgais fails jānovirza:
  ```json
  {
    ".jpg": "Attēli",
    ".pdf": "Dokumenti"
  }
  ```

- **Saraksts (`list`)** – iegūts no `os.listdir()`, lai pārskatītu visus failus norādītajā mapē.

- **Log fails** – `log.txt` satur laiku un katra pārvietotā (vai problemātiskā) faila aprakstu.

---

## Programmas arhitektūra

Programma sastāv no trīs galvenajām funkcijām:

1. **`load_config()`** – nolasīt un atgriezt konfigurāciju no `config.json`.
2. **`ensure_target_folders()`** – izveido nepieciešamās apakšmapes, ja to vēl nav.
3. **`move_files()`** – veic pašu galveno darbu, pārskata failus, pārbauda paplašinājumus, pārvieto failus un ieraksta darbību žurnālā.

---

## Demonstrācijas video

[Demonstrācijas video](demo.mp4)

---
