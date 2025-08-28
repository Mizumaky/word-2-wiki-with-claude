# Příloha C -- Konfigurovatelnost modulu

## Naplánované operace

| **Název naplánované operace CZ**                                    | **Název naplánované operace EN** | **Časový plán Parametry**          | **Use case**                                                | **Popis operace**`<br>`{=html}**Specifikace výsledku naplánované operace**                                                               |
|---------------------------------------------------------------------|----------------------------------|------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Uzavření fakturačních dávek -- 1x denně                             | BEm.CloseBillSessionsBySystem    | Denní spouštění v 1:00 am          | SYS.BAR.0.1`<br>`{=html}SYS.BAR.0.2`<br>`{=html}SYS.BAR.0.3 | Automatická uzávěrka fakturačních dávek sloužící k vygenerování pravidelných faktur a výzev k úhradě                                     |
| Vytvoření fakturačních dávek -- 1x denně                            | BEm.CreateBillSessions           | [Denní spouštění]{.mark}           |                                                             | Automatické vytvoření fakturačních dávek                                                                                                 |
| Zúčtování závazků a pohledávek účtů čekající na uzavření - 1x denně | BEm_ProcessSettlement            | [Denní spouštění v 5:00 am]{.mark} | SYS.BAR.2.3                                                 | Automatické zúčtování závazků a pohledávek účtů čekajících na uzavření a jejich následná terminace                                       |
| Exportování Billing details EETS Providers -- 1x denně              | BEm.ExportBillingDetailsHr       | [Denní spouštění]{.mark}           | SYS.BAR.1.9.HR                                              | Automatické vytvoření Billing details pro TSP jednou denně                                                                               |
| Zaplacení mýtné transakce tokenem platební karty                    | BEm.ExecuteTokenPaymentPolling   |                                    | SYS.BAR.1.10.HR                                             | Automatické dohledávání nezaplacených mýtných transakcí a jejich úhrada za pomocí uloženého tokenu platební karty                        |
| Vytvoření přestupku                                                 | BEm.Offence                      | Denní spouštění                    | SYS.BAR.1.11.HR                                             | Automatické dohledávání nezaplacených mýtných transakcí ve stavu starších než určitá doba a vystavení na jejich základě Výzvy na úhradu. |
| Vytvoření výzev za úhradu za přestupky                              | BEm.GenerateOffenceRfP           | Denní spouštění                    | SYS.BAR.0.13.HR                                             | Automatické dohledávání nezaplacených mýtných transakcí starších než určitá doba a vystavení na jejich základě Výzvy na úhradu.          |
|                                                                     |                                  |                                    |                                                             |                                                                                                                                          |

: Tabulka : Naplánované operace

## [Konfigurační klíče]{.mark}

| **Název konfiguračního klíče EN (CZ)**                                    | **Výchozí hodnota klíče** | **Datový typ**  | **Popis**                                                                                                                                                                                              |
|---------------------------------------------------------------------------|---------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BE.PaymentReversalTimeout (Timeout pro zrušení platby)                    | 15                        | Number          | Časový limit pro automatický reverzal nedokončené transakce platební kartou (v minutách)                                                                                                               |
| BE_DaysPriorSettlement (Počet dní před zúčtováním)                        | 20                        | Number          | Počet kalendářních dní po přepnutí účtu do Pending termination, po jejichž uplynutí Systém vyhodnocuje podmínky ke spuštění zúčtování závazků a pohledávek                                             |
| BE_DaysAfterBillSession (Počet dní po zúčtováním)                         | 0                         | Number          | Počet kalendářních dní po konci poslední bill session která nastala po uplynutí BE_DaysPriorSettlement (Počet dní před zúčtováním), po jejichž uplynutí se může spustit zúčtování závazků a pohledávek |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
| BE_AggregateZeroTollTransactions                                          | No                        | Boolean         | Tato konfigurace umožňuje nastavit, zda mají být nulové mýtné události shrnuty do fakturačních položek nebo nikoliv.                                                                                   |
| BE_AggregateZeroServiceTransactions (Zahrnovat nulové poplatky za služby) | No                        | Boolean         | Tato konfigurace umožňuje nastavit, zda mají být nulové transakce za služby shrnuty do fakturačních položek nebo nikoliv.                                                                              |
| [BE_VariableSymbolTopUp]{.mark}                                           | [2]{.mark}                | [Number]{.mark} | [Hodnota Variabilního symbolu pro platbu dobití kreditu placenou bankovním převodem.]{.mark}                                                                                                           |
| BE_DaysInGracePeriodPriorOffenceCreation                                  | 5                         | Number          | Počet pracovních dní od vzniku Unpaid Toll Transactions ve stavu Grace period, po uplynutí kterých se přenastaví do stavu Offence.                                                                     |
| BE_DaysPriorOffencesRfPCreation                                           | 5                         | Number          | Počet kalendářních dní od přepnutí Unpaid Toll Transactions do stavu Offence, po uplynutí kterých se zařadí do RfP.                                                                                    |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
| BE_MaturityPeriodForCreditNote                                            | 30                        | Number          | Počet kalendářních dní použitých pro výpočet Due date zákaznického dobropisu                                                                                                                           |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
|                                                                           |                           |                 |                                                                                                                                                                                                        |
|                                                                           |                           |                 |                                                                                                                                                                                                        |

