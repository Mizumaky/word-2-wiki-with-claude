# Případy užití

Sloupec **Realizace** určuje způsob implementace příslušného UC:

- New -- nový UC jen pro daný projekt

- Upd -- UC upravený (customizovaný) pro daný projekt

- AsIs -- UC beze změny

- N/A -- nebude používán

| **Funkční oblast**             | **Případ užití**                                                       | **BO**       | **FO**     | **SC**     | **Realizace** | **Aktér**                              |
|--------------------------------|------------------------------------------------------------------------|--------------|------------|------------|---------------|----------------------------------------|
| Operace s platbami             | Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1)    | *X*          | *X*        | *X*        | *N/A*         | *SC User, POS operator*                |
|                                | Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR) | *X*          | *X*        | *X*        | *Upd*         | *SC User, POS operator, System*        |
|                                | Zaplať depozit (UC.BAR.0.2)                                            | *X*          | *X*        | *X*        | *N/A*         | *BO operator, SC User,* *POS operator* |
|                                | Uhraď poplatek na FO (UC.BAR.0.3)                                      |              | *X*        |            | *N/A*         | *POS operator*                         |
|                                | Zaplať poplatek na FO (UC.BAR.0.3.HR)                                  |              | *X*        |            | *Upd*         | *POS operator*                         |
|                                | Vrať depozit (UC.BAR.0.4.VO1)                                          | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Zaplať předplacený kredit -- Pre-paid (UC.BAR.0.5)                     | *X*          | *X*        | *X*        | *N/A*         | *SC User, POS operator*                |
|                                | Storno platby (UC.BAR.0.6)                                             | *X*          | *X*        |            |               | *BO operator, POS operator*            |
|                                | Načti bankovní výpis (UC.BAR.0.7.VO1)                                  | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Rozpoznej položku bankovního výpisu (UC.BAR.0.8.VO1)                   | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Zruš rozpoznání platby (UC.BAR.0.9.VO1)                                | *X*          |            |            |               | *BO operator*                          |
|                                | Napáruj fakturu na platbu (UC.BAR.0.10.VO1)                            | *X*          |            |            |               | *BO operator*                          |
|                                | Napáruj platbu na fakturu (UC.BAR.0.11.VO1)                            | *X*          |            |            |               | *BO operator*                          |
|                                | Odpáruj platbu (UC.BAR.0.12.VO1)                                       | *X*          |            |            |               | *BO operator*                          |
|                                | Napáruj fakturu na fakturu (UC.BAR.0.13.VO1)                           | *X*          |            |            |               | *BO operator*                          |
|                                | Odpáruj fakturu z faktury (UC.BAR.0.14.VO1)                            | *X*          |            |            |               | *BO operator*                          |
|                                | Vrať platbu (UC.BAR.0.15.VO1)                                          | *X*          |            |            |               | *BO operator*                          |
|                                | Schval položku platebního příkazu (UC.BAR.0.16.VO1)                    | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Změň položku platebního příkazu (UC.BAR.0.17.VO1)                      | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Zamítni položku platebního příkazu (UC.BAR.0.18.VO1)                   | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Vytvoř soubor platebních příkazů (UC.BAR.0.19.VO1)                     | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Uhraď přestupek (UC.BAR.0.20.HR)                                       | *[X]{.mark}* | [X]{.mark} | [X]{.mark} | *New*         | *BO Operator*                          |
| Pomocné operace                | Načti soubor mýtných segmentů (UC.BAR.1.1)                             | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                |                                                                        |              |            |            |               |                                        |
| Operace na vyžádání zákazníkem | Vytvoř detailní výpis mýtných transakcí na vyžádání (UC.BAR.2.1.VO1)   |              |            | *X*        |               | *WSC User*                             |
| Operace s fakturami            | Vytvoř korekci (UC.BAR.3.1.VO1)                                        | *X*          |            |            |               | *BO operator*                          |
|                                | Uhraď dobropis (UC.BAR.3.2.VO1)                                        | *X*          |            |            |               | *BO operator*                          |
| Správa slev                    | Odešli oznámení o novém nároku na slevu v doméně CZ (UC.BAR.4.1)       | *X*          |            |            | *N/A*         | *BO operator*                          |
|                                | Potvrď nárok na slevu v doméně CZ (UC.BAR.4.2)                         |              |            |            | *N/A*         | *BO operator*                          |

: Tabulka : Seznam případů užití

## Operace s platbami

### Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

#### Cíl

Cílem tohoto případu užití je navýšení předplaceného kreditu Pre-paid účtu.

#### Aktéři

POS Operator, System, Customer

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
- 
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

Systém zobrazí aktuální výši balance (BM.Balance.amount - BM.Balance.Reservation amount - [Grace]{.mark} [period]{.mark} [amount]{.mark}).

Systém zobrazí minimální zaokrouhlenou výši kreditu:

- Pokud aktuální balance \< 0, pak MAX (absolutní hodnota aktuální výše balance; BAR.Currency.Minimum top-up amount),

- jinak BAR.Currency.Minimum top-up amount.

Aktér vybere částku z předdefinovaných hodnot (tj. Currency.GUI top-up value 1-4) nebo Aktér zvýší nebo potvrdí částku minimálního top-up.

Systém zkontroluje, zda částka je \<= hodnotě Currency.Max Top-up, pokud není, Aktér je vyzván k úpravě částky top-up.

Pokud zadaná částka kreditu (zaokrouhlená na celé číslo), je vyšší než hodnota Currency.MaxTop-upCash, Systém neumožní vybrat platbu v hotovosti.

Postup pokračuje realizací platby top-up za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(N2) Předplať kredit na Web Portal nebo Mobile app - online platba přes platební bránu

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši zadaného Top-up, Bill issuer a Account.

Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

Pokud transakce byla úspěšná (tj.Payment session.status = Realized), proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.

Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

(N3) Předplať kredit na Web Portal nebo Mobile app -- jiná platební metoda než online platba přes platební bránu

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši zaplaceného Top-up, typu platební metody (např SMS, Voucher), Bill issuer a Account.

Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).

Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.

Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(N4)]{.mark} [Předplať kredit]{.mark} [na externí POS]{.mark}

[Systém na vstupu přes]{.mark} [Rozhraní POS API (INT.BAR.34.HR)]{.mark} [obdrží informaci o výši zaplaceného Top-up,]{.mark} [typ platební metody,]{.mark} [Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(N5) Předplať kredit bankovním převodem na základě Proforma faktury

Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši zaplaceného Top-up, typ platební metody (bank transfer), Proforma bill, Bill issuer.

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

Proces pokračuje Společným postupem a to krokem, kdy Systém navýší zůstatek předplaceného kreditu.

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

(A1) Bez platby -- Proforma (Web portal nebo Mobile app)

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Top-up, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem.

Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(A2) Bez platby]{.mark} [-- Proforma]{.mark} [(externí POS)]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o výši požadovaného Top-up, Bill issuer a Account, tzn. že zákazník má zájem o vytvoření nabídky (tj. Proforma faktury (Offer)), kterou chce zaplatit bankovním převodem.]{.mark}

[Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).]{.mark}

[Systém vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).]{.mark}

(A3) Bez platby -- Proforma (na POS)

Je řešeno v rámci alternativy (A1) Bez platby -- Proforma (na POS) v případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

#### Chybové postupy

Neúspěšná online transakce

> Pokud online transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém informuje Aktéra o neúspěšné transakci (pokud proces byl inicializován v rámci Systému) a Aktér může pokračovat od začátku úpravou výše Top-up nebo proces ukončit.
>
> Případně Systém vrátí odpovídající result externímu systému (pokud proces byl inicializován z externího systému).

#### Grafické rozhraní

N/A

#### Poznámky

Nejsou

### Zaplať poplatek na POS (UC.BAR.0.3.HR)

#### Cíl

Cílem tohoto případu užití je zaplacení poplatku při vystavení jednorázové faktury na vlastní POS.

#### Aktéři

POS Operator, Customer

#### Spuštění případu

Je vloženou součástí případu užití:

- Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

  - na POS, externí POS, Kiosku nebo MEV

- Uhraď přestupek (UC.BAR.0.20.HR)

  - na POS, externí POS, Kiosku nebo MEV

- 

- [VCM prodej OBU]{.mark}

- [VCM prodej produktu]{.mark}

- [VCM poslani OBU]{.mark}

- 

#### Podmínky spuštění

Kanál prodeje je vlastní nebo externí POS (je známa POS a Bill issuer).

