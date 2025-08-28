# Příloha B -- Vstupní a výstupní artefakty¨

## Dokumenty

### Společná nastavení

Dokumenty budou generováný dvojjazyčně: HR/EN.

Název souboru BAR dokumentů bude odpovídat následující logice, pokud u popisu dokumentu není řečeno jinak:

Číslo dokumentu_název typu dokumentu_datum generování dokumentu.pdf případně .csv v [HR.]{.mark}

Příklad: 000000961005_Invoice_for_toll_202402270102.pdf

**Tabulka 40: Dokumenty**

| **Typ**               | **[Jméno HR]{.mark}**                                | **Jméno EN**                                                | **Jméno CZ**                               |
|-----------------------|------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------|
| DOC.BE.01.HR          | [Račun za nadoplatu]{.mark}                          | Advance invoice for top-up                                  | Zálohová faktura za top-up                 |
| DOC.BE.01B.HR         | [Račun za nadoplatu]{.mark}                          | Advance invoice for top-up                                  | Zálohová faktura za top-up                 |
| DOC.BE.06.HR          | [Odobrenie za neiskorištenu nadoplatu]{.mark}        | Advance invoice for top-up - Credit note                    | Zálohová faktura za top-up -- Dobropis     |
| DOC.BE.10.HR          | [Račun za cestarinu]{.mark}                          | Invoice for toll                                            | Faktura za mýtné                           |
| DOC.BE.10B.HR         | [Račun za cestarinu]{.mark}                          | Invoice for toll                                            | Faktura za mýtné                           |
| DOC.BE.11.HR          | [Detaljan prikaz prometa cestarine na računu]{.mark} | Detailed statement of toll transactions attached to invoice | Detailní výpis mýtných transakcí k faktuře |
| [DOC.BE.12.HR]{.mark} | [Detaljan prikaz prometa cestarine]{.mark}           | [Detailed statement of toll transactions]{.mark}            | [Detailní výpis mýtných transakcí]{.mark}  |
| DOC.BE.13.HR          | [Račun za cestarinu]{.mark}                          | Debit note for toll                                         | Vrubopis za mýtné                          |
| DOC.BE.14.HR          | [Odobrenie za cestarinu]{.mark}                      | Credit note for toll                                        | Dobropis za mýtné                          |
| [DOC.BE.15.HR]{.mark} | [Odobrenie za popuste na cestarini]{.mark}           | [Credit note for toll discounts]{.mark}                     |                                            |
| DOC.BE.16.HR          | [Račun za uslugu]{.mark}                             | Invoice for services                                        | Faktura za služby                          |
| DOC.BE.17.HR          | [Odobrenie za usluge]{.mark}                         | Credit note for services                                    | Dobropis za služby                         |
| [DOC.BE.19.HR]{.mark} | [Račun za ugovornu kaznu]{.mark}                     | [Invoice for contractual penalty]{.mark}                    |                                            |
| [DOC.BE.20.HR]{.mark} | [Odobrenie za ugovornu kaznu]{.mark}                 | [Credit note for contractual penalty]{.mark}                |                                            |
| DOC.BE.21.HR          | [eRačun]{.mark}                                      | eInvoice                                                    | eFaktura                                   |
| DOC.BE.22.HR          | [Zahtjev za isplatu]{.mark}                          | Offence Request for payment                                 | Výzva k úhradě za přestupky                |
| DOC.BE.23.HR          | [Zahtjev za isplatu - odobrenie]{.mark}              | Offence Request of Payment -- credit note                   | Výzva k úhradě za přestupky - Dobropis     |
| DOC.BE.24.HR          | [Predračun]{.mark}                                   | Proforma bill                                               | Proforma faktura                           |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |
|                       |                                                      |                                                             |                                            |