: Tabulka : Konfigurační klíče

## Číselníky a systémová nastavení

Součástí přehledu jsou i systémová nastavení (nekonfigurovatelné systémové číselníky).

### Payment Type (Typ platby)

|     |     |     |     |
|-----|-----|-----|-----|

| **Název konfigurovatelného číselníku EN (CZ)** | **Typ číselníku (jeden/více atributů)** | **Omezení konfigurovatelnosti**     | **Poznámka k číselníku**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------|-----------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Payment type                                   | Více atributů                           | omezená konfigurovatelnost (Create) | Bill payment`<br>`{=html}EETS Provider bill payment`<br>`{=html}Credit note refund`<br>`{=html}Payment cancel`<br>`{=html}[Payment refund]{.mark}`<br>`{=html}Top-up payment`<br>`{=html}Top-up refund`<br>`{=html}Top-up cancel`<br>`{=html}[Unknown credit]{.mark}`<br>`{=html}[Unknow debit]{.mark}`<br>`{=html}[Negative cent adjustment]{.mark}`<br>`{=html}[Positive cent adjustment]{.mark}`<br>`{=html}[Compensation]{.mark}`<br>`{=html}[Compensation cancel]{.mark}`<br>`{=html}[Other]{.mark}`<br>`{=html}[Other cancel]{.mark}`<br>`{=html}[Collateral guarantee payment]{.mark}`<br>`{=html}[Collateral guarantee refund]{.mark}`<br>`{=html}[Collateral guarantee cancel]{.mark}`<br>`{=html}Tokenization reservation`<br>`{=html}Tokenizationr reservation cancel`<br>`{=html}Toll payment |

### Rounding (Zaokrouhlování)

| **Name**        | **Mode**   | **Decimal places** | **Currency** |
|-----------------|------------|--------------------|--------------|
| BillDown        | BillDown   | 2                  |              |
| BillUp          | BillUp     | 2                  |              |
| BillRoundingEur | BillMath   | 2                  | EUR          |
| PosRoundingEur  | Aritmetic5 | 2                  | EUR          |

|     | BillUp     | 0   | EUR |
|-----|------------|-----|-----|
|     | Arithmetic | 2   |     |

### CorvusPay Payment Method (CorvusPay platební metoda)

| **Abbreviation** | **Description**                                                                            | **Is read only** | **Currency** |
|------------------|--------------------------------------------------------------------------------------------|------------------|--------------|
| [CARD]{.mark}    | Card payment -- buyers must enter credit card details on each purchase                     | yes              | [EUR]{.mark} |
| [IBAN]{.mark}    | Pay by IBAN -- buyer can enter IBAN to make purchase                                       |                  | [EUR]{.mark} |
| [WALLET]{.mark}  | Quick wallet payment -- buyers have option to save card and IBAN data for faster checkout  |                  | [EUR]{.mark} |
| [GIFT]{.mark}    | paysafecard -- gift card (vaucher) payments, no bank account or credit card required       |                  | [EUR]{.mark} |
| [GOOGLE]{.mark}  | Google Pay - Enables buyers to make quick and secure payments using their Android devices. |                  | [EUR]{.mark} |
| [APPLE]{.mark}   | Apple Pay - Enables buyers to make quick and secure payments using their Apple devices.    |                  | [EUR]{.mark} |
|                  |                                                                                            |                  |              |
|                  |                                                                                            |                  |              |

|     |     |     |     |
|-----|-----|-----|-----|
|     |     |     |     |

### CorvusPay Response Code (CorvusPay kód odpovědi)

Viz přiložený excel CorvusPay kódů odpovědí a požadované reakce Systému:

||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||
||

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |