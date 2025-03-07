[![Beerware License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/BartekSzymik/create-ds-projects/blob/master/LICENSE)

# Create_ds

`create_ds` to narzędzie w Pythonie do szybkiego generowania struktury katalogów i plików dla projektów Data Science. 
Umożliwia również automatyczną instalację często używanych bibliotek, takich jak:
- numpy
- pandas
- matplotlib
- scikit-learn

## Instalacja

Pakiet można zainstalować za pomocą `pip` lub `uv`:
```bash
  pip install create_ds
```
albo za pomocą
```bash
   uv add create_ds
```

Tworzenie nowego projektu
Po instalacji pakietu można utworzyć nowy projekt Data Science, uruchamiając następującą komendę:

```bash
  python -m src.commands create-ds project_name
```
Spowoduje to wygenerowanie struktury katalogów oraz podstawowych plików konfiguracyjnych.

Konfiguracja środowiska
Po utworzeniu projektu, można skonfigurować środowisko wirtualne oraz zainstalować zależności za pomocą

```bash
  uv sync
```

Komenda ta odczyta plik pyproject.toml i automatycznie skonfiguruje środowisko z wymaganymi zależnościami.

## Technologie
Backend: Python


## Author

- [@BartekSzymik](https://github.com/BartekSzymik)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/BartekSzymik?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bartosz-szymik-82b615a1/)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/BartekSzymik/)