Podrobná specifikace jednotlivých dokumentů, notifikací a reportů je uvedena na [Confluence](https://tollnet.atlassian.net/wiki/x/FoA7Cw).

| **Dokument**                                                                                                              | **Skupina (Document group)** | **GUI**     | **Metadata**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Tisk**                                      | **E-mail**   | **Jazyk**                 |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|--------------|---------------------------|
| Zálohová faktura za top-up (DOC.BE.01.HR a DOC.BE.01B.HR)                                                                 | Invoice                      | BO          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                               |              | dvoujazyčná verze (hr+en) |
| Zálohová faktura za top-up -- Dobropis (DOC.BE.06.HR)                                                                     | Invoice                      | BO          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                               |              | dvoujazyčná verze (hr+en) |
| Faktura za mýtné (DOC.BE.10.HR)`<br>`{=html}Vrubopis za mýtné (DOC.BE.13.HR)`<br>`{=html}Dobropis za mýtné (DOC.BE.14.HR) | Invoice                      | BO          | Bill type`<br>`{=html}Bill issue type`<br>`{=html}Bill recurrence type`<br>`{=html}Bill category`<br>`{=html}Bill number`<br>`{=html}Bill ID`<br>`{=html}Bill session number`<br>`{=html}Bill session ID`<br>`{=html}Bill total amount`<br>`{=html}System operator ID`<br>`{=html}System operator abbreviation`<br>`{=html}Subject type`<br>`{=html}Customer ID`<br>`{=html}Customer number`<br>`{=html}Account number`<br>`{=html}Account type`<br>`{=html}EETS Provider ID`<br>`{=html}EETS Provider abbreviation`<br>`{=html}Exemption Partner ID`<br>`{=html}Exemption Partner [abbreviation]{.mark} |                                               | Ano          | dvoujazyčná verze (hr+en) |
| Detailní výpis mýtných transakcí k faktuře (DOC.BE.11.HR)                                                                 | Detail statement             | BO          | Metadata jako DOC.BE.10.HR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | stáhnutí z SC jako příloha faktury            |              | dvoujazyčná verze (hr+en) |
| [Detailní výpis mýtných transakcí (DOC.BE.12.HR)]{.mark}                                                                  | [Detail statement]{.mark}    | [SC]{.mark} | [Customer number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account type]{.mark}`<br>`{=html}[Customer ID]{.mark}                                                                                                                                                                                                                                                                                                                                                                                                                                      | [stáhnutí vygenerovaného exportu z SC]{.mark} |              | dvoujazyčná verze (hr+en) |
| Faktura za služby (DOC.BE.16.HR)                                                                                          | Invoice                      | BO          | Bill type`<br>`{=html}Bill issue type`<br>`{=html}Bill category`<br>`{=html}Bill number`<br>`{=html}Bill ID`<br>`{=html}Bill total amount`<br>`{=html}System operator ID`<br>`{=html}System operator abbreviation`<br>`{=html}Subject type`<br>`{=html}Customer ID`<br>`{=html}Customer number`<br>`{=html}Account number`<br>`{=html}Account type`<br>`{=html}EETS Provider ID`<br>`{=html}EETS Provider abbreviation`<br>`{=html}Exemption Partner ID`<br>`{=html}Exemption Partner [abbreviation]{.mark}                                                                                              |                                               | Ano          | dvoujazyčná verze (hr+en) |
| Dobropis za služby (DOC.BE.17.HR)                                                                                         | Invoice                      | BO          | Metadata jako DOC.BE.16.HR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                               | Ano          | dvoujazyčná verze (hr+en) |
| [Faktura za smluvní pokutu (DOC.BE.19.HR)]{.mark}                                                                         | [Invoice]{.mark}             | [BO]{.mark} | [Customer number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account type]{.mark}`<br>`{=html}[Bill issuer]{.mark}`<br>`{=html}[Bill number]{.mark}`<br>`{=html}[Bill issue type]{.mark}`<br>`{=html}[Bill total amount]{.mark}`<br>`{=html}[Bill total amount]{.mark}`<br>`{=html}[System operator ID]{.mark}`<br>`{=html}[Customer ID]{.mark}`<br>`{=html}[Bill ID]{.mark}                                                                                                                                                                            |                                               | [Ano]{.mark} | dvoujazyčná verze (hr+en) |
| [Dobropis za smluvní pokutu (DOC.BE.20.HR)]{.mark}                                                                        | [Invoice]{.mark}             | [BO]{.mark} | [Customer number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account number]{.mark}`<br>`{=html}[Account type]{.mark}`<br>`{=html}[Bill issuer]{.mark}`<br>`{=html}[Bill number]{.mark}`<br>`{=html}[Bill issue type]{.mark}`<br>`{=html}[Bill total amount]{.mark}`<br>`{=html}[Bill total amount]{.mark}`<br>`{=html}[System operator ID]{.mark}`<br>`{=html}[Customer ID]{.mark}`<br>`{=html}[Bill ID]{.mark}                                                                                                                                                                            |                                               | [Ano]{.mark} | dvoujazyčná verze (hr+en) |
| eFaktura (DOC.BE.21.HR)                                                                                                   | Invoice                      | BO          | Metadata jako DOC.BE.10.HR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                               | Ano          | dvoujazyčná verze (hr+en) |
| Výzva k úhradě za přestupek (DOC.BE.22.HR)                                                                                | Invoice                      | BO          | Bill issue type`<br>`{=html}Bill number`<br>`{=html}Bill ID`<br>`{=html}Bill total amount`<br>`{=html}System operator ID`<br>`{=html}System operator abbreviation`<br>`{=html}Subject type`<br>`{=html}Customer ID`<br>`{=html}Customer number`<br>`{=html}Account number`<br>`{=html}Account type`<br>`{=html}Postal address                                                                                                                                                                                                                                                                            |                                               |              | dvoujazyčná verze (hr+en) |
| Výzva k úhradě za přestupky -- Dobropis (DOC.BE.23.HR)                                                                    | Invoice                      | BO          | Metadata jako DOC.BE.22.HR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                               |              | dvoujazyčná verze (hr+en) |
| Proforma faktura (DOC.BE.24.HR)                                                                                           | Invoice                      | BO          | Bill number`<br>`{=html}Bill ID`<br>`{=html}Bill total amount`<br>`{=html}System operator ID`<br>`{=html}System operator abbreviation`<br>`{=html}Customer ID`<br>`{=html}Customer number`<br>`{=html}Account number`<br>`{=html}Account type                                                                                                                                                                                                                                                                                                                                                            |                                               |              | dvoujazyčná verze (hr+en) |

: Tabulka : Přehled dokumentů -- nastavení metadat a jazyků

### Zálohová faktura za top-up (DOC.BE.01.HR) [a (DOC.BE.01B.HR)]{.mark}

Advance invoice for top-up

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Zálohová faktura za předplacení kreditu - dobropis (DOC.BE.06)

Advance invoice for top-up - Credit note

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Faktura za mýtné (DOC.BE.10.HR) [a (DOC.BE.10B.HR)]{.mark}

Invoice for toll

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

| Č.  | [Název parametru]{.mark}       | Datový Typ | Povinný`<br>`{=html}*Ano/Ne* | Zdroj parametru`<br>`{=html}(Modul.) Entita.Atribut                     | Poznámka |
|-----|--------------------------------|------------|------------------------------|-------------------------------------------------------------------------|----------|
| 1   | Bill number                    | Number     | Ano                          | Bill.fiscal verification number, if null then Bill.bill number          |          |
| 2   | JIR                            | Text       | Ne                           | Bill.Variable symbol                                                    |          |
| 3   | ZKI                            | Text       | Ne                           | Bill.Variable symbol                                                    |          |
| 4   | Payment reference              | Text       | Ne                           | Bill.Variable symbol                                                    |          |
| 5   | Bill issuer                    | Text       | Ano                          | VCM.System operator                                                     |          |
| 6   | BIBA                           | Text       | Ano                          | VCM.BIBA                                                                |          |
| 7   | Customer number                | Text       | Ne                           | CM.Customer.number                                                      |          |
| 8   | Account number                 | Text       | Ne                           | CM.Account.number                                                       |          |
| 9   | Full name                      | Text       | Ne                           | CM.Customer.full name                                                   |          |
| 10  | Residential address            | Text       | Ne                           | CM.Customer.residential address                                         |          |
| 11  | Postal address                 | Text       | Ne                           | CM.Account.postal address                                               |          |
| 12  | Organization ID                | Text       | Ne                           | CM.Customer.organization ID                                             |          |
| 13  | VAT identification number      | Text       | Ne                           | CM.Customer.Personal identification number or VAT identification number |          |
| 14  | Bill date of issue             | Text       | Ano                          | Bill.date of issue                                                      |          |
| 15  | Bill date of beginning and end | Text       | Ano                          | Bill.date of beginning, Bill.date of end                                |          |
| 16  | Bill due date                  | Text       | Ano                          | Bill.due date                                                           |          |
| 17  | Bill total amount              | Text       | Ano                          | Bill.total amount                                                       |          |
| 18  | Bill item amount               | Text       | Ano                          | Bill item.price amount                                                  |          |
| 19  | Bill item tax base             | Text       | Ano                          | Bill item.tax base                                                      |          |
| 20  | Bill item category             | Text       | Ano                          | Bill item.bill item category                                            |          |
|     | Billing service                | Text       | Ano                          | Bill item.billing service                                               |          |
|     | Number of units                | Text       | Ano                          | Bill item.number of units                                               |          |
|     | Unit price                     | Text       | Ano                          | Bill item.unit price VAT                                                |          |
|     | Discount amount                | Text       | Ne                           | Bill item.discount amount VAT                                           |          |
|     | Payment card                   | Text       | Ne                           | Bill item.card number                                                   |          |
|     | Payment card type              | Text       | Ne                           | Bill item.card type                                                     |          |

: Tabulka : Seznam atributů entity Faktura

### [Detailní výpis mýtných transakcí k faktuře (DOC.BE.11)]{.mark}

#### CSV formát

Detailní výpis mýtných transakcí v csv formátu je generován jako příloha faktury (Customer bill z Bill session).

Záznamy jsou řazeny podle Registration number a Event time.

Název csv souboru bude odpovídat logice:

DS\_\[account number\]\_\[Bill.Date of beginning\]\_\[Bill.Date of end\]\_\[bill number\]\_\[document issue date\].csv

Příklad: DS_4101234567_20221001_20221015_1221205075_202210160345.csv

| Název sloupce`<br>`{=html}EN`<br>`{=html}CS`<br>`{=html}SK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Název atributu EN                                                                                                                                   | Typ             | Povinné      | Poznámky                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Account number (VCM)                                                                                                                                | Text            | Ano          | použije se ve jméně souboru, pokud existuje (DS pro pre-paid a post-paid bills)                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Bill.Date of beginning+Date of end (BAR)                                                                                                            | Date - interval | Ano          | použije se ve jméně souboru                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Bill.Bill number (BAR)                                                                                                                              | Number          | Ano          | použije se ve jméně souboru                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | document issue date                                                                                                                                 | Date Time       | Ano          | použije se ve jméně souboru                                                                                                                                                                                         |
| Registracija`<br>`{=html}Registration No.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Toll Transaction.Registration number (BAR)                                                                                                          | Text            | Ne           |                                                                                                                                                                                                                     |
| Zemlja`<br>`{=html}Country                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Toll Transaction.Registration country (BAR)                                                                                                         | Text            | Ne           |                                                                                                                                                                                                                     |
| [OBU serial number]{.mark}`<br>`{=html}[Výrobní číslo OBU]{.mark}`<br>`{=html}[Výrobné číslo OBU]{.mark}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Toll Transaction.OBU serial number]{.mark}                                                                                                         | [Text]{.mark}   | [Ano]{.mark} |                                                                                                                                                                                                                     |
| [Vehicle category]{.mark}`<br>`{=html}[Kategorie vozidla]{.mark}`<br>`{=html}[Kategória vozidla]{.mark}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Toll Transaction.Vehicle category (BAR)]{.mark}                                                                                                    | [Text]{.mark}   | [Ne]{.mark}  |                                                                                                                                                                                                                     |
| [Emission class]{.mark}`<br>`{=html}[Emisní třída]{.mark}`<br>`{=html}[Emisná trieda]{.mark}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Toll Transaction.Emission class (BAR)]{.mark}                                                                                                      | [Text]{.mark}   | [Ne]{.mark}  |                                                                                                                                                                                                                     |
| [Emission class CO2]{.mark}`<br>`{=html}[Emisní třída CO2]{.mark}`<br>`{=html}[Emisná trieda CO2]{.mark}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Toll Transaction.Emission class CO2 (BAR)]{.mark}                                                                                                  | [Text]{.mark}   | [Ne]{.mark}  |                                                                                                                                                                                                                     |
| Datum i vrijeme`<br>`{=html}Date and time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Toll Transaction.Event time (BAR)                                                                                                                   | Date Time       | Ano          |                                                                                                                                                                                                                     |
| Ulaz - Izlaz`<br>`{=html}Entry - Exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Toll Transaction.Toll segment name (BAR)                                                                                                            | Text            | Ano          |                                                                                                                                                                                                                     |
| Cestarina`<br>`{=html}Toll                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Součet Rated toll event.Price amount VAT pro jednu Toll Transaction (pro jeden průjezd) (BAR)`<br>`{=html}Toll Transaction.Transaction price amount | Money           | Ano          | Součet cen za jednotlivé složky mýtného za jeden průjezd                                                                                                                                                            |
| [Infrastructure]{.mark}`<br>`{=html}[Pozemní komunikace]{.mark}`<br>`{=html}[Pozemné komunikácie]{.mark}`<br>`{=html}[Pollution]{.mark}`<br>`{=html}[Znečištění ovzduší]{.mark}`<br>`{=html}[Znečistenie ovzdušia]{.mark}`<br>`{=html}[Noise]{.mark}`<br>`{=html}[Hluk z provozu]{.mark}`<br>`{=html}[Hluk z prevádzky]{.mark}`<br>`{=html}[Emissions CO2]{.mark}`<br>`{=html}[Emise CO2]{.mark}`<br>`{=html}[Emisie CO2]{.mark}`<br>`{=html}[Pollution - Noise]{.mark}`<br>`{=html}[Znečištění ovzduší a hluk z provozu]{.mark}`<br>`{=html}[Znečistenie ovzdušia a hluk z prevádzky]{.mark} | [Rated toll event.Charge type (BAR)]{.mark}                                                                                                         | [Text]{.mark}   | [Ne]{.mark}  | [Zobrazí se každý jednotlivý Charge type jako název sloupce a k němu odpovídající částka jako hodnota.]{.mark}`<br>`{=html}[Infrastraction]{.mark}`<br>`{=html}[Pollution]{.mark}`<br>`{=html}[Emission CO2]{.mark} |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Rated toll event.Price amount pro daný Charge type (BAR)                                                                                            | Money           | Ne           |                                                                                                                                                                                                                     |