Je známa částka k úhradě a buď oceněná událost a typ operace (top-up, placení offence, prodej OBU, prodej produktu, obejdnání OBU, objednání produktu\...).

[Account není terminovaný.]{.mark}

#### Normální postup

Systém zobrazí částku na zaplacení s přesností na dvě desetinná místa.

Aktér vybere platební metodu:

- Na vlastní a externí POS jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (NexGo (INT.BAR.28.HR))

  - hotovost

  - bankovním převodem (vystaví se jen Offer s platebními údaji).

- Na KIOSKU jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (Ingenico (rozhraní INT.BAR.29.HR))

- Na MEV jsou dostupné:

  - platba bankovní a palivovou kartou přes EFT (NexGo (INT.BAR.28.HR))

  - hotovost

  - Poznámka: platba bankovní a palivovou kartou přes EFT (NexGo (INT.BAR.28.HR)) je řešena v rámci systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR)

Poznámka: Pokud zákazník chce platit bankovním převodem, tj. vytisknout jen nabídku s platebními údaji, pokračuje se alternativou (A1) Bez platby -- Proforma (na POS).

(N1) Bank card nebo Fleet card payment přes terminál na POS nebo MEV

Aktér vloží kartu do EFT terminálu přes Rozhraní EFT Terminal NexGo (INT.BAR.28.HR).

EFT terminal rozpozná platbu bankovní/tankovací kartou.

EFT terminal autorizuje platbu pomocí karetního autorizačního centra. V případě, že EFT terminal zamítne autorizaci, Systém zobrazí informaci, že "Platba nebyla autorizována" a postup pokračuje opětovnou volbou platební metody.

Systém získá data o platbě z EFT terminálu z Rozhraní EFT Terminal NexGo (rozhraní INT.BAR.28.HR).

Systém vytvoří Payment Session:

- Online payment identifier = číslo transakce z EFT

- Payment session type =

  - Top-up, pokud Product type = Top-up

  - Offence, pokud jde o placení přestupků (placení UTT ve stavu Offence),

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

(N2) Bank card nebo Fleet card payment přes terminál na KIOSKu

Aktér vloží kartu do EFT terminálu přes Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR).

EFT terminal rozpozná platbu bankovní/tankovací kartou.

EFT terminal autorizuje platbu pomocí karetního autorizačního centra. V případě, že EFT terminal zamítne autorizaci, Systém zobrazí informaci, že "Platba nebyla autorizována" a postup pokračuje opětovnou volbou platební metody.

Systém získá data o platbě z EFT terminálu z Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR).

Systém vytvoří Payment Session:

- Online payment identifier = číslo transakce z EFT

- Payment session type =

  - Top-up, pokud Product type = Top-up

  - Offence, pokud jde o placení přestupků (placení UTT ve stavu Offence),

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

[Systém potřebnou částku za poplatek placenou hotovostí]{.mark} [zaokrouhlí]{.mark} [na nejbližší pěticent (tj. 102,02 🡪 102,00; 102,03 🡪 102,05; 102,26 🡪 102,25; 99,97 🡪 99,95; 99,98 🡪 100,00).]{.mark}

Aktér převezme zaokrouhlenou částku v hotovosti od zákazníka a zaregistruje Platbu.

Společný postup pro všechny platební metody

[Systém zjistí BIBA pro fakturaci na základě Bill issuer ze vstupu a Reason:]{.mark}

- [Offence, pokud jde o]{.mark} [Offence operaci]{.mark}

- [Top-up, pokud jde o Top-up operaci]{.mark}

- [jinak Services.]{.mark}

Systém vytvoří Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type =

  - Top-up payment, pokud jde o Top-up

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

#### Alternativní postupy

(A1) Bez platby -- Proforma (na POS)

Aktér vybere platební metodu bankovní převod, tzn. vytvoření nabídky (tj. Proforma faktury (Offer)).

Systém vygeneruje Proforma fakturu za použití systémové funkce Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR).

Postup končí.

#### Chybové postupy

Nejsou

#### Grafické rozhraní

POS:

### Uhraď přestupek (UC.BAR.0.20.HR)

1.  Cíl

> Cílem tohoto případu užití je uhradit jeden nebo více přestupků nebo jednu nebo více Výzev na úhradu (Offence RfP), ve kterých jsou zahrnuty starší přestupky společně s případnými administrativními poplatky.

2.  Aktéři

> Offence Portal User, POS Operator, Customer, System

