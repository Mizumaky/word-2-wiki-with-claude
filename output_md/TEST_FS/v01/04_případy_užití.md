# Případy užití

Sloupec **Realizace** určuje způsob implementace příslušného UC:

- New -- nový UC jen pro daný projekt

- Upd -- UC upravený (customizovaný) pro daný projekt

- AsIs -- UC beze změny

- N/A -- nebude používán

| **Funkční oblast**             | **Případ užití**                                                       | **BO** | **FO** | **SC** | **Realizace** | **Aktér**                              |
|--------------------------------|------------------------------------------------------------------------|--------|--------|--------|---------------|----------------------------------------|
| Operace s platbami             | Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1)    | *X*    | *X*    | *X*    | *N/A*         | *SC User, POS operator*                |
|                                | Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR) | *X*    | *X*    | *X*    | *Upd*         | *SC User, POS operator, System*        |
|                                | Zaplať depozit (UC.BAR.0.2)                                            | *X*    | *X*    | *X*    | *N/A*         | *BO operator, SC User,* *POS operator* |
|                                | Uhraď poplatek na FO (UC.BAR.0.3)                                      |        | *X*    |        | *N/A*         | *POS operator*                         |
|                                | Zaplať poplatek na FO (UC.BAR.0.3.HR)                                  |        | *X*    |        | *Upd*         | *POS operator*                         |
|                                | Vrať depozit (UC.BAR.0.4.VO1)                                          | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Zaplať předplacený kredit -- Pre-paid (UC.BAR.0.5)                     | *X*    | *X*    | *X*    | *N/A*         | *SC User, POS operator*                |
|                                | Storno platby (UC.BAR.0.6)                                             | *X*    | *X*    |        |               | *BO operator, POS operator*            |
|                                | Načti bankovní výpis (UC.BAR.0.7.VO1)                                  | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Rozpoznej položku bankovního výpisu (UC.BAR.0.8.VO1)                   | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Zruš rozpoznání platby (UC.BAR.0.9.VO1)                                | *X*    |        |        |               | *BO operator*                          |
|                                | Napáruj fakturu na platbu (UC.BAR.0.10.VO1)                            | *X*    |        |        |               | *BO operator*                          |
|                                | Napáruj platbu na fakturu (UC.BAR.0.11.VO1)                            | *X*    |        |        |               | *BO operator*                          |
|                                | Odpáruj platbu (UC.BAR.0.12.VO1)                                       | *X*    |        |        |               | *BO operator*                          |
|                                | Napáruj fakturu na fakturu (UC.BAR.0.13.VO1)                           | *X*    |        |        |               | *BO operator*                          |
|                                | Odpáruj fakturu z faktury (UC.BAR.0.14.VO1)                            | *X*    |        |        |               | *BO operator*                          |
|                                | Vrať platbu (UC.BAR.0.15.VO1)                                          | *X*    |        |        |               | *BO operator*                          |
|                                | Schval položku platebního příkazu (UC.BAR.0.16.VO1)                    | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Změň položku platebního příkazu (UC.BAR.0.17.VO1)                      | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Zamítni položku platebního příkazu (UC.BAR.0.18.VO1)                   | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Vytvoř soubor platebních příkazů (UC.BAR.0.19.VO1)                     | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Uhraď přestupek (UC.BAR.0.20.HR)                                       | *X*    | X      | X      | *New*         | *BO Operator*                          |
|                                | Zaplať Produktový balíček (UC.BAR.0.21.HR)                             | *X*    | X      | X      | *New*         | *BO Operator*                          |
|                                | Zaplať OBU (UC.BAR.0.22.HR)                                            | *X*    | X      | X      | *New*         | *BO Operator*                          |
|                                |                                                                        |        |        |        |               |                                        |
|                                | Přesuň platbu (UC.BAR.0.30.VO2)                                        | *X*    |        |        | *N/A*         | *BO operator*                          |
| Podpůrné operace               | Načti soubor mýtných segmentů (UC.BAR.1.1)                             | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                |                                                                        |        |        |        |               |                                        |
| Operace na vyžádání zákazníkem | Vytvoř detailní výpis mýtných transakcí na vyžádání (UC.BAR.2.1.VO1)   |        |        | *X*    |               | *WSC User*                             |
| Operace s fakturami            | Vytvoř korekci (UC.BAR.3.1.VO1)                                        | *X*    |        |        |               | *BO operator*                          |
|                                | Uhraď dobropis (UC.BAR.3.2.VO1)                                        | *X*    |        |        |               | *BO operator*                          |
|                                | Vytvoř proforma fakturu (UC.BAR.3.3.HR)                                | *X*    | X      | X      | *New*         | *BO Operator*                          |
| Správa slev                    | Odešli oznámení o novém nároku na slevu v doméně CZ (UC.BAR.4.1)       | *X*    |        |        | *N/A*         | *BO operator*                          |
|                                | Potvrď nárok na slevu v doméně CZ (UC.BAR.4.2)                         |        |        |        | *N/A*         | *BO operator*                          |

: Tabulka 32: Seznam případů užití

## 

