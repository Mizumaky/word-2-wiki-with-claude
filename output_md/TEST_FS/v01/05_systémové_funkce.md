# Systémové funkce

Sloupec **Realizace** určuje způsob implementace příslušného UC:

- New -- nový UC jen pro daný projekt

- Upd -- UC upravený (customizovaný) pro daný projekt

- AsIs -- UC beze změny

- N/A -- nebude používán

| **Funkční oblast**           | **Případ užití**                                                           | **Realizace**  | **Aktér**       |
|------------------------------|----------------------------------------------------------------------------|----------------|-----------------|
| Fakturace                    | Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1)                           | *N/A*          | Systém          |
|                              | Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.VO1)                       | *N/A*          | Systém          |
|                              | Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.VO2)                       | *N/A*          | Systém          |
|                              | Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.HR)                        | *Upd*          | Systém          |
|                              | Vytvoř pravidelné faktury za služby (SYS.BAR.0.2)                          | *N/A*          | Systém          |
|                              | Vytvoř pravidelné výzvy na úhradu za platby tankovací kartou (SYS.BAR.0.3) | *N/A*          | Systém          |
|                              | Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.VO1)                    | *N/A*          | Systém          |
|                              | Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR)                     | *N/A*          | Systém          |
|                              | Naúčtuj transakční poplatek za mýtné (SYS.BAR.0.5)                         | *N/A*          | Systém          |
|                              | Vytvoř fakturační dávku (SYS.BAR.0.6)                                      | *N/A*          | Systém          |
|                              | Vytvoř fakturační dávku (SYS.BAR.0.6.VO1)                                  | *N/A*          | Systém          |
|                              | Vytvoř fakturační dávku (SYS.BAR.0.6.VO2)                                  | *N/A*          | Systém          |
|                              | Vytvoř fakturační dávku (SYS.BAR.0.6.HR)                                   | *Upd*          | Systém          |
|                              | Naúčtuj jednorázový poplatek (SYS.BAR.0.7)                                 | *N/A*          | Systém          |
|                              | Vytvoř jednorázový dobropis za služby (SYS.BAR.0.8)                        | *N/A*          | Systém          |
|                              | Vytvoř jednorázový dobropis za služby (SYS.BAR.0.8.VO1)                    | *N/A*          | Systém          |
|                              | Zagreguj platby tankovací kartou do FCI RfP (SYS.BAR.0.9).                 | *N/A*          | Systém          |
|                              | Importuj EETS EMS faktury (SYS.BAR.0.10.VO1)                               | *N/A*          | Systém          |
|                              | Importuj jednorázovou ENF fakturu (SYS.BAR.0.11.VO1)                       | *N/A*          | Systém          |
|                              | Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR)            | *New*          | Systém          |
|                              | Vytvoř výzvu na úhradu za přestupek (SYS.BAR.0.13.HR)                      | *New*          | Systém          |
|                              | Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR)                      | *New*          | Systém          |
| Zpracování mýtných transakcí | Zpracuj billing details (SYS.BAR.1.1)                                      | *N/A*          | Systém          |
|                              | Zpracuj billing details (SYS.BAR.1.1.VO2)                                  | *N/A*          | Systém          |
|                              | Vytvoř souhrn oceněných událostí pro VTK (SYS.BAR.1.2)                     | *N/A*          | Systém          |
|                              | Vytvoř souhrn fakturačních detailů pro PL (SYS.BAR.1.3)                    | *N/A*          | Systém          |
|                              | Vytvoř platební oznámení pro PL (SYS.BAR.1.4)                              | *N/A*          | Systém          |
|                              | Zpracuj nárok na platbu pro BG (SYS.BAR.1.5)                               | *N/A*          | Systém          |
|                              | Vytvoř souhrn mýtných transakcí pro VTK (TT) (SYS.BAR.1.6)                 | *N/A*          | Systém          |
|                              | Zpracuj oceněnou událost zpoplatnění (SYS.BAR.1.7.VO1)                     | *N/A*          | Systém          |
|                              | Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR)                            | *New*          | Systém          |
|                              | Vytvoř billing details (SYS.BAR.1.9.VO1)                                   | *N/A*          | Systém          |
|                              | Vytvoř billing details (SYS.BAR.1.9.HR)                                    | *Upd*          | Systém          |
|                              | Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR)                          | *New*          | *Systém*        |
|                              | Vytvoř Přestupek (SYS.BAR.1.11.HR)                                         | *New*          | *Systém*        |
| Operace s platbami           | Vytvoř platbu bankovním převodem (SYS.BAR.2.1)                             | *N/A*          | Systém          |
|                              | Proveď párování (SYS.BAR.2.2)                                              | *N/A*          | Systém          |
|                              | Zúčtuj závazky a pohledávky (SYS.BAR.2.3)                                  | *N/A*          | Systém          |
|                              | Zúčtuj závazky a pohledávky (SYS.BAR.2.3.VO1)                              | *N/A*          | Systém          |
|                              | Zúčtuj závazky a pohledávky (SYS.BAR.2.3.HR)                               | *Upd*          | Systém          |
|                              | [Vrať depozit na tankovací kartu (SYS.BAR.2.4)]{.mark}                     | *N/A*          | [Systém]{.mark} |
|                              | [Vytvoř souhrn debetních plateb pro VTK (SYS.BAR.2.5)]{.mark}              | *N/A*          | [Systém]{.mark} |
|                              | Rezervuj depozit z předplaceného kreditu (SYS.BAR.2.6)                     | *N/A*          | Systém          |
|                              | Zruš rezervaci depozitu z předplaceného kreditu (SYS.BAR.2.7)              | *N/A*          | Systém          |
|                              | Zúčtuj závazky a pohledávky pro EETS Provider (SYS.BAR.2.8.VO1)            | *N/A*          | Systém          |
|                              | Zpracuj bankovní výpis (SYS.BAR.2.9.VO1)                                   | *N/A*          | Systém          |
|                              | Rozpoznej položky bankovního výpisu (SYS.BAR.2.10.VO1)                     | *N/A*          | Systém          |
|                              | Vrať platbu (SYS.BAR.2.11.VO1)                                             | *N/A*          | Systém          |
|                              | [Vrať automaticky platbu (SYS.BAR.2.12.VO1)]{.mark}                        | *[N/A]{.mark}* | [Systém]{.mark} |
|                              | Vytvoř položku platebního příkazu (SYS.BAR.2.13.VO1)                       | *N/A*          | Systém          |
|                              | Aplikuj centové vyrovnání (SYS.BAR.2.14.VO1)                               | *N/A*          | Systém          |
|                              | Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR)                | *New*          | Systém          |
|                              | Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR)               | *New*          | Systém          |
|                              | Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR)                      | *New*          | Systém          |
|                              | Ověř token (SYS.BAR.2.18.HR)                                               | *New*          | Systém          |
|                              | Zúčtuj závazky a pohledávky Business Partnera (SYS.BAR.2.19.HR)            | *New*          | Systém          |
|                              | Tokenizuj kartu přes EFT (SYS.BAR.2.20.HR)                                 | *New*          | Systém          |
| Pomocné operace              | Stáhni kurzovní lístek Erste Bank (SYS.BAR.3.0)                            | *N/A*          | Systém          |
|                              | Stáhni kurzovní lístek Tatrabanky (SYS.BAR.3.1)                            | *N/A*          | Systém          |
|                              | Spočítej minimální částku top-up (SYS.BAR.3.2)                             | *N/A*          | Systém          |
|                              | Vytvoř finanční transakci (SYS.BAR.3.3.VO1)                                | *N/A*          | Systém          |
|                              |                                                                            |                |                 |
| Správa slev                  | Importuj nárok na slevu v doméně CZ (SYS.BAR.4.1)                          | *N/A*          | Systém          |

: Tabulka 33: Seznam systémových funkcí

## Fakturace

### Vytvoř pravidelné faktury za mýtné (SYS.BAR.0.1.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování pravidelných faktur za mýtné.

#### Spuštění případu

Případ je spuštěn systémovou úlohou BE_CloseBillSessionsBySystem

#### Popis

Normální typ fakturační dávky obsahující mýto

Systém dohledá všechny Bill session s:

- Bill session status = Open,

- Bill session end date \< aktuální datum,

- Bill session aggregation type = Pre-paid, Post-paid card, Post-paid invoice, Exemption partner, [Fleet card issuer]{.mark} a EETS Provider,

- Bill session content type = Toll,

- Bill session type = Normal

a pro každou Bill session vykoná nasledující postup:

Systém změní **Bill session status na Closing** a postupně provádí následující fakturační kroky:

- Systém vytvoří daňový bill item pro každou sazbu daně vyskytující se v bill items patřící do dané bill session a k danému bill:

  - Bill item category = Tax

  - Bill item type =

    - Corrective bill item credit, pokud součet bill item s danou sazbou daně byl \< 0,

    - jinak Regular bill item

  - Price amount = celková daň za bill itemy s danou tax rate (Tax base \* Tax rate a následné zaokrouhlení podle BillRounding pro danou měnu)

  - Unit price = null

  - Number of units = null

  - Metric unit = null

  - Tax rate = tax rate pro kterou se bill item vytváří

  - Tax base = celková částka bez daně s danou tax rate (suma Price amount příslušných nedaňových bill items s ohledem na jejich Bill item type a následné zaokrouhlení podle BillRounding)

- 

- Systém zaokrouhlí bill item.price amount podle BillRounding.

- Systém pro každou daňovou bill item zjistí, zda není potřeba vytvořit bill item pro Rounding adjustment:

  - pokud rozdíl mezi (Tax base daňové bill itemy) a (absolutní hodnoty součtu Price amount nedaňových bill item se shodnou tax rate a s ohledem na jejich Bill item type) = 0, rounding adjustment není potřeba pro danou daňovou bill item.

  - jinak Systém vytvoří korekční bill item s parametry:

    - Bill item category = Rounding adjustment

    - Product type = null

    - Bill item type =

    <!-- -->

    - - 
      - 

    - - 

      - - Pokud součet Tax base všech daňových Bill item a Price amount všech daňových Bill items \>= 0, a pokud vypočtený rozdíl je menší než nula, pak Corrective bill item -- credit, jinak Corrective bill item -- debit Pokud součet Tax base všech daňových Bill item a Price amount všech daňových Bill items \< 0,A pokud vypočtený rozdíl je větší než nula, pak Corrective bill item -- credit, jinak Corrective bill item -- debit Unit price = Price amount

        - Unit price definition method = None

        - Number of units = 1

        - Metric unit = Piece

        - Tax rate = null

        - Price amount = absolutní hodnota vypočteného rozdílu

        - Price amount VAT = Price amount

        - Billing service = Systém zjistí billing service z PCRE na základě Billing service.abbreviation = ADJ-ROUNDING

- Systém vypočítá základ daně faktury (Bill amount) tak, že sečte Tax base všech daňových Bill item.

- Systém vypočítá daň faktury (Tax amount) tak, že sečte Price amount všech daňových Bill items.

- Systém vypočítá celkovou částku faktury (Total amount) tak, že sečte Bill amount a Tax amount.

- Pokud vypočtená hodnota Total amount je \< 0, Systém nastaví bill.Bill issue type = Corrective bill -- credit, jinak na bill.Bill issue type = Regular bill.

- Pokud vypočtená hodnota Total amount je = 0, Systém nastaví bill.Bill payment status = Payment not needed.

- Do bill.Total amount, bill.Bill amount a bill.Tax amount se uloží absolutní hodnota vypočtených částek.

- Systém updatuje další bill atributy:

  - Bill number = použijí se pravidla Číslování faktur na základě Bill issue type

  - Fiscal verification number = vygeneruje se Fiskální verifikační číslo ze sekvence pro číslování faktur (BNF77) s Business Premises BO, určeným podle user profile

  - ZKI = vyplní se Ochranný kód vystavitele faktury (Issuer\'s Protection Code)

  - Bill type =

    - Customer bill pokud Bill session aggregation type = Pre-paid[,]{.mark} Post-paid card, Post-paid invoice,

    - EETS Provider bill, pokud Bill session aggregation type = EETS Provider

    - Exemption partner bill, pokud Bill session aggregation type = Exemption partner

    - [Fleet card issuer bill, pokud Bill session aggregation type = Fleet card issuer]{.mark}

  - Date of issue = systémové datum

  - Date of beginning = Bill session.Bill period start

  - Date of end = Bill session.Bill period end

  - Matched amount = 0

  - Bill issuer bank account = zjištěné číslo bankovního účtu Bill issuera (BIBA) pro Reason = toll

- [Systém vypočítá termíny splatnosti (Bill Due date)]{.mark}

  - [pro fakturu a vrubopis tak, že k Bill Date of issue přičte hodnotu Maturity period z příslušného Účtu, případně příslušné specializace Business partnera.]{.mark}

  - [pro EETS dobropis tak, že k Bill Date of issue přičte hodnotu Maturity period for credit note z příslušného Poskytovatele mýtných služeb,]{.mark}

  - [pro jiný dobropis tak, že k Bill Date of issue přičte hodnotu z konfiguračního klíče BE_Maturity period for customer credit note.]{.mark}

  - [Systém automaticky spáruje: vytvořené dobropisy s Issued fakturami/vrubopisy za mýto ze stejné mýtné domény, stejného subjektu, ve stejné zúčtovací měně a stejného System operator.ERP abbreviation.Systém pro každý dobropis dohledá veškeré nespárované issued faktury/vrubopisy za Toll ze stejné mýtné domény, ve shodné zúčtovací měně, patřící stejnému subjektu, se stejným System operator.ERP abbreviation a seřadí je od nejstarší.]{.mark}

  - [Systém spáruje seřazené dobropisy s  fakturami nebo vrubopisy od nejstaršího, až do výše nevypárované částky dobropisu nebo neuhrazené částky bill, tj. vytvoří pro každé párování Matching s parametry:]{.mark}

    - [Date of matching = Datum a čas, kdy bylo párování provedeno]{.mark}

    - [Effective date of matching = vyšší z datumů párovaných stran (tj. bill.date od end)]{.mark}

    - [Bill -- debit matching side = Faktura/Vrubopis]{.mark}

    - [Bill -- credit matching side = Dobropis]{.mark}

    - [Matched amount = Párovaná částka = menší z (rozdíl mezi Total amount in clearing currency a Matched amount faktury/vrubopisu; rozdíl mezi Total amount in clearing currency a Matched amount dobropisu)]{.mark}

    - [Matching method = Automatic]{.mark}

    - [Disconnect allowed = True]{.mark}

  - [Systém u všech automaticky napárovaných faktur a dobropisů updatuje bill.matched amount a bill.payment status v závislosti na výši vypárované částky.]{.mark}

  - [Systém automaticky spáruje: vytvořené faktury/vrubopisy s Issued dobropisy za mýto nebo slevu z mýtného, ze stejné mýtné domény, stejného subjektu, ve stejné zúčtovací měně a stejného System operator.ERP abbreviation:]{.mark} [Systém pro každou fakturu/vrubopis dohledá veškeré nespárované issued dobropisy za Toll a Toll dicount, ze stejné mýtné domény, ve shodné zúčtovací měně, patřící stejnému subjektu, se stejným System operator.ERP abbreviation a seřadí je od nejstaršího.]{.mark}

  - [Systém spáruje seřazené dobropisy s  fakturami nebo vrubopisy od nejstaršího, až do výše nevypárované částky dobropisu nebo neuhrazené částky bill, tj. vytvoří pro každé párování Matching s parametry:]{.mark}

    - [Date of matching = Datum a čas, kdy bylo párování provedeno]{.mark}

    - [Effective date of matching = vyšší z datumů párovaných stran (tj. bill.date od end)]{.mark}

    - [Bill -- debit matching side = Faktura/Vrubopis]{.mark}

    - [Bill -- credit matching side = Dobropis]{.mark}

    - [Matched amount = Párovaná částka = menší z (rozdíl mezi Total amount in clearing currency a Matched amount faktury/vrubopisu; rozdíl mezi Total amount in clearing currency a Matched amount dobropisu)]{.mark}

    - [Matching method = Automatic]{.mark}

    - [Disconnect allowed = True]{.mark}

  - [Systém u všech automaticky napárovaných faktur a dobropisů updatuje bill.matched amount a bill.payment status v závislosti na výši vypárované částky.]{.mark}

  - [Systém automaticky spáruje vytvořené a v předešlém kroku plně neuhrazené faktury/vrubopisy s přeplatky (jiného typu než Deposit payment) shodného subjektu, ve stejné zúčtovací měně a stejného System operator.ERP abbreviation:Systém dohledá nevypárované kreditní platby jiného typu než Deposit payment, ve shodné zúčtovací měně, patřící stejnému subjektu, se stejným System operator.ERP abbreviation a seřadí je od nejstarší.]{.mark}

  - [Systém spáruje seřazené platby s  fakturami nebo vrubopisy od nejstarší, až do výše nevypárované částky platby nebo neuhrazené částky bill, tj. vytvoří Matching s následujícími parametry:]{.mark}

    - [Date of matching = aktuální datum]{.mark}

    - [Effective date of matching = vyšší z datumů párovaných stran (tj. payment.date of collection, bill.date od end)]{.mark}

    - [Payment -- credit matching side = platba faktury]{.mark}

    - [Bill -- debit matching side = neuhrazená faktura nebo vrubopis]{.mark}

    - [Matched amount = menší z (rozdíl mezi Total amount in clearing currency a Matched amount faktury/vrubopisu; rozdíl mezi Payment amount in clearing currency a Matched amount platby)]{.mark}

    - [Matching method = Automatic]{.mark}

    - [Disconnect allowed = True]{.mark}

  - [Systém updatuje na napárovaných platbách:]{.mark}

    - [Matching status na Recognized-matched nebo Recognized -- partially matched, v závislosti na výši párované částky.]{.mark}

    - [Matched amount = součet všech Matching.Matched amount dané platby]{.mark}

  - [Systém updatuje na napárovaných bills:]{.mark}

    - [Bill payment status na Paid fully nebo Paid partially, v závislosti na výši párované částky]{.mark}

    - [Matched amount = součet všech Matching.Matched amount daného bill]{.mark}

- Systém vytvoří statistiku fakturační dávky.

Systém nastaví Bill status na **Waiting for print** a postupně provádí následující fakturační kroky:

- Systém informace o faktuře v ePorezna formátu (XML) odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

- Systém propíše Unique invoice identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

- Systém vygeneruje podle bill type, bill issue type a bill category všechny dokumenty faktur, vrubopisů případně dobropisů v pdf formátu za využití systémoveé funkce Vytvoř a ulož dokument (SYS.DFRP.1.1):

  - Faktura za mýtné (DOC.BE.10.HR)

  - Vrubopis za mýtné (DOC.BE.13.HR)

  - Dobropis za mýtné (DOC.BE.14.HR),

- Systém updatuje Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

- Systém pro [každý]{.mark} Customer bill za mýto připraví a vygeneruje souhrnný detailní výpis (Detailní výpis mýtných transakcí k faktuře (DOC.BE.11.HR)) jako povinnou součást vytvořené faktury.

- Systém zjistí, zda se má faktura vygenerovat také v xml formátu jako elektronická faktura (tj. pokud CM.Account.Preferred electronic invoice format = FINA, nebo ECM.EETS Provider.Preferred electronic invoice format = FINA, nebo CM.Exemption partner.Preferred electronic invoice format = FINA).

- V případě požadovaného elektronického formátu (XML) faktury:

  - Systém navíc vygeneruje eFakturu (DOC.BE.21.HR). Systém dokument uloží s využitím případu užití Ulož externí dokument (SYS.DFRP.1.4).

  - Systém updatuje Bill.E-Bill document = identifikátor vytvořeného XML dokumentu faktury.

- Systém odešle všechny pdf a případně i XML verze faktur, vrubopisů, dobropisů a info o Detailním výpisu v csv formátu na zákazníkův/EETS Provider/Exemption partner email (pokud je vyplněn) společně s notifikací Oznámení o vystavení faktury (NTF.DF.01.HR).

- Systém případně odešle XML verzi faktury přes eFINA přes Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR).