3.  Spuštění případu

Offence portal:

- Otevření stránky Offence portálu, a zadání Registrační značky vozidla a PIN, který byl vygenerován pro danou registrační značku a který provozovatel vozidla obdržel v dopise po vygenerování Výzvy na úhradu daného vozidla.

- Otevření linku a zadáním PIN, který provozovatel vozidla obdržel v dopise po vygenerování Výzvy na úhradu daného vozidla. (Poznámka: Link obsahuje jak registrační značku tak zemi registrace, takže není potřeba je již vyplňovat. Musí se zadat jen PIN vygenerovaný pro danou SPZ).

POS, MEV, KIOSK:

- Zadáním Registrační značky vozidla, pro které se mají najít Přestupky.

- Případně zadáním Accountu, pro který se mají najít přestupky.

Na základě požadavku na zaplacení Přestupku z rozhraní:

- Rozhraní ERP Navision (INT.BAR.30.HR)

- Rozhraní Web portal API (INT.BAR.33.HR)

- Rozhraní POS API (INT.BAR.34.HR)

- Rozhraní KIOSK API (INT.BAR.35.HR)

- Rozhraní IEFBO API (INT.BAR.36.HR)

  1.  Podmínky spuštění

> Je známo vozidlo, na kterém se mají uhradit Přestupky.

2.  Normální postup

> Systém, pro dané vozidlo ze vstupu, vyhledá:

- Přestupky (tj. Unpaid Toll Transaction s Unpaid toll transaction status = Offence) a

- Výzvy na úhrady za přestupky (tj. Bill s Bill type = Request for payment a Bill issue type = Regular bill a Bill category = Offence a Bill payment status = Unpaid nebo Paid Partially a kde zároveň je Matched Amount \< Total amount).

> Systém zobrazí úvodní přehled obsahující maximálně 6 položek. Každá položka bude součtem nalezených Přestupků per Bill issuer nebo Výzev na úhradu per Bill issuer.
>
> Z úvodního přehledu Aktér může každou jednotlivou souhrnnou položku zaplatit nebo zobrazit si její detail.
>
> Zaplatit půjde jen souhrnná položka, jejíž položky patří jednomu nebo žádnému Accountu.
>
> Pokud aktér vybral zaplacení konkrétní souhrnné položky, postup pokračuje (N1) Zaplať přestupek online.
>
> Pokud Aktér vybere zobrazení detailu, Systém zobrazí položky zahrnuté do dané vybrané souhrnné položky:

- aktuálně evidované Přestupky k danému vozidlu daného Bill issuera s možností ho vybrat pro zaplacení nebo zobrazit jeho detaily:

  - Unpaid Toll Transaction.Bill issuer

  - Account number

  - Unpaid Toll Transaction.Event time (by default seřazené podle Event time)

  - Unpaid Toll Transaction.Transaction amount

  - Unpaid Toll Transaction.Toll trip 🡪 VTP.Toll trip (entry -- exit)

  - 

  - Unpaid Toll Transaction.Toll trip 🡪 Pictures (možnost zobrazit [a stáhnout]{.mark} fotky)

- aktuálně evidované Výzvy na úhrady za přestupky k danému vozidlu daného Bill issuera s možností ji vybrat pro zaplacení nebo zobrazit její detaily:

  - Bill.Bill issuer

  - Account number

  - Bill.Bill issue date

  - Bill.Total amount -- Bill.Matched amount

  - Bill.Date of beginning -- Bill.Date of end

  - Přehled Unpaid Toll Transactions s detaily, jako u Offence (ale bez možnosti je vybírat)

  - Přehled administrativních poplatků (bez možnosti je vybírat):

    - Bill item.billing service name

    - Bill item.number of units

    - Bill item. Price amount VAT

Pokud Aktér vybere jednu nebo více položek v detailu souhrnné položky musí mít stejný nebo žádný Account. Systém s každou vybranou položkou zobrazuje celkový součet k zaplacení (tj. SUM (Unpaid Toll Transaction.Transaction amount VAT) nebo SUM (Bill.Total amount)).

Aktér potvrdí, že je chce uhradit.

(N1) Zaplať přestupek online

Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

Společný postup pro všechny platební metody

Systém:

- na základě každé zaplacené Unpaid Toll Transaction vytvoří odpovídající Toll Transaction ve stavu Processed, kdy se zkopírují hodnoty odpovídajících atributů z Unpaid Toll Transaction,