[]{#_Toc205285685 .anchor}Operace s platbami

### Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

#### Cíl

Cílem tohoto případu užití je navýšení předplaceného kreditu Pre-paid účtu.

#### 

AktéřiPOS Operator, System, Customer

#### Spuštění případu

Případ užití je vloženou součástí případu užití:

- [Dobi predplatený kredit (UC.VCM.4.2)]{.mark},

Na základě požadavku na Top-up z rozhraní:

- Rozhraní ERP Navision (INT.BAR.30.HR)

- Rozhraní Web portal API (INT.BAR.33.HR)

- Rozhraní interní POS API (INT.BAR.34.HR)

- Rozhraní interní KIOSK API (INT.BAR.35.HR)

- Rozhraní interní IEFBO API (INT.BAR.36.HR)

<!-- -->

- 

#### Podmínky spuštění

Account je znám.

Account type je Pre-paid.

[Account není terminovaný.]{.mark}

[Pokud Customer není anonymní (tj. Anonymous registration = false) a zároveň Account status je Terminated, Systém přenastaví Account do stavu Active?]{.mark}

Výše top-up je známa.

Bill issuer je znám (tj. System operator).

Způsob platby je znám.

Případně POS je známa.

#### Normální postup

(N1) Předplať kredit na vlastní POS, externí POS, Kiosku nebo MEV

Systém zobrazí aktuální výši balance (BM.Balance.amount - BM.Balance.Reservation amount - [Grace period amount]{.mark}).

Systém zobrazí minimální zaokrouhlenou výši kreditu:

- Pokud aktuální balance \< 0, pak MAX (absolutní hodnota aktuální výše balance; BAR.Currency.Minimum top-up amount),

- jinak BAR.Currency.Minimum top-up amount.

Aktér vybere částku z předdefinovaných hodnot (tj. Currency.GUI top-up value 1-4) nebo Aktér zvýší nebo potvrdí částku minimálního top-up.

Systém zkontroluje, zda částka je \<= hodnotě Currency.Max Top-up, pokud není, Aktér je vyzván k úpravě částky top-up.

Pokud zadaná částka kreditu (zaokrouhlená na celé číslo), je vyšší než hodnota Currency.MaxTop-upCash, Systém neumožní vybrat platbu v hotovosti.

Aktér může vybrat, zda se zároveň má tokenizovat platební karta.

Postup pokračuje realizací platby top-up za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(N2) Předplať kredit na Web Portal nebo Mobile app - online platba přes platební bránu

Placení z Web portálu nebo Mobile App je popsáno v systémové funkci Zprocesuj transakci platební kartou (API.BAR.0.1.HR):

- Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši zadaného Top-up, Bill issuer a Account.

- Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

- Pokud transakce byla úspěšná (tj.Payment session.status = Realized), proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.

- Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(N3) Předplať kredit na Web Portal nebo Mobile app -- jiná platební metoda než online platba přes platební bránu]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši zaplaceného Top-up, typu platební metody (např SMS, Voucher), Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).]{.mark}

[(N4) Předplať kredit přes HR Toll aplikaci]{.mark}

[Systém na vstupu přes Rozhraní HR Toll API (INT.BAR.34.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody, Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(N5) [Předplať kredit]{.mark} bankovním převodem na základě Proforma faktury

[Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody (bank transfer), Proforma bill, Bill issuer.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

Společný postup pro všechny platební metody

Systém o částku top-up platby navýší zůstatek předplaceného kreditu, použije se případ užití Aktualizuj zůstatek (SYS.BM.1.2.HR) s důvodem updatu balance = TopUp.

Systém zjistí údaje o top-up na základě Bill issuer, [Bill issuer VAT registration country, VAT registration country zákazníka, VAT registration country zákazníka,]{.mark} Product type = Top-up a Event attribute Top-up = Top-up (za použití případu užití Získej produkt (SYS.PCRE.1.2.HR)).

Systém vygeneruje jednorázovou fakturu za mýto za užití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

Systém napáruje nově vytvořený Bill na nově vytvořený Payment, tj. vytvoří Matching s následujícími parametry:

- Date of matching = aktuální datum

- Effective date of matching = vyšší z datumů párovaných stran (tj. payment.date of collection, bill.date od end)

- Bill -- debit matching side = vytvořený Bill

- Payment -- credit matching side = vytvořený Payment

- Matched amount = částka zaplaceného top-up

- Matching method = Automatic

- Disconnect allowed = True

Systém na základě provedého párování updatuje atributy napárovaného Bill:

- Matched amount = částka zaplaceného top-up (tj. Bill.total amount),

- Bill payment status = Paid fully.

Systém na základě provedého párování updatuje atributy napárovaného Payment:

- Matched amount = částka zaplaceného top-up (tj. Payment amount),

- Matching status = Recognized -- matched.

[Pokud šlo o platbu tankovací kartou, Systém zagreguje platbu do odpovídajícího FCI RfP, využitím případu užití Zagreguj platby tankovací kartou do FCI RfP (SYS.BAR.0.9).]{.mark}

Postup končí.

#### Alternativní postupy 

[(A1) Bez platby -- Proforma (na BO, vlastní POS, externí POS nebo MEV )]{.underline}

Pokud Aktér bude chtít jako platební metodu bankovní převod, iniciuje vytvoření nabídky (tj. Proforma faktury (Offer)) zmáčknutím příslušného tlačítka a spuštěním případu užití Vytvoř proforma fakturu (UC.BAR.3.3.HR).

Postup končí.

Postup končí.

(A2) Bez platby-- Proforma (Web portal nebo Mobile app)

Pokud Zákazník na exerním Web portálu nebo Mobile app bude chtít jako platební metodu bankovní převod, Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Top-up, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem. Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR):

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

Postup končí.

#### Chybové postupy

Neúspěšná transakce

> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém informuje Aktéra o neúspěšné transakci (pokud proces byl inicializován v rámci Systému) a Aktér může pokračovat od začátku úpravou výše Top-up nebo proces ukončit.
>
> [Neúspěšná online transakce]{.underline}
>
> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém vrátí odpovídající result externímu systému (pokud proces byl inicializován z externího systému).

#### Grafické rozhraní

N/A

#### Poznámky

Nejsou

### Zaplať poplatek na POS (UC.BAR.0.3.HR)

#### 

CílCílem tohoto případu užití je zaplacení poplatku při vystavení jednorázové faktury na vlastní nebo externí POS používající POS aplication.

#### 

AktéřiPOS Operator, Customer

#### 

Spuštění případuJe vloženou součástí případu užití:

- Top-up

  - Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

    - na POS, externí POS, Kiosku nebo MEV

- Přestupek

  - Uhraď přestupek (UC.BAR.0.20.HR)

    - na POS, externí POS, Kiosku nebo MEV

- OBU

  - Zaplať OBU (UC.BAR.0.22.HR), Objednaj OBU (UC.VCM.2.8)

    - na POS, externí POS nebo MEV

- Produktový balíček

  - Zaplať Produktový balíček (UC.BAR.0.21.HR), Pridaj produktový balíček (UC.VCM.1.6)

    - na POS, [externí POS]{.mark},

- OBU příslušenství

  - Prodej příslušenství OBU na POS (UC.OL.1.7.HR)

    - na POS, externí POS,

- [VCM poslani OBU]{.mark}

#### 

Podmínky spuštěníKanál prodeje je vlastní nebo externí POS (je známa POS a Bill issuer) nebo MEV nebo Kiosk.

Je známa částka k úhradě, případně oceněná událost a typ operace (top-up, placení offence, prodej OBU, prodej produktu, objednání OBU, objednání produktu\...).

Volitelně je znám Account.

[Account není terminovaný.]{.mark}

#### 

Normální postupSystém zobrazí částku na zaplacení s přesností na dvě desetinná místa.

Aktér vybere platební metodu:

- Na vlastní a externí POS jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (NexGo (INT.BAR.28.HR)) s možností tokenizace karty při top-up

  - hotovost

  - [bankovním převodem (vystaví se jen Offer s platebními údaji).]{.mark}

- Na KIOSKU jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (Ingenico (rozhraní INT.BAR.29.HR))

- Na MEV jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (NexGo (INT.BAR.28.HR)) s možností tokenizace karty při top-up

  - hotovost

Poznámka: platba bankovní a palivovou kartou přes HR Toll app v EFT (NexGo (INT.BAR.28.HR)) je řešena v rámci systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR)

(N1) Bank card nebo Fleet card payment přes terminál na POS nebo MEV

Aktér vloží kartu do EFT terminálu přes Rozhraní EFT Terminal NexGo (INT.BAR.28.HR).

EFT terminal rozpozná platbu bankovní/tankovací kartou.

EFT terminal autorizuje platbu pomocí karetního autorizačního centra. V případě, že EFT terminal zamítne autorizaci, Systém zobrazí informaci, že "Platba nebyla autorizována" a postup pokračuje opětovnou volbou platební metody.

Systém získá data o platbě a případně také o tokenu z EFT terminálu z Rozhraní EFT Terminal NexGo (rozhraní INT.BAR.28.HR).

Systém vytvoří Payment Session:

- Online payment identifier = číslo transakce z EFT

- Payment session type =

  - Top-up, pokud Product type = Top-up

  - [Offence, pokud jde o placení přestupků (placení UTT ve stavu Offence),]{.mark}

  - 

  - Offence RfP payment, pokud jde o placení RfP za přestupky,

  - jinak Services.

- Payment session status = Realized

- Payment amount = částka platby z EFT

- Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

- Internet banking channel = EFT payment

- Created on = aktuální datum a čas

- Authorization code = autorizační kód z EFT

- Result code = návratový kód z EFT

- Card type = Typ karty z EFT

- Card expiry = Expirace karty z EFT

- Card number = Číslo karty z EFT

- Card brand = Brand karty z EFT

- Card token = Token karty z EFT

- EFT terminal = Identifikátor platebního terminálu z EFT

Pokud na vstupu byla požadována zároveň tokenizace platební karty, Systém získaný token a informace o Payment card uloží na Accountu za použití systémové funkce Pridaj platobnú kartu (SYS.VCM.4.1).

(N2) Bank card nebo Fleet card payment přes terminál na KIOSKu

Aktér vloží kartu do EFT terminálu přes Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR).

EFT terminal rozpozná platbu bankovní/tankovací kartou.

EFT terminal autorizuje platbu pomocí karetního autorizačního centra. V případě, že EFT terminal zamítne autorizaci, Systém zobrazí informaci, že "Platba nebyla autorizována" a postup pokračuje opětovnou volbou platební metody.

Systém získá data o platbě z EFT terminálu z Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR).

Systém vytvoří Payment Session:

- Online payment identifier = číslo transakce z EFT

- Payment session type =

  - Top-up, pokud Product type = Top-up

  - Offence RfP payment, pokud jde o placení RfP za přestupky,

  - jinak Services.

- Payment session status = Realized

- Payment amount = částka platby z EFT

- Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

- Internet banking channel = EFT payment

- Created on = aktuální datum a čas

- Authorization code = autorizační kód z EFT

- Result code = návratový kód z EFT

- Card type = Typ karty z EFT

- Card expiry = Expirace karty z EFT

- Card number = Číslo karty z EFT

- Card brand = Brand karty z EFT

- EFT terminal = Identifikátor platebního terminálu z EFT

(N3) Hotovost na POS nebo MEV

[Systém potřebnou částku za poplatek placenou hotovostí zaokrouhlí na nejbližší pěticent (tj. 102,02 🡪 102,00; 102,03 🡪 102,05; 102,26 🡪 102,25; 99,97 🡪 99,95; 99,98 🡪 100,00).]{.mark}

Aktér převezme zaokrouhlenou částku v hotovosti od zákazníka a zaregistruje Platbu.