- Systém změní stav Bill.Bill issue status na Issued.

Systém dokončí proces vytváření pravidelných faktur a nastaví stav **Bill session na Closed,** pokud se všechny Bills dostaly do stavu Issued. Systém postupně provádí následující fakturační kroky:

- 

Postup končí

#### Alternativní postupy

Fakturační dávka opožděných událostí

Systém zpracuje opožděné mýtné události, které vznikly v již vyfakturovaném období, které přišly do Systému až po uzávěrce fakturační dávky, do které patří podle data mýtné transakce.

Systém vybere bill session type = Delayed (Systém automaticky spustí proces uzavírání pravidelné fakturační dávky typu Delayed pouze u zpracovávání normálního typu pravidelné fakturační dávky).

Postup pokračuje kroky jako u normálního typu fakturační dávky s tím rozdílem, že:

- Pokud při vytváření tax bill itemy je součet bill item s danou sazbou daně

  - \< 0, pak Bill item type = Corrective bill item credit,

  - \>=0 a zároveň neexistují Corrective bill items debit a součet Corrective bill items credit je 0, pak Bill item type = Regular bill item,

  - jinak Bill item type = Corrective bill item debit

- Pokud vypočtená hodnota bill.Total amount je \< 0, Systém nastaví bill.Bill issue type = Corrective bill -- credit, jinak na bill.Bill issue type = Corrective bill -- debit.

- Detailní výpis mýtných transakcí se vytvoří v případě opožděných mýtných transakcí jen v důsledku vydání vrubopisu) pro Customer bills.

Fakturační dávka znovuoceněných událostí

Systém zpracuje opětovně oceněné mýtné události.

Systém vybere bill session type = Rerated (Systém automaticky spustí proces uzavírání pravidelné fakturační dávky typu Rerated pouze u zpracovávání normálního typu pravidelné fakturační dávky).

Postup pokračuje kroky jako u normálního typu fakturační dávky s tím rozdílem, že:

- Pokud při vytváření tax bill itemy je součet bill item s danou sazbou daně

  - \< 0, pak Bill item type = Corrective bill item credit,

  - \>= 0, pak Bill item type = Corrective bill item debit

- Pokud vypočtená hodnota bill.Total amount je \< 0, Systém nastaví bill.Bill issue type = Corrective bill -- credit, jinak na bill.Bill issue type = Corrective bill -- debit. Do bill.Total amount se uloží absolutní hodnota vypočtené částky.

- Detailní výpis mýtných transakcí se nevytvoří.

- 

#### Chybové postupy

Bill - Print failed

Pokud se nepodařilo vygenerovat všechny dokumenty billu (tj. nedokončil se některý z následujících kroků), Systém u takovýchto faktur nastaví jejich stav Bill.Bill issue status na Print failed:

- ePorezna package -- nepovedlo se mapování / výroba xml/json

- odeslání do ePorezna -- skončilo jako business error

- tvorba document xml -chyba v načítání dat z CM nebo chyba při tvorbě XML

- zaslání xml do DF: GenerateDocument -- skončilo s error result

- tvorba eBill - chyba načítání dat z CM

- uložení eBill do DF: StoreExternalDocument - skončilo s error result

- detailní výpis - chyba načítání dat z CM nebo chyba při tvorbě XML

- uložení detailního výpisu do DF: StoreExternalDocument - skončilo s error result

- odeslání faktur přes DF: SendDocument - skončilo s error result

- odeslání eBill z DF: SendToEfina - skončilo s error result

Bill session - Closed with error

Systém dokončí proces vytváření pravidelných faktur a nastaví stav **Bill session na Closed with error**, pokud některý z Bills se dostal do stavu Print failed (tzn. nejsou všechny ve stavu Issued).

Na základě manuálně spuštěného dokončovacího jobu, Systém pro každou Bill session (tj. normal, delayed, rerated) ve stavu Closed with error se pokusí pro Bills ve stavu Print failed znovu vygenerovat potřebné dokumenty.

Pokud bylo generování dokumentů úspěšné, Systém nastaví Bill.Bill issue status na Issued, jinak ponechá stav Print failed.