: Tabulka : Seznam atributů detailního výpisu mýtných transakcí připojených k faktuře v csv formátu

### Vrubopis za mýtné (DOC.BE.13.HR)

Debit note for toll

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Dobropis za mýtné (DOC.BE.14.HR) 

Credit not efor toll

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Faktura za služby (DOC.BE.16.HR) 

Invoice for services

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Dobropis za služby (DOC.BE.17.HR) 

Credit note for services

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### [Faktura za smluvní pokutu (DOC.BE.19.HR)]{.mark} 

[Invoice for contractual penalty]{.mark}

[Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.]{.mark}

### [Dobropis za smluvní pokutu (DOC.BE.20.HR)]{.mark} 

[Credit note for contractual penalty]{.mark}

[Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury .]{.mark}

### eFaktura (DOC.BE.21.HR)

eInvoice

Jde o elektronickou fakturu ve formátu podle eFINA formátu, která se generuje v případě, že ji Zákazník, Partner nebo Poskytovatel mýtných služeb požaduje.

Tato XML verze se zasílá emailem společně s pdf verzí účetního dokladu případně přes eFINA. XML verze je k dispozici také na SC ke stažení.

Mapování atributů eFaktury na Billien 5.8 atributy:

[eFina_mapping_v01.xlsx](https://tollnetas-my.sharepoint.com/:x:/g/personal/zuzana_irova_tollnet_cz/EUnCEqCzuAhDv_iV1UshOVIBqObYn_uKvUYoWSBMGNHokQ?e=HPmdO5)

### Výzva k úhradě za přestupky (DOC.BE.22.HR)

Request for payment

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Výzva k úhradě za přestupky -- Dobropis (DOC.BE.23.HR) 

Request of Payment -- credit note

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

### Proforma faktura (DOC.BE.24.HR) 

Proforma bill

Šablona entity „Faktura" obsahuje různé části, tyto části závisí na subjektu, typu faktury.

## Externí oznámení (e-mail)

Notifikace (e-mail) slouží pro informování o vystavení účetních dokladů, jiných dokladů nebo o stavu probíhajícího procesu. PDF případných dokumentů je v příloze tohoto e-mailu.

**Tabulka 44: Notifikace -- e-mail**

| **Typ**                | **Jméno HR**                                              | **Jméno EN**                                                 | **Jméno CZ**                                         |
|------------------------|-----------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------|
| NTF.BAR.01.HR          | Obavijest o izdavanju računa za otplatu kredita unaprijed | Notification of a new Invoice for top-up                     | Oznámení o vystavení faktury za předplacení kreditu  |
| NTF.BAR.13.HR          | Obavijest o transakciji neplaćene cestarine               | Unpaid toll transaction notification                         | Oznámení o neúspěšné úhradě mýtné transakce          |
| [NTF.BAR.20.HR]{.mark} | [Oznámenie o zúčtovaní záväzkov a pohľadávok]{.mark}      | [Notice of settlement of liabilities and receivables]{.mark} | [Oznámenie o zúčtovaní záväzkov a pohľadávok]{.mark} |
| NTF.BAR.21.HR          | Obavijest o fakturi                                       | Notice of invoice issue                                      | Oznámení o vystavení faktury                         |
| NTF.DF.01.HR           | Obavijest o fakturi                                       | Notice of invoice issue                                      | Oznámení o vystavení účetního dokladu                |

### Společná nastavení -- e-mail

Externí oznámení jsou poplatná System operatorovi (logo, patička) - notifikace budou používat stejnou parent šablonu, teda hlavičky a patičky, jako notifikace CM.

Jako email odesílatele se použije hodnota System operator.Sender e-mail address Bill issuera.

#### Struktura e-mailu

- 
- 
- 

Externí oznámení (e-mail) jsou generovány jako dvoujazyčné, použité jazyky jsou vybrány podle následujících pravidel:

- [Primární jazyk je vždy chorvatština (hr)]{.mark}

- [Sekundární jazyk je vždy angličtina (en)]{.mark}

Externí oznámení (e-mail) má následující strukturu:

- Hlavička externího oznámení (hr)

- Obsah (hr)

- Patička externího oznámení (hr)

- Hlavička externího oznámení (en)

- Obsah (en)

- Patička externího oznámení (en)

##### Hlavička externího oznámení (hr)

Poštovani gospodine/gospođo, «konec řádky»

«mezera»

##### Hlavička externího oznámení (en)

Dear customer, «konec řádky»

«mezera»

##### [Patička externího oznámení HAC (hr)]{.mark}

[«mezera»]{.mark}

[Srdačan pozdrav, HAC d.o.o.]{.mark}

[«praznine»]{.mark}

[Call centar (24/7): 0800 0422]{.mark}

[Email: info-naplata@hac.hr]{.mark}

[«mezera»]{.mark}

##### [Patička externího oznámení HAC (en)]{.mark}

[«mezera»]{.mark}

[With best regards,]{.mark}

[HAC d.o.o.]{.mark}

[«mezera»]{.mark}

[Call centre (24/7): 0800 0422 or +385 1 6504 899]{.mark}

[Email: info-naplata@hac.hr]{.mark}

[«mezera»]{.mark}

##### [Patička externího oznámení BINA-Istra (hr)]{.mark}

[«mezera»]{.mark}

[Srdačan pozdrav, BINA-ISTRA d.d.]{.mark}

[«praznine»]{.mark}

[Call centar (24/7): 0800 0422]{.mark}

[Email: info-naplata@hac.hr]{.mark}

[«mezera»]{.mark}

##### [Patička externího oznámení BINA-Istra (en)]{.mark}

[«mezera»]{.mark}

[With best regards,]{.mark}

[BINA-ISTRA d.d.]{.mark}

[«mezera»]{.mark}

[Call centre (24/7): 0800 600 601]{.mark}

[Email:]{.mark}

[«mezera»]{.mark}

##### [Patička externího oznámení AZM (hr)]{.mark}

[«mezera»]{.mark}

[Srdačan pozdrav, AZM d.o.o.]{.mark}

[«praznine»]{.mark}

[Call centar (24/7): 0800 600 601]{.mark}

[Email:]{.mark}

[«mezera»]{.mark}

##### [Patička externího oznámení AZM (en)]{.mark}

[«mezera»]{.mark}

[With best regards,]{.mark}

[AZM d.o.o.]{.mark}

[«mezera»]{.mark}

[Call centre (24/7):]{.mark}

[Email:]{.mark}

[«mezera»]{.mark}

### Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR)

Notification of a new Invoice for top-up

#### Popis

Oznámení slouží pro informování zákazníka o vystavení faktury po úspěšném předplacení kreditu.

#### Předmět

Obavijest o izdavanju računa za otplatu kredita unaprijed (Notification of a new Invoice for top-up)

#### Obsah (hr)

ovim putem Vas obavještavamo da je u privitku e-maila dostupan za preuzimanje novi Račun za nadoplatu.

Ako imate bilo kakvih pitanja, molimo kontaktirajte našu liniju za korisnike.

#### Obsah (en)

we hereby inform you that in the email attachment a new Invoice for top-up is available for download.

If you have any questions, please contact our Customer hotline.

### Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction notification) (NTF.BAR.13.HR)

#### Popis

Oznámení slouží pro informování PV o neúspěšné úhradě mýtné transakce při online platbě nebo předplaceným kreditem.

Oznámení se odesílá v následujících případech:

1.  Po vytvoření Unpaid Toll Transaction s Pre-paid registration type, kdy nebyl dostatečný zůstatek na pre-paid balance (SYS.BAR.1.8.HR)

2.  Po neúspěšném posledním pokusu o uhrazení uloženým tokenem platební karty Unpaid Toll Transaction s Post-paid card registration type (SYS.BAR.1.10.HR)

#### Předmět

Obavijest o transakciji neplaćene cestarine / Unpaid toll transaction notification

#### Obsah (hr)

obavještavamo vas da je pokušaj plaćanja cestarine bio neuspješan.

#### Obsah (en)

We would like to inform you that the attempt to pay the toll transaction was unsuccessful.

### Oznámení o vystavení faktury (NTF.BAR.21.HR)

Notification of an Accounting document

#### Popis

Oznámení slouží pro informování zákazníka o vystavení nového (jednorázového) účetního dokladu.

#### Předmět HR

Obavijest o fakturi

#### Předmět EN

Notice of invoice issue

#### Obsah HR

obavještavamo Vas da smo izdali račun br. [«BAR.Bill.Bill number»]{.mark} na vaš korisnički račun [1.\[na vašom mýtnom účte «Account.Number»\]]{.mark}. Račun možete pronaći u privitku ovog e-maila.

[1.\[ Svi računi dostupni su iu zoni samoposluživanja, gdje ih možete preuzeti u bilo kojem trenutku.\]]{.mark}

> Varianty:

1.  [\[uvést, pokud jde o Account\]]{.mark}

#### Obsah EN

Please be advised that we have [1.\[on your toll account «Account.Number»\]]{.mark} issued invoice number \"BAR.Bill.Bill number\". Please find the invoice attached to this email.

[1.\[All invoices are also available in the self-service area where you can download them at any time.\]]{.mark}

> Varianty:

1.  [\[uvést, pokud jde o Account\]]{.mark}

### Oznámení o vystavení účetního dokladu (NTF.DF.01.HR) 

Notification of an Accounting document

#### Popis

Oznámení slouží pro informování o vystavení účetních dokladů za mýtné, služby, případně RfP generované z fakturační dávky (Bill Session).

Definice notifikace přesunuta do FS DFRP.

## [Externí oznámení (SMS)]{.mark}

Notifikace (SMS) slouží pro informování o stavu probíhajícího procesu.

**Tabulka 45: Notifikace**

| **Typ**       | **Jméno HR**                                | **Jméno EN**                         | **Jméno CZ**                                |
|---------------|---------------------------------------------|--------------------------------------|---------------------------------------------|
| NTF.BAR.14.HR | Obavijest o transakciji neplaćene cestarine | Unpaid toll transaction notification | Oznámení o neúspěšné úhradě mýtné transakce |

### [Společná nastavení -- SMS]{.mark}

#### Struktura SMS

[Externí oznámení (SMS) jsou generovány jako jednojazyčné, konkrétní jazyk je vybrán podle země odvozené od telefonního čísla (CO.Country.Phone prefix) a na základě konfigurovatelného atributu Country.Document language extended set (konfigurace pro každou zemi z výběru jazyků číselníku Language s Is document language = Ano).]{.mark}

Externí oznámení (SMS) má následující strukturu:

- Hlavička externího oznámení (xx) + Obsah (xx),

- kde (xx) je vybraný jazyk

Dále je uvedena chorvatská (hr) a anglická (en) mutace.

#### Hlavička externího oznámení (hr)

Poštovani gospodine/gospođo,

#### Hlavička externího oznámení (en)

Dear customer,

### Oznámení o neúspěšné úhradě mýtné transakce (Unpaid toll transaction SMS notification) (NTF.BAR.14.HR)

#### Popis

Oznámení slouží pro informování PV o neúspěšné úhradě mýtné transakce při online platbě nebo předplaceným kreditem.

Oznámení se odesílá v následujících případech:

1.  Po vytvoření Unpaid Toll Transaction s Pre-paid registration type, kdy nebyl dostatečný zůstatek na pre-paid balance (SYS.BAR.1.8.HR)

2.  Po neúspěšném posledním pokusu o uhrazení uloženým tokenem platební karty Unpaid Toll Transaction s Post-paid card registration type (SYS.BAR.1.10.HR)

#### Předmět

Není

#### Obsah (hr)

obavještavamo vas da je pokušaj plaćanja cestarine bio neuspješan. [1.\[HAC d.o.o.\] 2.\[BINA-ISTRA d.d.\] 3.\[AZM d.o.o.\]]{.mark}

[Délka textu: cca 77 znaků.]{.mark}

Varianty:

1.\[(System operator = HAC)\]

2.\[(System operator = BINA-Istra)\]

3.\[(System operator = AZM)\]

#### Obsah (en)

We would like to inform you that the attempt to pay the toll transaction was unsuccessful. . [1.\[HAC d.o.o.\] 2.\[BINA-ISTRA d.d.\] 3.\[AZM d.o.o.\]]{.mark}

[Délka textu: cca 101 znaků.]{.mark}

Varianty:

1.\[(System operator = HAC)\]

2.\[(System operator = BINA-Istra)\]

3.\[(System operator = AZM)\]

## Výměnné soubory

### Rozhraní TC HR -- HAC (INT.BAR.26.HR)

#### BD-HR: Billing details -- doména HR -2022 (DEX.BAR.29.HR)

##### Popis

Soubor slouží k předání Billing details HR oceněných Toll Chargerem HAC příslušným Poskytovatelům mýtných služeb.

Billing details jsou podle [ISO 12855:2022.]{.mark}

##### Základní vlastnosti

| **Vlastnost**                                   | **Hodnota**                                                                  |
|-------------------------------------------------|------------------------------------------------------------------------------|
| Identifikační číslo                             | DEX.BAR.29.HR                                                                |
| Plný název                                      | [BillingDetailsHr2022]{.mark}                                                |
| Název souboru (Export)                          | N/A                                                                          |
| Požadovaný název souboru (Import) -- File Regex | BillingDetails_YYYYMMDD_hhmmss_GUID`<br>`{=html}\^BillingDetails\_.+\\.xml\$ |
| Formát souboru                                  | XML                                                                          |

: Tabulka : Základní vlastnosti výměnného souboru

| Jazykové verze (CZ/EN)                                                                                | N/A                                |
|-------------------------------------------------------------------------------------------------------|------------------------------------|
| Kódování                                                                                              | UTF-8                              |
| Směr (Import/Export)                                                                                  | Export                             |
| Externí systém                                                                                        | EETS Provider                      |
| Maximální velikost souboru (Import)                                                                   | 5 MB                               |
| Povolené generování/přijetí prázdného souboru                                                         | Ano                                |
| Soubor má hlavičku                                                                                    | N/A                                |
| Zasílá se potvrzení o přijetí protistraně (Import)/Očekává se odpověď o přijetí protistranou (Export) |                                    |
| Úložiště pro vygenerované/přijímané soubory                                                           | .\\Files\\EETS\\HR\\BillingDetails |

##### Parametry

Realizace podle aktuální specifikace BillingDetails na Confluence.

1.  ACK-HR: EETS List Acknowledgement - doména HR (DEX.BAR.100.HR)

    1.  Popis

> Příchozí nebo odchozí zpráva prostřednictvím Rozhraní EETS pro odesílání a příjem EDE zpráv (INT.CO.20), sloužící k:

- přijetí potvrzení od příslušného EETS Provider o přijetí zprávy/souboru

- odeslání potvrzení příslušnému EETS Provider o přijetí zprávy/souboru

[EETS List Acknowledgement je podle ISO 12855:2022.]{.mark}

1.  Základní vlastnosti

| **Vlastnost**                                                                                         | **Hodnota**                  |
|-------------------------------------------------------------------------------------------------------|------------------------------|
| Identifikační číslo                                                                                   | DEX.BAR.00.HR                |
| Plný název                                                                                            | EETS List Acknowledgement HR |
| Název souboru (Export)                                                                                | N/A                          |
| Požadovaný název souboru (Import) -- File Regex                                                       | N/A                          |
| Formát souboru                                                                                        | XML                          |
| Jazykové verze (CZ/EN)                                                                                | N/A                          |
| Kódování                                                                                              | [UTF-8]{.mark}               |
| Směr (Import/Export)                                                                                  | Import                       |
| Externí systém                                                                                        | N/A                          |
| Maximální velikost souboru (Import)                                                                   | [10 MB]{.mark}               |
| Povolené generování/přijetí prázdného souboru                                                         | Ano                          |
| Soubor má hlavičku                                                                                    | N/A                          |
| Zasílá se potvrzení o přijetí protistraně (Import)/Očekává se odpověď o přijetí protistranou (Export) | Ne                           |
| Úložiště pro vygenerované/přijímané soubory                                                           | [TBD]{.mark}                 |

: Tabulka : Základní vlastnosti výměnného souboru

2.  Parametry

> Detailní technická specifikace je uvedena v dokumentu „EETS_TS_Ack_EN.xlsx" a dále v odpovídajících XSD schématech.

| Č.  | Název parametru (CZ) | Datový Typ | Povinný`<br>`{=html}*Ano/Ne* | Zdroj parametru`<br>`{=html}(Modul.) Entita.Atribut | Poznámka |
|-----|----------------------|------------|------------------------------|-----------------------------------------------------|----------|

: Tabulka : Vybrané parametry EDE zprávy ACK-HR

|                                                           |                       |               |     |     |                                                                                                                                        |
|-----------------------------------------------------------|-----------------------|---------------|-----|-----|----------------------------------------------------------------------------------------------------------------------------------------|
| **InfoExchange/infoExchangeContent/adus/ackADUs/AckADU/** |                       |               |     |     |                                                                                                                                        |
| 1                                                         | apduIdentifier        | Number        | Ano |     | Číslo APDU                                                                                                                             |
| 2                                                         | apduAckCode           | Number (Enum) | Ano |     | Návratová hodnota                                                                                                                      |
| 3                                                         | Issues/issueADUStruct | Number        | Ne  |     | 0 -- Zamítnutí celé zprávy`<br>`{=html}1 -- Chyba v konkrétní položce                                                                  |
| 4                                                         | Issues/issueLocation  | Text          | Ne  |     | Cesta k identifikovanému elementu ve formátu XPath                                                                                     |
| 5                                                         | Issues/issueContent   | Text          | Ne  |     | Hodnota elementu identifikovaného v issue/issueLocation                                                                                |
| 6                                                         | Issues/issueCode      | Number        | Ne  |     | Chybový kód - v případě, kdy normou předdefinovaný issueCode nepokrývá nastalou situaci, bude využíván issueCode = acceptedWithWarning |
| 7                                                         | Issues/issueText      | Text          | Ne  |     | Detailní popis zachycené situace při zpracování přijaté zprávy                                                                         |