Společný postup pro všechny platební metody

Systém zjistí BIBA pro fakturaci na základě Bill issuer ze vstupu a Reason:

- Offence, pokud jde o Offence operaci

- Top-up, pokud jde o Top-up operaci

- [OBU, pokud jde o OBU operaci]{.mark}

- Product, pokud jde o Product package operaci

- jinak Services.

Systém vytvoří Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type =

  - Top-up payment, pokud jde o Top-up operaci,

  - Offence payment, pokud jde o placení Offence RfP operaci,

  - OBU payment, pokud jde o OBU operaci,

  - OBU accessories payment, pokud jde o OBU accessories operaci,

  - Product payment, pokud jde o Product package operaci,

  - jinak Bill payment.

- Payment method =

  - pokud Payment session.internet banking channel = EFT payment a Card type má Card type.type = Bank card, pak Bank card payment,

  - pokud Payment session.internet banking channel = EFT payment a Card type má Card type.type = Fleet card, pak Fleet card payment,

  - pokud na vstupu byla platební metoda Cash, pak Cash payment.

- Payment category = Credit payment

- Payment status = Realized

- Matching status = Recognized -- not matched

- Variable symbol = Variable symbol z Payment session, pokud existuje, jinak Null

- Specific symbol = Subject number

- Payment amount = částka platby

- Matched amount = 0

- Date of payment = aktuální datum

- Date of collection = aktuální datum

- Comment = null

- Subject type = Account

- Subject number = VCM.VT Account.number

- POS = obchodní místo, kde byla provedena platba

- FCI = FCI karty, v případě platby tankovací kartou

- Bill issuer bank account = zjištěné číslo bankovního účtu Bill issuera (BIBA)

- Bill issuer = Bill issuer ze vstupu

[Pokud šlo o platbu tankovací kartou, Systém zagreguje platbu do odpovídajícího FCI RfP, využitím případu užití Zagreguj platby tankovací kartou do FCI RfP (SYS.BAR.0.9).]{.mark}

Postup končí.

#### 

Alternativní postupyNejsou

#### 

Chybové postupyNejsou

#### 

Grafické rozhraníPOS:

### Uhraď přestupek (UC.BAR.0.20.HR)

1.  

> CílCílem tohoto případu užití je uhradit jeden nebo více Výzev na úhradu (Offence RfP), ve kterých je zahrnut přestupek a zákonná pokuta.

2.  

> AktéřiOffence Portal User, POS Operator, Customer, System

3.  

Spuštění případuOffence portal:

- 
- 
- 
- 

Otevření stránky Offence portálu, a zadání Registrační značky vozidla a PIN, který byl vygenerován pro danou registrační značku a který provozovatel vozidla obdržel v dopise po vygenerování Výzvy na úhradu daného vozidla.Otevření linku a zadání PIN, který provozovatel vozidla obdržel v dopise po vygenerování Výzvy na úhradu daného vozidla. (Poznámka: Link obsahuje jak registrační značku tak zemi registrace, takže není potřeba je již vyplňovat. Musí se zadat jen PIN vygenerovaný pro danou SPZ).[Anonymní registrací na stránce Offence portálu za použití případu užití Zaregistruj vozidlo cez Offence Portal (UC.VCM.1.7.HR)]{.mark}Přihlášením do Offence portálu na základě zákaznických přihlašovacích údajů za použití sytémové funkce Přihlaš uživatele (UC.AC.21).POS, MEV:

- 
- 

Zadáním Registrační značky vozidla, pro které se mají najít Přestupky. Případně zadáním Customera nebo Accountu, pro jehož vozidla se mají najít přestupky.KIOSK:

- 

Rozpoznaná Registrační značka vozidla, pro které se mají najít Přestupky.

Na základě požadavku na zaplacení Přestupku z rozhraní:

- Rozhraní ERP Navision (INT.BAR.30.HR)

- Rozhraní Web portal API (INT.BAR.33.HR)

- Rozhraní POS API (INT.BAR.34.HR)

- Rozhraní KIOSK API (INT.BAR.35.HR)

- Rozhraní IEFBO API (INT.BAR.36.HR)

  1.  

> Podmínky spuštěníJe známo vozidlo, účet nebo zákazník na kterém se mají uhradit Přestupky.

2.  

> Normální postupSystém vyhledá všechny Výzvy na úhradu za přestupky (tj. Bill s Bill type = Request for payment, a Bill issue type = Regular bill nebo Simplified bill, a Bill category = Offence, a Bill payment status = Unpaid nebo Paid Partially a kde zároveň je Matched Amount \< Total amount) pro:

- Registrační značky všech vozidel daného zákazníka, pokud je znám ze vstupu jen zákazník (např. došlo k přihlášení existujícího zákazníka) (subject RfP není limitován zákazníkem),

- pro Registrační značky všech vozidel daného účtu, pokud je znám ze vstupu jen účet (např. přišel požadavek z Web selfcare) (subject RfP není limitován účtem),

- pro danou Registrační značku, pokud je známa ze vstupu Registrační značka vozidla (např. přihlášení za pomocí linku a PIN nebo na Kiosku).

> Systém zobrazí úvodní přehled obsahující maximálně 3 položky. Každá položka bude součtem nalezených Výzev na úhradu sečtených per Bill issuer s detaily:

- Toll charger 🡪 Bill.bill issuer

- Time period 🡪 MIN(Bill.date of issue) a MAX(Bill.date of issue)

- Amount to pay 🡪 SUM(Bill.total amount -- Bill.matched amount)

> Pokud jde o Kiosek, z úvodního přehledu Aktér může každou jednotlivou souhrnnou položku zaplatit nebo přeskočit proces placení přestupků.
>
> Pokud nejde o Kiosek, z úvodního přehledu Aktér může každou jednotlivou souhrnnou položku zaplatit nebo zobrazit si její detail.
>
> Pokud aktér vybral zaplacení konkrétní souhrnné položky, postup pokračuje (N1) Zaplať přestupek online.
>
> Pokud Aktér vybere zobrazení detailu, Systém zobrazí položky zahrnuté do dané vybrané souhrnné položky = přehled aktuálně evidovaných Výzev na úhrady daného Bill issuera s možností každou vybrat pro zaplacení nebo zobrazit její detaily:

- Bill.bill issuer

- Bill.registration number + .registration country

- Account.number

- Customer.number

- Customer.full name

- Bill.date of issue

- Bill.total amount -- Bill.matched amount

- Unpaid Toll Transaction s možností zobrazit detaily:

  - Unpaid Toll Transaction.event time (by default seřazené podle Event time)

  - Unpaid Toll Transaction.transaction amount

  - Unpaid Toll Transaction.toll trip 🡪 VTP.Toll trip (entry -- exit)

  - Unpaid Toll Transaction.toll trip 🡪 Pictures (možnost zobrazit a stáhnout fotky)

- Legal penalty s detaily:

  - Bill item.billing service name

  - Bill item.price amount VAT

Aktér vybere jednu nebo více položek v detailu souhrnné položky. Systém s každou vybranou položkou zobrazuje celkový součet k zaplacení (tj. SUM(Bill.total amount -- Bill.matched amount)).

Aktér potvrdí, že je chce uhradit.

(N1) Zaplať přestupek online

> Zaplatit půjde i souhrnná položka, jejíž položky patří jednomu, více nebo žádnému Accountu nebo výběr RfP, patří jednomu, více nebo žádnému Accountu:

- Pokud přihlášení proběhlo vytvořením nového anonymního zákazníka, pro identifikaci subjektu platby se použije jeho nový Account.

- Pokud je známa Registrační značka vozidla a zákazník, jako subject platby se použije subjekt nejnovějšího vybraného RfP dané Registrační značky daného zákazníka.

- Pokud se přihlásil stávajicí zákazník nebo je znám jen Customer ze vstupu, pro identifikaci subjektu platby se použije subjekt nejnovějšího vybraného RfP daného zákazníka.

- Pokud je znám jen Account ze vstupu, použije se jako subjekt platby.

- Pokud je známa jen Registrační značka vozidla, jako subject platby se použije subjekt nejnovějšího vybraného RfP dané Registrační značky.

> Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové

funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

Společný postup pro všechny platební metody

Systém:

- na základě každé zaplacené Unpaid Toll Transaction vytvoří odpovídající Toll Transaction ve stavu Processed, kdy se zkopírují hodnoty odpovídajících atributů z Unpaid Toll Transaction,

- převěsí na Toll Transaction odpovídající Rated Toll Events,

- updatuje atributy Toll Transaction:

  - Unpaid Toll Transaction creation time = z Unpaid Toll Transaction.creation time

  - [Payment = referenci na realizovanou platbu]{.mark}

- zruší Unapid Toll Transaction.

Systém vygeneruje jednorázovou fakturu za mýto za užití systémové funkce Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR).

Systém napáruje nově vytvořenou fakturu s platbou, tj. vytvoří pro ně Matching s následujícími parametry:

- Date of matching = Datum a čas, kdy bylo párování provedeno

- Effective date of matching = vyšší datum z datumů obou párovaných stran (tj. bill.date of end a payment.date of collection)

- Bill -- debit matching side = Bill

- Payment -- credit matching side = Payment

- Matched amount = částka platby = částka faktury

- Matching method = Automatic

- Disconnect allowed = False

- BO Operátor = System

Systém na základě provedého párování updatuje atributy napárovaného Bill:

- Matched amount = částka zaplaceného top-up (tj. Bill.total amount),

- Bill payment status = Paid fully.

Systém na základě provedého párování updatuje atributy napárovaného Payment:

- Matched amount = částka zaplaceného top-up (tj. Payment amount),

- Matching status = Recognized -- matched.

Systém, pro každé zaplacené Offence RfP, které je po splatnosti, informuje Dunning, zavoláním případu užití Aktualizuj dluh (SYS.DU.1.2.HR) s uvedením Effective date of matching provedeného párování.

Systém na základě zaplacených Přestupků updatuje záznam Alert listu: U existujícího záznamu Alert listu pro dané SPZ sníží částku Total due amount o celkovou zaplacenou částku za mýto (tj. o částku bez administrativních poplatků) a sníží Offence count o počet vyřešených mýtných transakcí, za použití systémové funkce Zaeviduj Offence na Alert list (SYS.TDP.5.6):

- UTT.Registration number a UTT.Registration country

- Bill.Bill issuer

- -1 \* Suma Bill item.price amount VAT s Bill item category = Toll event (= suma Toll transaction.transaction amount VAT, u kterých se měnil stav na Processed)

- -1 \* Suma Bill item.number of units s Bill item category = Toll event (= počet Toll transaction, u kterých se měnil stav na Processed)

Systém nabídne na stažení vygenerovanou fakturu.

Aktér Fakturu může stáhnout.

Systém přegeneruje hlavní přehled zbývajících Přestupků a Výzev na zaplacení per Bill issued a zobrazí je Aktérovi.

Aktér může provést nový výběr a pokračovat platbou, nebo proces ukončit.

Pokud již neexistuje ani jeden Přestupek nebo Výzva na úhradu, Systém zobrazí informaci, že pro dané vozidlo již neeviduje žádný přestupek.

> Postup končí.

1.  

Alternativní postupy(A0) Přestupek neexistuje

> Pokud pro SPZ nebo pro všechny SPZ přihlášeného zákazníka neexistuje ani jedna Výzva na úhradu, Systém zobrazí informaci, že momentálně neeviduje žádný přestupek.

(A1) Zaplať přestupek na POS, Kiosku nebo MEV

Aktér potvrdí částku na zaplacení a postup pokračuje realizací platby za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(A2) Zaplať přestupek na Web Portal nebo Mobile app - online platba přes platební bránu

Placení z Web portálu nebo Mobile App je popsáno v systémové funkci Zprocesuj transakci platební kartou (API.BAR.0.1.HR):

- Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence RfPs) na zaplacení, Bill issuer a Account.

- Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

- Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(A3) Zaplať přestupek na Web Portal nebo Mobile app -- jiná platební metoda než online platba přes platební bránu]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence RfPs), typu platební metody (např SMS, Voucher), Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).]{.mark}

[(A4) Zaplať přestupek na externí POS]{.mark}

[Systém na vstupu přes Rozhraní POS API (INT.BAR.34.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence RfPs), typu platební metody, Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(A5) Zaplať přestupek bankovním převodem na základě Offence RfP

Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši platby, typ platební metody (bank transfer), Offence RfP, Bill issuer.

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

1.  

Chybové postupyNeúspěšná transakce nebo zrušená transakce zákazníkem

> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected nebo Cancelled), Systém informuje Aktéra o neúspěšné transakci.
>
> Aktér může pokračovat úpravou počtu vybraných položek na zaplacení nebo proces ukončit.

2.  

> Grafické rozhraníFO: UI.BAR.[xxx]{.mark}

3.  

PoznámkyPo přihlášení do Offence portálu pomocí linku + PIN nebo registrační značkou + PIN, bude možné se dodatečně anonymně zaregistrovat za použití případu užití Zaregistruj vozidlo cez Offence Portal (UC.VCM.1.7.HR)

> Pokud placení přestupků proběhlo před registrací, subjekt faktury nebude vyplněn. Pokud registrace proběhla před placením přestupků, subjektem faktury bude nově vytvořený Account.

### Zaplať Produktový balíček (UC.BAR.0.21.HR)

#### Cíl

Cílem tohoto případu užití je zaplacení Produktového balíčku.

#### 

AktéřiPOS Operator, System, Customer

#### Spuštění případu

Případ užití je vloženou součástí případu užití:

- Pridaj produktový balíček (UC.VCM.1.6)

- 

Na základě požadavku na objednání Produktu z rozhraní:

- Rozhraní Web portal API (INT.BAR.33.HR)

- [Rozhraní HR Toll API (INT.BAR.34.HR)]{.mark}

- [Rozhraní ERP Navision (INT.BAR.30.HR)]{.mark}

- 

#### Podmínky spuštění

Customer je znám a není anonymní (tj. Anonymous registration = false).

Product Account nebo Account je znám.

Account není terminovaný.

Product package detail je znám.

Bill issuer je znám (tj. System operator).

Způsob platby je znám.

Případně POS je známa.

#### Normální postup

(N1) Zaplať produkt na vlastní POS, [externí POS]{.mark}

Systém zobrazí minimální výši top-up pro požadovaný Produktový balíček.

Aktér zvýší nebo potvrdí částku minimálního top-up.

Postup pokračuje realizací platby top-up za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(N2) Zaplať produkt na Web Portal nebo Mobile app - online platba přes platební bránu

Placení z Web portálu nebo Mobile App je popsáno v systémové funkci Zprocesuj transakci platební kartou (API.BAR.0.1.HR):

- Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o Product package, výši zadaného produktového top-up, Bill issuer a Account.

- Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

- Pokud transakce byla úspěšná (tj.Payment session.status = Realized), proces pokračuje Společným postupem.

- Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(N4) Zaplať produkt]{.mark} [na externí POS]{.mark}

[Systém na vstupu přes Rozhraní POS API (INT.BAR.34.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody, Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(N5) [Zaplať produkt]{.mark} bankovním převodem na základě Proforma faktury

[Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody (bank transfer), Proforma bill, Bill issuer.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

Společný postup pro všechny platební metody

Systém vytvoří nový Product account (pokud Account ze vstupu byl národní Account a daný Product account na zákazníkovi ještě neexistuje) nebo updatuje existující Product account (pokud Account na vstupu byl Product account) za použití případu užití (Pridaj produktový balíček (UC.VCM.1.6)).

Systém vytvoří Product balance, pokud ještě neexistuje pro daný Product Account, za použití systémové funkce Vytvoř zůstatky (SYS.BM.1.3.HR).

Systém o částku platby navýší zůstatek odpovídající Product balance, použije se případ užití Aktualizuj zůstatek (SYS.BM.1.2) s Product account number.

Systém zjistí údaje o Product package eventě na základě Bill issuer, Product type = Product package a Event attribute Product package = Product package ze vstupu, za použití případu užití Získej produkt (SYS.PCRE.1.2.HR).

Systém vygeneruje jednorázovou fakturu za služby za užití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

Systém napáruje nově vytvořený Bill na nově vytvořený Payment, tj. vytvoří Matching s následujícími parametry:

- Date of matching = aktuální datum

- Effective date of matching = vyšší z datumů párovaných stran (tj. payment.date of collection, bill.date od end)

- Bill -- debit matching side = vytvořený Bill

- Payment -- credit matching side = vytvořený Payment

- Matched amount = částka zaplaceného top-up

- Matching method = Automatic

- Disconnect allowed = True

Systém na základě provedého párování updatuje atributy napárovaného Bill:

- Matched amount = částka zaplaceného top-up (tj. Bill.total amount),

- Bill payment status = Paid fully.

Systém na základě provedého párování updatuje atributy napárovaného Payment:

- Matched amount = částka zaplaceného top-up (tj. Payment amount),

- Matching status = Recognized -- matched.

[Pokud šlo o platbu tankovací kartou, Systém zagreguje platbu do odpovídajícího FCI RfP, využitím případu užití Zagreguj platby tankovací kartou do FCI RfP (SYS.BAR.0.9).]{.mark}

Postup končí.

#### Alternativní postupy 

[(A1) Bez platby -- Proforma (na BO, vlastní POS, externí POS nebo MEV )]{.mark}

[Pokud Aktér bude chtít jako platební metodu bankovní převod, iniciuje vytvoření nabídky (tj. Proforma faktury (Offer)) zmáčknutím příslušného tlačítka a spuštěním případu užití Vytvoř proforma fakturu (UC.BAR.3.3.HR).]{.mark}

[Postup končí.]{.mark}

[(A2) Bez platby -- Proforma (Web portal nebo Mobile app)]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Produktového top-up, Product package, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem. Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR)]{.mark}

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

Postup končí.

#### Chybové postupy

Neúspěšná online transakce

> Pokud online transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém informuje Aktéra o neúspěšné transakci (pokud proces byl inicializován v rámci Systému) a Aktér může pokračovat od začátku úpravou výše Top-up nebo proces ukončit.
>
> Případně Systém vrátí odpovídající result externímu systému (pokud proces byl inicializován z externího systému).

#### Grafické rozhraní

N/A

#### Poznámky

Nejsou

### Zaplať OBU (UC.BAR.0.22.HR)

#### Cíl

Cílem tohoto případu užití je navýšení OBU balance před samotným výdejem OBU.

#### 

AktéřiPOS Operator, System, Customer

#### Spuštění případu

Případ užití je vloženou součástí případu užití:

- Objednaj OBU (UC.VCM.2.8) (jen Proforma)

- Vydaj OBU na POS (UC.VCM.2.9)

Na základě požadavku na Top-up z rozhraní:

- Rozhraní ERP Navision (INT.BAR.30.HR)

- Rozhraní Web portal API (INT.BAR.33.HR)

- [Rozhraní interní POS API (INT.BAR.34.HR)]{.mark}

- Rozhraní interní IEFBO API (INT.BAR.36.HR)

<!-- -->

- 

#### Podmínky spuštění

Account je znám.

[Account není terminovaný.]{.mark}

Počet požadovaných OBU je znám.

Cena za jednu OBU je známa.

Bill issuer je znám (tj. System operator).

Způsob platby je znám.

Případně POS je známa.

#### Normální postup

(N1) Zaplať OBU na vlastní POS, externí POS nebo MEV

Systém zobrazí aktuální výši OBU balance poplatnou Toll chargerovi dané POS.

Aktér vyplní požadovaný počet palubních jednotek.

Systém, na základě zadaného počtu OBE, aktuální výše OBU balance a ceny za OBU daného TC, spočítá minimální potřebnou částku k úhradě:

- Pokud částka OBU balance je dostatečná na požadovaný počet OBU, postup je ukončen.

- Jinak Systém zobrazí minimální částku k úhradě.

Aktér zvýší nebo potvrdí částku.

Postup pokračuje realizací platby OBU za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(N2) Zaplať OBU na Web Portal nebo Mobile app - online platba přes platební bránu

Placení z Web portálu nebo Mobile App je popsáno v systémové funkci Zprocesuj transakci platební kartou (API.BAR.0.1.HR):

- Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o počtu OBU, Bill issuer a Account.

- Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

- Pokud transakce byla úspěšná (tj.Payment session.status = Realized), proces pokračuje Společným postupem.

- Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(N4) Zaplať OBU přes HR Toll aplikaci]{.mark}

[Systém na vstupu přes Rozhraní HR Toll API (INT.BAR.34.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody, Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem.]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(N5) Zaplať OBU bankovním převodem na základě Proforma faktury

Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši platby za OBU, typ platební metody (bank transfer), Proforma bill, Bill issuer.

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

Proces pokračuje Společným postupem.

Společný postup pro všechny platební metody

Systém o částku platby navýší zůstatek OBU balance daného Toll chargera.

[Pokud šlo o platbu tankovací kartou, Systém zagreguje platbu do odpovídajícího FCI RfP, využitím případu užití Zagreguj platby tankovací kartou do FCI RfP (SYS.BAR.0.9).]{.mark}

Postup končí.

#### Alternativní postupy 

(A1) Bez platby -- Proforma (na BO, vlastní POS, externí POS nebo MEV )

Pokud Aktér bude chtít jako platební metodu bankovní převod, iniciuje vytvoření nabídky (tj. Proforma faktury (Offer)) zmáčknutím příslušného tlačítka a spuštěním případu užití Vytvoř proforma fakturu (UC.BAR.3.3.HR).

Postup končí.

(A2) Bez platby -- Proforma (Web portal nebo Mobile app)

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o počtu požadovaných OBU, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem.

Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR). Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR):

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

Postup končí.

#### Chybové postupy

Neúspěšná transakce

> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém informuje Aktéra o neúspěšné transakci (pokud proces byl inicializován v rámci Systému) a Aktér může pokračovat od začátku úpravou počtu OBU nebo proces ukončit.

Neúspěšná online transakce

> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém vrátí odpovídající result externímu systému (pokud proces byl inicializován z externího systému).

#### Grafické rozhraní

N/A

#### Poznámky

Nejsou

## Operace s fakturami

### Vytvoř proforma fakturu (UC.BAR.3.3.HR)

#### Cíl

Cílem tohoto případu použití je vytvořit proforma fakturu pro prodej Top-up, OBU nebo Produktového balíčku. Jde o vystavení nabídky, kterou bude moci zákazník uhradit bankovním převodem.

#### 

AktéřiPOS Operator, BO Operator, System, Customer

#### Spuštění případu

Případ užití je vloženou součástí případu užití:

- Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

  - na BO, POS, [externí POS]{.mark} nebo MEV

- Zaplať OBU (UC.BAR.0.22.HR), Objednaj OBU (UC.VCM.2.8)

  - na BO, POS, [externí POS]{.mark} nebo MEV

- Zaplať Produktový balíček (UC.BAR.0.21.HR), Pridaj produktový balíček (UC.VCM.1.6)

  - [na BO, POS, externí POS,\
    ]{.mark}

Na základě požadavku na Proforma fakturu z rozhraní:

- Rozhraní Web portal API (INT.BAR.33.HR) - Vygeneruj proforma fakturu (API.BAR.1.1.HR)

- Rozhraní interní IEFBO API (INT.BAR.36.HR)

#### Podmínky spuštění

Account je znám.

[Account není terminovaný.]{.mark}

Pro spuštění UC z rozhraní: Je známa částka k úhradě, typ operace (OBU, Top-up, Product package), případně počet OBU, případně identifiace Product package.

Bill issuer je znám (tj. System operator).

Případně POS je známa.

#### Normální postup

[(N1) Proforma na Top-up na BO, vlastní POS, [externí POS]{.mark} nebo MEV]{.underline}

Systém zobrazí **aktuální výši balance** (BM.Balance.amount - BM.Balance.Reservation amount - Grace period amount).

Systém zobrazí minimální zaokrouhlenou výši kreditu k zaplacení:

- Pokud **aktuální výše balance** \< 0, pak MAX (absolutní hodnota aktuální výše balance; BAR.Currency.Minimum top-up amount),

- jinak BAR.Currency.Minimum top-up amount.

Aktér zvýší nebo potvrdí částku minimálního top-up.

Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

[(N2) Proforma na Produktový nbalíček na BO, vlastní POS, externí POS nebo MEV]{.mark}

[Systém zobrazí minimální výši top-up daného Produktového balíčku.]{.mark}

[Aktér zvýší nebo potvrdí částku.]{.mark}

[Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).]{.mark}

(N3) Proforma na OBU na BO, vlastní POS, externí POS nebo MEV

Systém zobrazí aktuální výši OBU balance poplatnou Toll chargerovi dané POS.

Aktér vyplní požadovaný počet palubních jednotek.

Systém, na základě zadaného počtu OBE, aktuální výše OBU balance a ceny za OBU daného TC, spočítá potřebnou minimální částku k úhradě:

- Pokud částka OBU balance je dostatečná na požadovaný počet OBU, postup je ukončen.

- Jinak Systém zobrazí minimální částku k úhradě.

Aktér zvýší nebo potvrdí částku.

Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

Postup končí.

#### Alternativní postupy 

[(A1) Proforma na Top-up (Web portal nebo Mobile app)]{.underline}

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Top-up, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem. Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR):

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[[(A2) Proforma na Produktový balíček (Web portal nebo Mobile app)]{.underline}]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Produktového top-up, Product package, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem. Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR):]{.mark}

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

(A3) Proforma na OBU (Web portal nebo Mobile app)

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o počtu požadovaných OBU, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem. Operace je realizována za použití systémové funkce Vygeneruj proforma fakturu (API.BAR.1.1.HR):

- Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

- Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

#### Chybové postupy

> Nejsou

#### Grafické rozhraní

[TBD]{.mark}

#### Poznámky

Nejsou

### Vytvoř korekci ([UC.BAR.3.X.HR]{.mark})

#### Cíl

Cílem tohoto případu použití je vytvořit manuální kreditní korekci faktury za služby, či smluvní pokuty. Včetně tohoto případu užití je i vrácení OBU jednotky do 15 dní a příslušenství k OBU.

#### 

AktéřiBO Operator

#### Spuštění případu

Tlačítkem z BAR BO v případě korekce služby.

V případě vrácení OBU či OBU příslušenství, příjmem zboží a kontrolou, do 15 dní na POS, či zaslání poštou.

#### Podmínky spuštění

Existuje faktura za služby, nebo smluvní pokuty (tj. Faktura má kategorii Services nebo [Penalty]{.mark}, Offence (RSE), OBU accesories), která není korigována (nemusí být Issued)

Účet není Terminated

Faktura má issue type: Regular bill

Faktura nebyla plně korigována (tj. Existuje na faktuře alespoň jeden RSE, který je Cancellable = true a Number of units corrected \< Number of units).

#### Normální postup

V případě manuální korekce v BAR BO:

Aktér vyhledá fakturu, která má být korigována a iniciuje vytvoření kreditní korekce (tlačítkem na BO).

Systém zobrazí přehled všech Bill item (agregovaných), jehož RSE se dají zrušit (Tj. RSE. Cancellable = true), a pro každou z nich zobrazí celkový počet jednotek, počet jednotek, které lze korigovat (suma Number of units agregovaných RSE - suma Number of units corrected agregovaných RSE), jednotkovou cenu a její měnu. Zároveň zobrazí ty, které již jsou korigovány (jsou zašedlé).

#### Alternativní postupy 

[Korekce celé faktury]{.underline}

#### Chybové postupy

#### Grafické rozhraní

#### Poznámky