Po zprocesování všech problematických Bills, Systém nastaví stav Bill session na Closed, pokud všechny Bill jsou již Issued, jinak ponechá stav Closed with error a proces se opakuje.

#### Poznámky

Pro Customer bills Detailní výpis mýtných transakcí se vytvoří pouze v případě, že existuje alespoň jeden oceněný záznam pro daný účet.

Pro Customer bills Detailní výpis mýtných transakcí se dále vytvoří v případě opožděných mýtných událostí (v důsledku vydání vrubopisu).

### Vytvoř jednorázovou fakturu za služby (SYS.BAR.0.4.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování jednorázové faktury nebo proforma faktury za naúčtované jednorázové poplatky nebo za Top-up.

#### Spuštění případu

Případ užití je vloženou součástí případů užití:

- Top-up

  - Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

  - Vygeneruj proforma fakturu (API.BAR.1.1.HR)

- OBU

  - Vydaj OBU na POS (UC.VCM.2.9)

  - Vygeneruj proforma fakturu (API.BAR.1.1.HR)

- Produktový balíček

  - Zaplať Produktový balíček (UC.BAR.0.21.HR)

  - [Vygeneruj proforma fakturu (API.BAR.1.1.HR)]{.mark}

- OBU příslušenství

  - Prodej příslušenství OBU na POS (UC.OL.1.7.HR)

#### Podmínky spuštění

Pro daný Account, pro které je potřeba vystavit fakturu, je na vstupu:

- 
- 
- 
- 
- 

identifikace Accountu (národního případně produktového)oceněná událost (včetné počtu jednotek), Bill issuer, info o POS (pokud je to relevantní)informace o platbě nebo o požadované částce k zaplacení (pak jde o vystavení Proforma faktury na požadovanou částku)

Poznámka: Pro FCI, EETS Provider a Exemption partner není aktuálně UC potřeba realizovat.

#### Normální postup

Systém zjistí BIBA pro fakturaci na základě Bill issuer ze vstupu a Reason:

- Top-up, pokud jde o Top-up operaci

- OBU, pokud jde o OBU operaci

- Product, pokud jde o Product package operaci

- jinak Services.

- 

Systém, pokud jde o Top-up, vytvoří Rated Service Event pro top-up:

- Event time = sysdate

- Product type = PCRE.product type (Top-Up)

- Type = Rating

- Basic unit price = Price amount

- Basic unit price definition method = PCRE.product type.unit price definition method (none)

- Unit price = Price amount

- Unit price VAT = Price amount VAT

- Number of units = 1

- Metric unit = piece

- Tax rate = PCRE.tax rate rate

- Price amount = částka top-up platby/(1+tax rate)

- Price amount VAT = částka platby nebo požadovaná částka top-up

- Billing service = PCRE.billing service

- Number of units corrected = null

- Cancellable = True

- Subject type = Account, pokud na vstupu je identifikace Account

- Subject number = ze vstupu

- Bill issuer = ze vstupu

- [FCI partner = FCI karty v případě platby tankovací kartou]{.mark}

- [Fleet Card Number = Číslo tankovací karty v případě platby tankovací kartou]{.mark}

- [Fleet Card Id = Id tankovací karty v případě platby tankovací kartou]{.mark}

Systém, pokud jde o platbu za Produktový balíček, vytvoří Rated Service Event pro Product package:

- Event time = sysdate

- Product type = PCRE.product type (Product package)

- Type = Rating

- Basic unit price = Price amount

- Basic unit price definition method = PCRE.product type.unit price definition method (none)

- Unit price = Price amount

- Unit price VAT = Price amount VAT

- Number of units = 1

- Metric unit = piece

- Tax rate = PCRE.tax rate rate

- Price amount = částka platby/(1+tax rate)

- Price amount VAT = částka platby nebo požadovaná částka top-up Produktového balíčku

- Billing service = PCRE.billing service

- Number of units corrected = null

- Cancellable = True

- Subject type = Product Account

- Subject number = ze vstupu

- Bill issuer = ze vstupu

- [FCI partner = FCI karty v případě platby tankovací kartou]{.mark}

- [Fleet Card Number = Číslo tankovací karty v případě platby tankovací kartou]{.mark}

- [Fleet Card Id = Id tankovací karty v případě platby tankovací kartou]{.mark}

Pokud nejde o Top-up nebo Product package, Systém na základě každé oceněné události ze vstupu vytvoří jednorázový poplatek, za použití systémové funkce Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR).

Systém seskupí oceněné události podle atributů Rated service events:

- Subject number (tj. Account nebo null),

- Billing service,

- Unit price VAT,

- Unit price,

- Tax rate,

- Product type,

- Basic unit price definition method,

- Card number (pokud je na vstupu)

- Discount rate.

a pro každou kombinaci vytvoří Bill Item s parametry:

- Bill item category =

  - Top-up event, pokud Product type = Top-up

  - OBU event, pokud Product type = OBU

  - Product package event, pokud Product type = Product package

  - OBU accessories event, pokud Product type = OBU accessories

  - jinak Service event

- Bill item type = Regular bill item

- Unit price = Unit price z RSE

- Unit price VAT = Unit price VAT z RSE

- Number of units = součet z Number of units RSE

- Metric unit = Piece

- Tax rate = Tax rate z RSE

- Price amount = částka poplatků bez daně,

- Price amount VAT = částka poplatků s daní

- Billing service = Billing service z RSE

Systém pro každou sazbu tax rate vytvoří tax bill item:

- Bill item category = Tax

- Bill item type = Regular bill item

- Number of units = null

- Metric unit = null

- Tax rate = sazba daně (v procentech)

- Price amount = celková daň za bill itemy s danou tax rate (Tax base \* Tax rate a zaokrouhlení na dvě desetinná místa)

- Tax base = celková částka bez daně s danou tax rate (suma Price amount příslušných nedaňových bill items a zaokrouhlení na dvě desetinná místa)

Systém zjistí pro každou sazbu daně, zda není potřeba Rounding adjustment:

- Pokud rozdíl, daňové bill item.tax base a absolutní hodnoty součtu nedaňových bill item.price amount, není roven nule, Rounding adjustment bill item se vytvoří s výsledkem rozdílu jako bill item.price amount

- Pokud rozdíl, (součtu daňové bill item.tax base a daňové bill item.price amount) a součtu nedaňových bill item.price amount VAT, není roven nule, Rounding adjustment bill iem se vytvoří, s výsledkem rozdílu jako bill item.price amount VAT

  - Systém vytvoří korekční bill item s parametry:

  - Bill item category = Rounding adjustment

  - Product type = null

  - Bill item type =

    - pokud vypočtený rozdíl je větší než 0, pak Corrective bill item -- credit,

    - jinak Corrective bill item -- debit

  - Unit price = Price amount

  - Unit price VAT = Price amount VAT

  - Number of units = 1

  - Metric unit = Piece

  - Tax rate = null

  - Price amount = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

  - Price amount VAT = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

  - Billing service = Systém zjistí billing service z PCRE na základě Billing service.abbreviation = ADJ-ROUNDING

Systém vytvoří vytvoří Bill s parametry:

- Bill number = Unikátní číslo faktury podle schématu z Číslování faktur v závislosti na Bill type, Bill issue type, Bill category a Bill issuer.

- Fiscal verification number = vygeneruje se Fiskální verifikační číslo ze sekvence pro číslování faktur (BNF77) s Business Premises BO, určeným podle user profile