- převěsí na Toll Transaction odpovídající Rated Toll Events,

- updatuje atributy Toll Transaction:

  - Unpaid Toll Transaction creation time = z Unpaid Toll Transaction.creation time

  - Payment = referenci na realizovanou platbu

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

Systém na základě zaplacených Přestupků a zaplacených Offence RfPs per Bill issuer updatuje záznam Alert listu: U existujícího záznamu Alert listu pro dané SPZ sníží částku Total due amount o celkovou zaplacenou částku za mýto (tj. o částku bez administrativních poplatků) a sníží Offence count o počet vyřešených mýtných transakcí, za použití systémové funkce Zaeviduj Offence na Alert list (SYS.TDP.5.6):

- UTT.Registration number a UTT.Registration country

- Bill.Bill issuer

- -1 \* Suma Bill item.price amount VAT s Bill item category = Toll event (= suma Toll transaction.transaction amount VAT, u kterých se měnil stav na Processed)

- -1 \* Suma Bill item.number of units s Bill item category = Toll event (= počet Toll transaction, u kterých se měnil stav na Processed)

Systém nabídne na stažení vygenerovanou fakturu.

Aktér Fakturu může stáhnout.

Systém přegeneruje hlavní přehled zbývajících Přestupků a Výzev na zaplacení per Bill issued a zobrazí je Aktérovi.

Aktér může provést nový výběr a pokračovat platbou, nebo proces ukončit.

Pokud na vozidle již neexistuje ani jeden Přestupek nebo Výzva na úhradu, Systém zobrazí informaci, že pro dané vozidlo již neeviduje žádný přestupek.

> Postup končí.

1.  Alternativní postupy

(A0) Přestupek pro vozidlo neexistuje

> Pokud na vozidle neexistuje alepoň jeden Přestupek nebo alespoň jedna Výzva na úhradu, Systém zobrazí informaci, že pro dané vozidlo momentálně neeviduje žádný přestupek.

(A1) Zaplať přestupek na POS, Kiosku nebo MEV

Aktér potvrdí částku na zaplacení a postup pokračuje realizací platby za použití případu užití Zaplať poplatek na POS (UC.BAR.0.3.HR).

(A2) Zaplať přestupek na Web Portal nebo Mobile app - online platba přes platební bránu

Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence RfPs) na zaplacení, Bill issuer a Account.

Systém realizuje Online platbu přes CorvusPay platební bránu za použití systémové funkce Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR).

Systém, navíc oproti Společnému postupu, potvrdí externímu systému úspěšnou realizaci platby a vrátí identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).

[(A3) Zaplať přestupek na Web Portal nebo Mobile app -- jiná platební metoda než online platba přes platební bránu]{.mark}

[Systém na vstupu přes Rozhraní Web portal API (INT.BAR.33.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence]{.mark} [RfPs), typu platební metody (např SMS, Voucher), Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní Web portal API (INT.BAR.33.HR).]{.mark}

[(A4) Zaplať přestupek na externí POS]{.mark}

[Systém na vstupu přes Rozhraní POS API (INT.BAR.34.HR) obdrží informaci o vybraných přestupcích (UTTs nebo Offence]{.mark} [RfPs), typu platební metody, Bill issuer a Account.]{.mark}

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

[Systém, navíc oproti Společnému postupu, vrátí externímu systému identifikaci vytvořené faktury přes Rozhraní POS API (INT.BAR.34.HR).]{.mark}

(A5) Zaplať přestupek bankovním převodem na základě Offence RfP

Systém na vstupu přes Rozhraní ERP Navision (INT.BAR.30.HR) obdrží informaci o výši platby, typ platební metody (bank transfer), Offence RfP, Bill issuer.

[Systém vytvoří odpovídající realizovanou platbu za použití systémové funkce Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR).]{.mark}

2.  Chybové postupy

Neúspěšná transakce

> Pokud transakce nebyla úspěšná (tj.Payment session.status = Rejected), Systém informuje Aktéra o neúspěšné transakci.
>
> Aktér může pokračovat úpravou počtu vybraných položek na zaplacení nebo proces ukončit.

3.  Grafické rozhraní

> FO: UI.BAR.[xxx]{.mark}

4.  Poznámky

> Nejsou