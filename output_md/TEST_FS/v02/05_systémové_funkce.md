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