- ZKI = vyplní se Ochranný kód vystavitele faktury (Issuer\'s Protection Code)

- Bill type =

  - Pokud jde o subject type = Account, pak Customer bill

  - [pokud jde o Fleet card issuer, pak FCI bill]{.mark}

  - [pokud jde o Exemption partner, pak Exemption partner bill]{.mark}

  - [pokud jde o subjecte type = EETS Provider, pak EETS Provider bill]{.mark}

- Bill category =

  - OBU, pokud Bill item category = OBU event,

  - OBU accessories, pokud Bill item category = OBU accessories,

  - Top-up, pokud Bill item category = Top-up event,

  - Product package, pokud Bill item category = Product package event,

  - jinak Services.

- Bill issue type =

  - Proforma bill, pokud je požadována Proforma pro danou operaci (požadována platba bankovním převodem),

  - Advance bill, pokud Bill category = Top-up a existuje realizovaná platba pro danou operaci,

  - jinak Regular bill.

- Bill recurrence type = One-time bill

- Bill issue status = Issued

- Bill payment status = Unpaid

- Comment = null

- Bill amount = součet daňových bill items.tax base

- Tax amount = součet daňových bill items.price amount

- Total amount = součet Bill amount a Tax amount

- Date of issue = aktuální datum

- Due date = se vypočte tak, že k Bill Date of issue se přičte hodnota Maturity period z příslušného Účtu, [případně z Provider EETS, případně z Exemption partner, případně z FCI]{.mark}.

- Date of beginning = aktuální datum

- Date of end = aktuální datum

- Matched amount = 0

- Subject type = Subject type z RSE

- Subject number = Subject number z RSE

- Bill issuer bank account = zjištěné číslo bankovního účtu Bill issuera (BIBA)

- Bill issuer = Bill issuer ze vstupu

Pokud se nejedná o Proforma bill, Systém informace o faktuře v XML formátu odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

Systém propíše Unique Invoice Identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

Pokud se případ užití spustil na POS (MEV, Kiosk, POS), Systém zjistí, zda se má dokument generovat ve variantě (DOC.BE.x) v případě A4 formátu [nebo (DOC.BE.x**B**) v případě thermo tisku na POS (podle POS.Printer type).]{.mark}

Systém, s ohledem na zjištěnou variantu dokumentu, vygeneruje dokument faktury v pdf formátu:

- Pokud jde o bill category = Top-up, pak Zálohová faktura za top-up (DOC.BE.1.HR) v případě A4 formátu, nebo (DOC.BE.1B.HR) v případě thermo tisku

- pokud jde o bill issue type = Proforma bill, pak Proforma faktura (DOC.BE.24.HR),

- jinak (Faktura za služby (DOC.BE.16.HR),

s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém zjistí, zda se má faktura vygenerovat také v xml formátu jako elektronická faktura (tj. pokud CM.Account.Preferred electronic invoice format = FINA, [nebo ECM.EETS Provider.Preferred electronic invoice format = FINA, nebo CM.Exemption partner.Preferred electronic invoice format = FINA)]{.mark}.

V případě požadovaného XML formátu, Systém navíc vygeneruje eFakturu (DOC.BE.21.HR). Systém dokument uloží s využitím případu užití Ulož externí dokument (SYS.DFRP.1.4).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém případně updatuje Bill.E-Bill document = identifikátor vytvořeného XML dokumentu faktury.

[Pokud vygenerování faktury proběhlo na žádost DU, Systém odešle do DU identifikaci vzniklé faktury.]{.mark}

Pokud vygenerování faktury proběhlo pro POS (MEV, POS), Systém dokument nabídne ke stažení.

Pokud vygenerování faktury proběhlo pro Kiosk, Systém dokument faktury nenabídne ke stažení, ale vystaví a vytiskne Doklad o navýšení kreditu (DOC.KIO.04.HR).

Systém odešle pdf a případně XML verzi faktury na zákazníkův email [případně email Poskytovatele mýtných služeb]{.mark} společně s notifikací:

- 
- 

Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR), pokud jde o Top-upjinak Oznámení o vystavení faktury (NTF.BAR.21.HR).

Systém případně odešle XML verzi faktury přes eFINA přes Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR).

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

### Vytvoř fakturační dávku (SYS.BAR.0.6.HR) 

#### Cíl

Cílem tohoto případu užití je otevření nové Bill session.

Budou se vytvářet Bill sessions podle nastavených Bill cycles platné pro jednotlivé Bill session aggregation typy, Bill session content typy a normální Bill session type.

#### Spuštění případu

Na základě naplánované operace BEm.CreateBillSessions.

#### Podmínky spuštění

#### Popis

Systém vytvoří novou Bill Session na základě hodnot bill session aggregation type, Bill session content type a Bill cycle:

- Bill session number = Číslo fakturační dávky ve formátu RRMMDDXXXX

- Bill session aggregation type = Post-paid card, , EETS Provider, Exemption partner, [Fleet card issuer,]{.mark} Pre-paid

- Bill session content type = Toll

- Bill session type = Normal

- Bill session status = Open

- Bill period start = navazující na Bill period end předchozí Bill session

- Bill period end = Bill period start posunutý o Bill cycle

- Bill cycle = Month, 15-days

- 

Nastavení při instalaci:

pro EETS Provider a Toll

- Bill session aggregation type = EETS Provider

- Bill session content type = Toll

- Bill cycle = 15-days, Month (agregace podle hodnoty atributu Bill cycle na EETS Provider)

pro Post-paid Invoice a Toll

- Bill session aggregation type = Post-paid Invoice

- Bill session content type = Toll

- Bill cycle = Month (agregace podle hodnoty atributu Bill cycle na Account)

pro Post-paid Card a Toll

- Bill session aggregation type = Post-paid Card

- Bill session content type = Toll

- Bill cycle = Month (agregace podle hodnoty atributu Bill cycle na Account)

pro Exemption partner a Toll

- Bill session aggregation type = Exemption partner

- Bill session content type = Toll

- Bill cycle = 15-days, Month (agregace podle hodnoty atributu Bill cycle na VCM.Exemption partner)

[pro FC payments]{.mark}

- [Bill session content type = FC payments (agregace podle typu bill itemy)]{.mark}

- [Bill cycle = 15-days, Month (agregace podle hodnoty atributu Bill cycle na FCI)]{.mark}

[pro Fleet card issuer a Toll]{.mark}

- [Bill session aggregation type = Exemption partner]{.mark}

- [Bill session content type = Toll]{.mark}

- [Bill cycle = 15-days, Month (agregace podle hodnoty atributu Bill cycle na VCM.Exemption partner)]{.mark}

pro Pre-paid a Toll

- Bill session aggregation type = Pre-paid

- Bill session content type = Toll

- Bill cycle = Month (agregace podle hodnoty atributu Bill cycle na Account)

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

### Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování jednorázového poplatku na žádost různých procesů.

#### Spuštění případu

Případ užití je vloženou součástí případů užití:

- UCs vyžadující zákonnou pokutu za Přestupek (Offence)

  - Vytvoř výzvu na úhradu za přestupek (SYS.BAR.0.13.HR)

  - Vytvoř jednorázovou fakturu za mýto (SYS.BAR.14.HR)

- UCs vyžadující naúčtovat poplatek za OBU

  - Vytvoř jednorázovou fakturu za mýto (SYS.BAR.14.HR) z Vydaj OBU na POS (UC.VCM.2.9)

  - Vygeneruj proforma fakturu (API.BAR.1.1.HR)

- UCs vyžadující naúčtovat poplatek za OBU příslušenství

  - Vytvoř jednorázovou fakturu za mýto (SYS.BAR.14.HR) z Prodej příslušenství OBU na POS (UC.OL.1.7.HR)

- [UC vyžadující Poplatek za odeslání OBU poštou]{.mark}

  - [Zjisti počty zásilek pro naúčtování poplatků za zaslání OBU (SYS.CM.7.38)]{.mark}

  - 

#### Podmínky spuštění

Je znám:

- Bill issuer a event id, počet jednotek a subjekt

- nebo typ poplatku nebo poplatků, který je potřeba vygenerovat (tj. Product type a odpovídající hodnotu Event attribute type), počet jednotek a subjekt (případně subjekt type):

  - Legal penalty za Offence:

    - Product type = LP (Legal penalty) + hodnota event atributu type = Chargeable service ze vstupu (Legal penalty),

    - Počet jednotek

    - Info o subjektu

    - Bill issuer

  - OBU:

    - Product type = OBU + pro event atribut type = Chargeable service, jeho hodnota = OBU fee,

    - Počet jednotek

    - Info o subjektu

    - Bill issuer

  - OBU accessories:

    - Product type = OBU accessories + pro event atribut type = Chargeable service, jeho hodnota = např. OBU Holder 1,

    - Počet jednotek

    - Info o subjektu

    - Bill issuer

  - [OBU sending:]{.mark}

    - [Product type = OBU nebo ?Chargeable services + pro event atribut type = Chargeable service, jeho hodnota = OBU sending fee,]{.mark}

    - [je znám vypočítaný počet zásilek]{.mark}

    - [Info o subjektu]{.mark}

    - [případně info o Fleet card, pokud jde o platbu fleet card]{.mark}

    - [Bill issuer]{.mark}

Poplatky v jednom volání mohou vycházet jen z jednoho Product type.

Poznámka: Pro FCI, EETS Provider a Exemption partner není aktuálně UC potřeba realizovat.

#### Normální postup

Zákonná pokuta za Offence

Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů

- 
- 
- 

Bill issuer, [Bill issuer currency, Bill issuer VAT registration country, VAT registration country zákazníka, VAT registration country zákazníka]{.mark}, Product type = Legal penalty + hodnota event atributu typu = Chargeable service ze vstupu (i.e. Legal penalty, ),za použití systémové funkce Oceň produkt (SYS.PCRE.1.4.HR).

Postup pokračuje krokem **Společný postup pro všechny poplatky** s Number of units = počet Offences daného Bill issuer.

Poplatek za OBU

Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů

- 
- 
- 

Bill issuer, [Bill issuer currency, Bill issuer VAT registration country, VAT registration country zákazníka, VAT registration country zákazníka,]{.mark} Product type = OBU + hodnota event atributu typu = Chargeable service ze vstupu (OBU sending fee), za použití případu užití Oceň produkt (SYS.PCRE.1.4).

Postup pokračuje krokem **Společný postup pro všechny poplatky** s Number of units = počet OBU.

Poplatek za OBU accessories

Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů

- 
- 
- 

Bill issuer, [Bill issuer currency, Bill issuer VAT registration country, VAT registration country zákazníka, VAT registration country zákazníka,]{.mark} Product type = OBU accessories + hodnota event atributu typu = Chargeable service ze vstupu (nepř. OBU Holder 1), za použití případu užití Oceň produkt (SYS.PCRE.1.4).

Postup pokračuje krokem **Společný postup pro všechny poplatky** s Number of units = počet OBU.

[Poplatek za zaslání OBU]{.mark}

[Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů]{.mark}

- 
- 
- 

[Bill issuer, Bill issuer currency, Bill issuer VAT registration country, VAT registration country zákazníka, VAT registration country zákazníka, Product type = OBU nebo ?Chargeable service + hodnota event atributu typu = Chargeable service ze vstupu (i.e. OBU sending fee), za použití případu užití Oceň produkt (SYS.PCRE.1.4).]{.mark}

[Postup pokračuje krokem **Společný postup pro všechny poplatky** s Number of units = spočítaný počet zásilek.]{.mark}

Společný postup pro všechny poplatky

Pokud je poplatek = 0 a konfigurační klíč BE_AggregateZeroServiceTransactions = no, postup pro daný poplatek končí (nevytvoří se RSE a bill item pro tento poplatek).

Systém vytvoří Rated service event pro každý typ poplatku ze vstupu:

- Event time = sysdate

- Type = Rating

- Product type = ze vstupu (PCRE.Product type)

- Basic unit price = z PCRE Basic unit price

- Unit price = z PCRE Unit price

- Unit price VAT= z PCRE Unit price VAT

- Basic unit price definition method = z PCRE.product type.basic unit price definition method

- Number of units = počet jednotek ze vstupu

- Metric unit = Piece

- Tax rate = z PCRE.tax rate

- Price amount = částka poplatku bez daně = z PCRE Price amount \* Number of units

- Price amount VAT = částka poplatku s daní = z PCRE Price amount VAT \* Number of units

- Billing service = z PCRE.billing service

- Subject type =

  - Account, pokud na vstupu Account info,

  - jinak No subject

- Subject number =

  - ze vstupu VCM.account, pokud Subject type = Account,

  - jinak Null

- Cancellable = true

- Number of units corrected = 0

- FCI partner = FCI karty v případě platby tankovací kartou

- Fleet Card Number = Číslo tankovací karty v případě platby tankovací kartou

- Fleet Card Id = Id tankovací karty v případě platby tankovací kartou

Postup končí

#### Alternativní postupy

Žádné

#### Chybové postupy

Žádné

#### Poznámky

Žádné

### Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) 

#### Cíl

Cílem tohoto případu užití je zagregovat vytvořené Oceněné mýtné události (Rated Toll Events) do Fakturační dávky (Bill Sesssion).

#### Spuštění případu

> Je vloženou součástí případu užití:

- Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR)

- Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR)

#### Podmínky spuštění

Jde o Toll Transaction s Registration type = EETS, Exempted, Exempted not compliant nebo Exempted trip, nebo jde o Post-paid card nebo Pre-paid registration type po úspěšné platbě kartou nebo z Balance.

Rated toll event ještě není agregován do Bill session.

#### Popis

Systém na základě nastavení VCM.Exemption partner, VCM.Account nebo ECM.EETS Provider, vyhledá Bill session, která odpovídá podmínkám:

- Pro Subject type = Account a Registration type = Post-paid invoice:

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Post-paid invoice

  - VCM.Account.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type = Toll

- Pro Subject type = Account a Registration type = Exempted not compliant:

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Post-paid invoice

  - VCM.Account.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type = Toll

- Pro Subject type = Account a Registration type = Post-paid card (po úspěšné jakékoli platbě):

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Post-paid card

  - VCM.Account.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type = Toll

- Pro Subject type = Account a Registration type = Pre-paid (po úspěšné jakékoli platbě):

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Pre-paid

  - VCM.Account.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type = Toll

- Pro Subject type = EETS Provider:

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = EETS Provider

  - ECM.EETS Provider.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type= Toll

- Pro Subject type = Exemption partner:

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Exemption partner

  - VCM.Exemption partner.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type= Toll

- 

Pokud Bill session neexistuje, Systém odpovídající session s content type = Toll vytvoří a nastaví její platnost (např. podle původní bill session, do které opoždená nebo opravná položka patřila) tak aby :

- Pro opožděné oceněné mýtné události (události vzniklé v již vyfakturovaném období, které přišly do Systému až po uzávěrce fakturační dávky do které patří podle data mýtné transakce) Systém vytvoří novou pravidelnou fakturační dávku s typem = Delayed.

- Opětovně oceněné nebo rušené mýtné události (rerating chybně oceněných událostí), Systém vytvoří novou pravidelnou fakturační dávku s typem = Rerated.

Systém updatuje atributy na Toll Transaction:

- Agregation time = sysdate time

Systém přiřadí oceněné mýtné události k Bill ve stavu Bill issue status = In progress podle:

- Bill issuer,

- Account nebo EETS Provider nebo Exemption partner,

- a Bill Session.

Pokud Bill neexistuje, Systém vytvoří nový Bill:

- Bill type =

  - Customer bill, pokud Bill session.bill session aggregation type = Post-paid card nebo Post-paid invoice nebo Pre-paid

  - EETS Provider bill, pokud Subjekt type = EETS Provider

  - Exemption partner bill, pokud Subjekt type = Exemption partner

- Bill recurrence type = Periodical bill

- Bill category = Toll

- Bill issue status = In progress

- Bill payment status =

  - Payment not needed, pokud jde o Post-paid card nebo nebo Pre-paid (tj. po úspěšné jakékoli platbě)

  - jinak Unpaid

- Subject type = Toll transaction.Subject type

- Subject number = Toll transaction.Subject type

- Bill issuer bank account = null

- Bill issuer = Toll transaction.Bill issuer

Systém seskupí oceněné mýtné události podle:

- Subject number (tj. Account nebo Exemption partner nebo EETS Provider),

- Bill id

- Billing service,

- Unit price VAT,

- Unit price,

- Tax rate,

- Discount rate,

- Card number (jen pro Bill session.bill session aggregation type = Post-paid card nebo Pre-paid),

- Charge type,

- a Bill Session.

Systém pro každou skupinu z předchozího kroku aktualizuje odpovídající Bill item:

- Price amount navýší o sumu všech Price amount z jednotlivých seskupených Rated toll event,

- Price amount VAT navýší o sumu všech Price amount VAT z jednotlivých seskupených Rated toll event,

- Discount amount navýší o sumu všech Discount amount z jednotlivých seskupených Rated toll event

- Discount amount VAT navýší o sumu všech Discount amount z jednotlivých seskupených Rated toll event

- Number of units navýší o sumu všech Number of units z jednotlivých seskupených Rated Toll Events.

<!-- -->

- Pokud Bill item neexistuje, Systém ho vytvoří:

  - Bill item category = Toll event.

  - Product type = podle hodnoty z PCRE

  - Bill item type = podle Toll transaction type, pokud

    - - 
      - 
      - 
    - 
    - 

  - je Toll transaction type = Rating a pokud je v aktuální session, pak Regular bill item, a pokud není v aktuální session a Price amount \>=0, pak Corrective bill item -- credit, a pokud není v aktuální session a Price amount \< 0, pak Corrective bill item -- debitje Toll transaction type = Cancelling, pak Corrective bill item -- creditje Toll transaction type = ReRating a pokud Price amount \>=0, pak Corrective bill item - debit, jinak Corrective bill item -- credit Price amount = podle RTE.price amount

  - Price amount VAT = podle RTE.price amount VAT

  - Unit price = podle RTE.unit price

  - Unit price VAT = podle RTE.unit price VAT

  - Number of units = podle RTE.number of units

  - Metric unit = podle RTE.metric unit

  - Discount amount = podle RTE.discount amount

  - Discount amount VAT= podle RTE.discount amount VAT

  - Discount rate = podle RTE.discount rate

  - Tax rate = podle RTE.tax rate

  - Billing service = podle RTE.billing service

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Pokud Systém nenašel Bill session a nejde o opoždenou nebo opětovně oceněnou nebo rušenou mýtnou událost, Systém [zaloguje chybu a]{.mark} nastaví stav Toll transaction na Rejected.

#### Poznámky

Nejsou

### Vytvoř výzvu na úhradu za přestupek (SYS.BAR.0.13.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování výzvy na úhradu za mýtnou transakci, která se přenastavila do stavu Offence.

#### Spuštění případu

V pravidelných intervalech na základě operace [BEm.CreateOffenceRfP.]{.mark}

#### Podmínky spuštění

Nejsou.

#### Normální postup

Systém vyhledá přestupky (tj. Unpaid Toll Transactions, které jsou ve stavu Offence).

Systém zpracovává jeden přestupek po druhém.

V případě, že je UTT bez účtu (tj. patří neregistrovanému provozovateli vozidla; tj. Subject type = Not registered), nebo že je UTT s účtem, ale patřící anonymnímu zákazníku (tj. VCM.Customer.anonymous registration = true), Systém se pokusí získat kontaktní adresu provozovatele vozidla z veřejných rejstříků na základě registrační značky vozidla a země registrace, za použití systémové funkce Získej data z EUCARIS (SYS.TDP.9.1).

- V případě, že nebyla nalezena žádná kontaktní adresa, Systém vystaví Offence RfP jako Simplified bill.

- V případě, že byla nalezena kontaktní adresa, Systém ji použije pro vygenerování Offence RfP jako fakturační adresu.

Systém vygeneruje RfP (HR business nazývá Formal Notice):

- Systém použije Bill issuer z UTT.

- Systém zjistí BIBA na základě Bill issuer a Reason = Offence.

- Systém naúčtuje zákonnou pokutu za přestupek, za použití systémové funkce užití Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR).

- Systém vytvoří Bill Item za zákonnou pokutu s parametry:

  - Bill item category = Penalty

  - Bill item type = Regular bill item

  - Unit price = podle RSE.unit price

  - Unit price VAT = podle RSE.unit price VAT

  - Number of units = podle RSE.number of units

  - Metric unit = podle RSE.metric unit

  - Tax rate = podle RSE.tax rate

  - Price amount = částka pokuty bez daně, tj. podle RSE.price amount

  - Price amount VAT = částka pokuty s daní, tj. podle RSE.price amount VAT

  - Billing service = podle RSE.billing service

- Systém pro Unpaid Toll Transaction a její Rated Toll Events vytvoří Bill Items:

  - Systém seskupí oceněné mýtné události podle:

    - Subject number (tj. Account nebo null),

    - Billing service,

    - Unit price VAT,

    - Unit price,

    - Tax rate,

    - Discount rate,

    - Basic unit price definition method,

    - Charge type,

  - Systém pro každou skupinu vytvoří Bill item s atributy:

    - Bill item category = Toll event

    - Product type = Toll

    - Bill item type = Regular

    - Price amount = podle RTE.price amount

    - Price amount VAT = podle RTE.price amount VAT

    - Unit price = podle RTE.unit price

    - Unit price VAT = podle RTE.unit price VAT

    - Number of units = podle RTE.number of units

    - Metric unit = podle RTE.metric unit

    - Discount amount = podle RTE.discount amount

    - Discount amount VAT= podle RTE.discount amount VAT

    - Discount rate = podle RTE.discount rate

    - Tax rate = podle RTE.tax rate

    - Billing service = podle RTE.billing service

Systém vytvoří vytvoří Bill s parametry:

- Bill number = Unikátní číslo faktury podle schématu z Číslování faktur v závislosti na Bill type, Bill issue type, Bill category a Bill issuer.

- Bill type = Request for payment (Offence RfP)

- Bill issue type =

  - Regular bill, pokud je známa fakturační adresa,

  - Simplified bill, pokud není známa fakturační adresa

- Bill recurrence type = One-time bill

- Bill category = Offence

- Bill issue status = Issued

- Bill payment status = Unpaid

- Comment = null

- Bill amount = součet bill items.price amount VAT

- Tax amount = null

- Total amount = součet bill items.price amount VAT

- Date of issue = aktuální datum

- Due date = sysdate

- [Date of beginning = aktuální datum]{.mark}

- [Date of end = aktuální datum]{.mark}

- Matched amount = 0

- Subject type = Toll transaction.Subject type

- Subject number = Toll transaction.Subject number

- Bill issuer bank account = zjištěná BIBA

- Bill issuer = Toll transaction.Bill issuer

Systém pro vozidlo vygeneruje (nebo zjistí pokud již existuje) PIN a vytvoří uživatelský účet pro přístup do Offence portálu, za použití systémové funkce Vygeneruj PIN pro přístup do Offence portálu ([SYS.AC.16.HR](http://sys.ac.16.hr/))

Systém spočítá dlužnou částku za předcházející neuhrazené Offences jako SUM(Bill.total amount-Bill.matched amount) všech již vystavených plně neuhrazených RfP (bez práve vystavovaného RfP) pro:

- danou SPZ, pokud je TT.subject type = Not registered,

- daný accountu, pokud je TT.subject type = Account.

Systém, vygeneruje dokument faktury v pdf formátu Výzva k úhradě za přestupky (DOC.BE.22.HR), s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém změní stav Unpaid Toll Transaction, která byla zahrnuta do Formálního oznámení, na „RfP generated".

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

### Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování jednorázové faktury za zaplacené Výzvy za zaplacení za přestupky.

#### Spuštění případu

Případ užití je vloženou součástí případů užití:

- Offence

  - Uhraď přestupek (UC.BAR.0.20.HR)

#### Podmínky spuštění

Je znám výčet zaplacených Request for Payments (a tudíž výčet jejich zaplacených Toll Transactions a jejich Rated Toll Events).

Je znám Account nebo Registrační značka vozidla, případně POS a informace o platbě.

#### Normální postup

Systém zjistí BIBA na základě Bill issuer a Reason = Offence.

Systém dohledá Rated Toll Events a Toll Transactions ze zaplacených Offence RfPs:

- Systém vytvoří kopie Rated Toll Events z Offence RfPs a vyplní na nich referenci na původni RTE.

- Systém na původních Rated Toll Events nastaví příznak Replaced = true, aby bylo zřejmé že jejich vazba na Toll Transaction je již neplatná.

- Systém seskupí dohledané oceněné mýtné události ze zaplacených TT a zkopírované oceněné mýtné události podle:

  - Subject number (tj. Account nebo null),

  - Billing service,

  - Unit price VAT,

  - Unit price,

  - Tax rate,

  - Discount rate,

  - Basic unit price definition method,

  - Charge type.

- Systém pro každou skupinu vytvoří Bill item s atributy:

  - Bill item category = Toll event

  - Product type = Toll

  - Bill item type = Regular

  - Price amount = součet seskupených RTE.price amount

  - Price amount VAT = součet seskupených RTE.price amount VAT

  - Unit price = podle RTE.unit price

  - Unit price VAT = podle RTE.unit price VAT

  - Number of units = součet seskupených RTE.number of units

  - Metric unit = podle RTE.metric unit

  - Discount amount = součet seskupených RTE.discount amount

  - Discount amount VAT= součet seskupených RTE.discount amount VAT

  - Discount rate = podle RTE.discount rate

  - Tax rate = podle RTE.tax rate

  - Billing service = podle RTE.billing service

Systém dohledá Rated Service Events ze zaplacených Offence RfPs:

- Systém zkopíruje Rated Service Events z Offence RfPs a vyplní na nových RSE referenci na původni RSE.

- Systém seskupí oceněné události podle:

  - Subject number (tj. Account nebo null),

  - Billing service,

  - Unit price VAT,

  - Unit price,

  - Tax rate,

  - Product type,

  - Basic unit price definition method,

  - Discount rate,

- Systém pro každou skupinu vytvoří Bill item s atributy:

  - Bill item category = Penalty.

  - Product type = podle RSE

  - Bill item type = Regular

  - Price amount = součet seskupených RSE.price amount

  - Price amount VAT = součet seskupených RSE.price amount VAT

  - Unit price = podle RSE.unit price

  - Unit price VAT = podle RSE.unit price VAT

  - Number of units = součet seskupených RSE.number of units

  - Metric unit = podle RSE.metric unit

  - Discount amount = součet seskupených RSE.discount amount

  - Discount amount VAT= součet seskupených RSE.discount amount VAT

  - Discount rate = podle RSE.discount rate

  - Tax rate = podle RSE.tax rate

  - Billing service = podle RSE.billing service

Systém pro každou tax rate vytvoří tax bill item:

- Bill item category = Tax

- Bill item type = Regular bill item

- Number of units = null

- Metric unit = null

- Tax rate = sazba daně (v procentech)

- [Price amount = celková daň za bill itemy s danou tax rate (Tax base \* Tax rate a zaokrouhlení na dvě desetinná místa)]{.mark}

- [Tax base = celková částka bez daně s danou tax rate (suma Price amount příslušných nedaňových bill items a zaokrouhlení na dvě desetinná místa)]{.mark}

Systém zjistí pro každou sazbu daně, zda není potřeba Rounding adjustment:

- Pokud rozdíl, daňové bill item.tax base a absolutní hodnoty součtu nedaňových bill item.price amount, není roven nule, Rounding adjustment bill iem se vytvoří s výsledkem rozdílu jako bill item.price amount

- Pokud rozdíl, (součtu daňové bill item.tax base a daňové bill item.price amount) a součtu nedaňových bill item.price amount VAT, není roven nule, Rounding adjustment bill iem se vytvoří, s výsledkem rozdílu jako bill item.price amount VAT

  - Systém vytvoří korekční bill item s parametry:

    - Bill item category = Rounding adjustment

    - Product type = null

    - Bill item type =

      - 
      - 

    - pokud vypočtený rozdíl je větší než 0, pak Corrective bill item -- credit, jinak Corrective bill item -- debit Basic unit price = absolutní hodnota vypočteného rozdílu

    - Basic unit price definition method = None

    - Unit price = Price amount

    - Unit price VAT = Price amount VAT

    - Number of units = 1

    - Metric unit = Piece

    - Tax rate = null

    - Price amount = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

    - Price amount VAT = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

    - Billing service = Systém zjistí billing service z PCRE na základě Billing service.abbreviation = ADJ-ROUNDING

V případě, že se jedná o zaplacení Offence RfPs, které všechny jsou bez účtu (tj. patří neregistrovanému provozovateli vozidla; tj. Subject type = Not registered), nebo patřící anonymnímu zákazníku (tj. VCM.Customer.anonymous registration = true), Systém se pokusí získat kontaktní adresu provozovatele vozidla z veřejných rejstříků na základě registrační značky vozidla a země registrace, za použití systémové funkce Získej data z EUCARIS (SYS.TDP.9.1):

- Pokud se podařily kontaktní údaje získat, použijí se pro generování dokumentu faktury.

- Pokud se nepodařily získat, Systém vygeneruje zjednodušenou fakturu bez kontaktních údajů (Simplified bill).

Systém vytvoří vytvoří Bill s parametry:

- Bill number = Unikátní číslo faktury podle schématu z Číslování faktur v závislosti na Bill type, Bill issue type, Bill category a Bill issuer.

- Fiscal verification number = vygeneruje se Fiskální verifikační číslo ze sekvence pro číslování faktur (BNF77) s Business Premises BO, určeným podle user profile

- ZKI = vyplní se Ochranný kód vystavitele faktury (Issuer\'s Protection Code)

- Bill type = Customer bill

- Bill issue type =

  - Regular bill, pokud je známa adresa pro fakturaci

  - jinak Simplified bill

- Bill recurrence type = One-time bill

- Bill category =

  - Offence, pokud faktura obsahuje RTE a RSE,

  - jinak Toll

- Bill issue status = Issued

- Bill payment status = Unpaid

- Comment = null

- Bill amount = součet daňových bill items.tax base

- Tax amount = součet daňových bill items.price amount

- Total amount = součet Bill amount a Tax amount (mělo by se rovnat součtu plateb, použitých na úhradu)

- Date of issue = aktuální datum

- Due date = aktuální datum

- [Date of beginning = aktuální datum]{.mark}

- [Date of end = aktuální datum]{.mark}

- Matched amount = 0

- Subject type = Toll transaction.Subject type (pokud alespoň jedno TT má subject type Account, použije se jako subject faktury)

- Subject number = Toll transaction.Subject number (pokud alespoň jedno TT má subject type Account, použije se jako subject faktury)

- Bill issuer bank account = zjištěná BIBA

- Bill issuer = Toll transaction.Bill issuer

Systém přenastaví na zaplacených Výzvách na úhradu:

- Bill issue status = Replaced

- Replaced by bill = reference na novou fakturu

- Matched amount = Total amount.

Systém informace o faktuře v XML formátu odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

Systém propíše Unique Invoice Identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

Pokud se případ užití spustil na POS (MEV, Kiosk, POS), Systém zjistí, zda se má dokument generovat ve variantě (DOC.BE.x) v případě A4 formátu [nebo (DOC.BE.x**B**) v případě thermo tisku na POS (podle POS.Printer type)]{.mark}.

Systém, s ohledem na zjištěnou variantu dokumentu, vygeneruje dokument faktury v pdf formátu Faktura za mýtné (DOC.BE.10.HR) v případě A4 formátu [nebo (DOC.BE.10B.HR) v případě thermo tisku]{.mark}, s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém zjistí, zda se má faktura vygenerovat také v xml formátu jako elektronická faktura (tj. pokud CM.Account.Preferred electronic invoice format = FINA).

V případě požadovaného XML formátu, Systém navíc vygeneruje eFakturu (DOC.BE.21.HR). Systém dokument uloží s využitím případu užití Ulož externí dokument (SYS.DFRP.1.4).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém případně updatuje Bill.E-Bill document = identifikátor vytvořeného XML dokumentu faktury.

Pokud vygenerování faktury proběhlo na POS (MEV, POS), Systém pdf dokument nabídne ke stažení.

Pokud vygenerování faktury proběhlo pro Kiosk, Systém dokument faktury nenabídne ke stažení, ale Kiosek vytiskne Doklad o zaplatení dlhu (DOC.KIO.05.HR).

Systém odešle pdf a případně XML verzi faktury na zákazníkův email společně s  notifikací Oznámení o vystavení faktury (NTF.BAR.21.HR).

Systém případně odešle XML verzi faktury přes eFINA přes Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR).

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou