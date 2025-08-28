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
|                              | Vytvoř výzvy na úhradu za přestupky (SYS.BAR.0.13.HR)                      | *New*          | Systém          |
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
| Pomocné operace              | Stáhni kurzovní lístek Erste Bank (SYS.BAR.3.0)                            | *N/A*          | Systém          |
|                              | Stáhni kurzovní lístek Tatrabanky (SYS.BAR.3.1)                            | *N/A*          | Systém          |
|                              | Spočítej minimální částku top-up (SYS.BAR.3.2)                             | *N/A*          | Systém          |
|                              | Vytvoř finanční transakci (SYS.BAR.3.3.VO1)                                | *N/A*          | Systém          |
|                              |                                                                            |                |                 |
| Správa slev                  | Importuj nárok na slevu v doméně CZ (SYS.BAR.4.1)                          | *N/A*          | Systém          |

: Tabulka : Seznam systémových funkcí

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

- Bill session aggregation type = [Pre-paid]{.mark}, Post-paid card, [Post-paid invoice,]{.mark} Exemption partner, [Fleet card issuer]{.mark} a EETS Provider,

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

    - Pokud součet Tax base všech daňových Bill item a Price amount všech daňových Bill items \>= 0,

      - a pokud vypočtený rozdíl je menší než nula, pak Corrective bill item -- credit,

      - jinak Corrective bill item -- debit

    - Pokud součet Tax base všech daňových Bill item a Price amount všech daňových Bill items \< 0,

      - A pokud vypočtený rozdíl je větší než nula, pak Corrective bill item -- credit,

      - jinak Corrective bill item -- debit

        - Unit price = Price amount

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

    - Customer bill pokud Bill session aggregation type = [Pre-paid,]{.mark} Post-paid card, [Postpaid invoice]{.mark},

    - EETS Provider bill, pokud Bill session aggregation type = EETS Provider

    - Exemption partner bill, pokud Bill session aggregation type = Exemption partner

    - [Fleet card issuer bill, pokud Bill session aggregation type = Fleet card issuer]{.mark}

  - Date of issue = systémové datum

  - Date of beginning = Bill session.Bill period start

  - Date of end = Bill session.Bill period end

  - Matched amount = 0

- 

- [Systém vypočítá termíny splatnosti (Bill Due date)]{.mark}

  - [pro fakturu a vrubopis tak, že k Bill Date of issue přičte hodnotu Maturity period z příslušného Účtu, případně]{.mark} [příslušné specializace Business partnera.]{.mark}

  - [pro EETS dobropis tak, že k Bill Date of issue přičte hodnotu Maturity period for credit note z příslušného Poskytovatele mýtných služeb,]{.mark}

  - [pro jiný dobropis tak, že k Bill Date of issue přičte hodnotu z konfiguračního klíče BE_Maturity period for customer credit note.]{.mark}

- 

- Systém vytvoří statistiku fakturační dávky.

Systém nastaví Bill status na **Waiting for print** a postupně provádí následující fakturační kroky:

- Systém informace o faktuře v ePorezna formátu (XML) odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

- Systém propíše Unique invoice identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

- [Systém zjistí]{.mark} [preferovaný]{.mark} [jazyk faktury Účtu nebo]{.mark} [příslušné specializace Business partnera]{.mark} [(např.]{.mark} [Poskytovatele EETS]{.mark} [nebo FCI nebo Exemption partnera)]{.mark} [(tj. ze Account.Preferred document language nebo]{.mark} [Business partner.Preferred document language).]{.mark}

- Systém vygeneruje podle bill type, bill issue type a bill category všechny dokumenty faktur, vrubopisů případně dobropisů s ohledem [na zjištěný preferovaný jazyk]{.mark} v pdf formátu za využití systémoveé funkce Vytvoř a ulož dokument (SYS.DFRP.1.1):

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

Cílem tohoto případu užití je vygenerování jednorázové faktury za naúčtované jednorázové poplatky nebo za provedený Top-up.

#### Spuštění případu

Případ užití je vloženou součástí případů užití:

- Top-up

  - Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

- [OBU,]{.mark} [Products]{.mark}

  - [TBD]{.mark}

- [Záporný kredit]{.mark}

  - [Ukonči předplacený účet (UC.CM.4.15)]{.mark}

#### Podmínky spuštění

Pro daný Account, pro které je potřeba vystavit fakturu, je na vstupu:

- identifikace Accountu

- oceněná událost (včetné počtu jednotek),

- Bill issuer,

- info o POS (pokud je to relevantní)

- informace o platbě (pokud je informace o platbě prázdná, jde o vystavení Proforma faktury)

<!-- -->

- pokud se jedná o Top-up, je známa částka platby

- pokud se jedná o prodej OBU, jsou [známy]{.mark} [čísla prodaných OBU]{.mark} [(OBU Serial number).]{.mark}

Poznámka: Pro FCI, EETS Provider a Exemption partner není aktuálně UC potřeba realizovat.

#### Normální postup

Systém zjistí BIBA:

- pro Top-up z Payment.BIBA (tj. na základě Bill issuer a Reason = Top-up)

- jinak na základě Bill issuer a Reason = Services.

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

- Price amount VAT = částka platby

- Billing service = PCRE.billing service

- Number of units corrected = null

- Cancellable = True

- Subject type = Account, pokud na vstupu je identifikace Account

- Subject number = ze vstupu

- Bill issuer = ze vstupu

- [FCI partner = FCI karty]{.mark} [v případě platby]{.mark} [tankovací]{.mark} [kartou]{.mark}

- [Fleet Card Number = Číslo tankovací karty v případě platby]{.mark} [tankovací]{.mark} [kartou]{.mark}

- [Fleet Card Id = Id tankovací karty v případě platby]{.mark} [tankovací]{.mark} [kartou]{.mark}

Pokud nejde o Top-up, Systém na základě každé oceněné události ze vstupu naúčtuje jednorázový poplatek za použití systémové funkce Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR).

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

  - 

  - [pokud jde o Fleet card issuer, pak FCI bill]{.mark}

  - [pokud jde o Exemption partner, pak Exemption partner bill]{.mark}

  - [pokud jde o]{.mark} [subjecte type =]{.mark} [EETS Provider, pak EETS Provider bill]{.mark}

- Bill category =

  - OBU, pokud Bill item category = OBU event,

  - Services, pokud Bill item category = Service Event,

  - Top-up, pokud Bill item category = Top-up event.

- Bill issue type =

  - Proforma bill, pokud neexistuje platba pro danou operaci,

  - Advance bill, pokud Bill category = Top-up,

  - else Regular bill.

- Bill recurrence type = One-time bill

- Bill issue status = Issued

- Bill payment status = Unpaid

- Comment = null

- Bill amount = součet daňových bill items.tax base

- Tax amount = součet daňových bill items.price amount

- Total amount = součet Bill amount a Tax amount

- Date of issue = aktuální datum

- Due date = se vypočte tak, že k Bill Date of issue se přičte hodnota Maturity period z příslušného Účtu, [případně]{.mark} [z]{.mark} [Provider EETS, případně]{.mark} [z]{.mark} [Exemption partner, případně]{.mark} [z]{.mark} [FCI]{.mark}.

- Date of beginning = aktuální datum

- Date of end = aktuální datum

- Matched amount = 0

- Subject type = Subject type z RSE

- Subject number = Subject number z RSE

- Bill issuer bank account = zjištěné číslo bankovního účtu Bill issuera (BIBA)

- Bill issuer = Bill issuer ze vstupu

Pokud se nejedná o Proforma bill, Systém informace o faktuře v XML formátu odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

Systém propíše Unique Invoice Identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

[Systém zjistí jazyk faktury Účtu nebo Poskytovatele EETS (tj. ze Account.Preferred document language nebo EETS Provider.Preferred document language).]{.mark}

Pokud se případ užití spustil na POS (MEV, Kiosk, POS),

Systém zjistí, zda se má dokument generovat ve variantě (DOC.BE.x) v případě A4 formátu nebo (DOC.BE.x**B**) v případě thermo tisku na POS (podle POS.Printer type).

Systém, s ohledem na [zjištěný preferovaný jazyk,]{.mark} na zjištěnou variantu dokumentu, vygeneruje dokument faktury v pdf formátu:

- Pokud jde o bill category = Top-up, pak Zálohová faktura za top-up (DOC.BE.1.HR) v případě A4 formátu, nebo (DOC.BE.1B.HR) v případě thermo tisku

- pokud jde o bill issue type = Proforma bill, pak Proforma faktura (DOC.BE.24.HR),

- jinak (Faktura za služby (DOC.BE.16.HR),

s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém zjistí, zda se má faktura vygenerovat také v xml formátu jako elektronická faktura (tj. pokud CM.Account.Preferred electronic invoice format = FINA, [nebo ECM.EETS Provider.Preferred electronic invoice format = FINA, nebo CM.Exemption partner.Preferred electronic invoice format = FINA)]{.mark}.

V případě požadovaného XML formátu, Systém navíc vygeneruje eFakturu (DOC.BE.21.HR). Systém dokument uloží s využitím případu užití Ulož externí dokument (SYS.DFRP.1.4).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém případně updatuje Bill.E-Bill document = identifikátor vytvořeného XML dokumentu faktury.

[Pokud vygenerování faktury proběhlo na žádost DU, Systém odešle do DU identifikaci vzniklé faktury.]{.mark}

Pokud vygenerování faktury proběhlo pro POS (MEV, Kiosk, POS), Systém dokument nabídne ke stažení.

Systém odešle pdf a případně XML verzi faktury na zákazníkův email [případně email Poskytovatele mýtných služeb]{.mark} společně s notifikací:

- Oznámení o vystavení faktury za předplacení kreditu (NTF.BAR.01.HR), pokud jde o Top-up

- jinak Oznámení o vystavení faktury (NTF.BAR.21.HR).

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

- Bill session aggregation type = Post-paid card, [Post-paid invoice]{.mark}, EETS Provider, Exemption partner, [Fleet card issuer, Pre-paid]{.mark}

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

[pro Post-paid Invoice a]{.mark} [Toll]{.mark}

- [Bill session aggregation type = Post-paid Invoice]{.mark}

- [Bill session content type = Toll]{.mark}

- [Bill cycle = Month (agregace podle hodnoty atributu Bill cycle na Account)]{.mark}

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

[pro]{.mark} [Fleet card issuer a]{.mark} [Toll]{.mark}

- [Bill session aggregation type = Exemption partner]{.mark}

- [Bill session content type = Toll]{.mark}

- [Bill cycle = 15-days, Month (agregace podle hodnoty atributu Bill cycle na VCM.Exemption partner)]{.mark}

[pro Pre-paid]{.mark} [a]{.mark} [Toll]{.mark}

- [Bill session aggregation type =]{.mark} [Pre-paid]{.mark}

- [Bill session content type = Toll]{.mark}

- [Bill cycle = Month (agregace podle hodnoty atributu Bill cycle na Account)]{.mark}

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

- UCs vyžadující Administrativní poplatek za Přestupek (Offence)

  - Vytvoř výzvy na úhradu za přestupky (SYS.BAR.0.13.HR)

  - Vytvoř jednorázovou fakturu za mýto (SYS.BAR.14.HR)

- [UC vyžadující Poplatek za odeslání OBU poštou]{.mark}

  - [Zjisti počty zásilek pro naúčtování poplatků za zaslání OBU (SYS.CM.7.38)]{.mark}

  - 

#### Podmínky spuštění

Je znám Bill issuer, typ poplatku [nebo poplatků]{.mark}, který je potřeba vygenerovat (tj. Product type a odpovídající hodnotu Event attribute type), počet jednotek a subjekt (případně subjekt type):

- Administrative fee za Offence:

  - Product type = DF (Dunning fee) + hodnota event atributu type = Chargeable service ze vstupu (i.e. Offence fee[, MEV fee]{.mark}),

  - Počet jednotek

  - Info o subjektu

  - Bill issuer

- [OBU:]{.mark}

  - [Product type =]{.mark} [OBU]{.mark} [+ pro event atribut type]{.mark} [= Chargeable service, jeho hodnota = OBU]{.mark} [fee,]{.mark}

  - [Počet jednotek]{.mark}

  - [Info o subjektu]{.mark}

  - [případně info o Fleet card, pokud jde o platbu]{.mark} [fleet card]{.mark}

  - [Bill issuer]{.mark}

- [OBU sending:]{.mark}

  - [Product type =]{.mark} [OBU nebo ?Chargeable services + pro event atribut type]{.mark} [= Chargeable service, jeho hodnota = OBU]{.mark} [sending]{.mark} [fee,]{.mark}

  - [je znám vypočítaný počet zásilek]{.mark}

  - [Info o subjektu]{.mark}

  - [případně info o Fleet card, pokud jde o platbu fleet card]{.mark}

  - [Bill issuer]{.mark}

Poplatky v jednom volání mohou vycházet jen z jednoho Product type.

Poznámka: Pro FCI, EETS Provider a Exemption partner není aktuálně UC potřeba realizovat.

#### Normální postup

[Systém]{.mark} [zjistí BIBA na základě Bill issuera ze vstupu]{.mark} [a Reason = Services.]{.mark}

- 

Administrativní poplatek za Offence

Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů

- Bill issuer, [Bill issuer currency, Bill issuer VAT registration country,]{.mark}

- [VAT registration country zákazníka, VAT registration country zákazníka]{.mark},

- Product type = Dunning fee + hodnota event atributu typu = Chargeable service ze vstupu (i.e. Offence fee nebo MEV fee),

za použití systémové funkce Oceň produkt (SYS.PCRE.1.4.HR).

Postup pokračuje krokem **Společný postup pro všechny poplatky** s Number of units = počet Offences daného Bill issuer.

[Poplatek za zaslání OBU]{.mark}

[Systém pro požadovaný typ poplatku, zjistí jeho částku na základě kombinace atributů]{.mark}

- [Bill issuer, Bill issuer currency, Bill issuer VAT registration country,]{.mark}

- [VAT registration country zákazníka, VAT registration country zákazníka,]{.mark}

- [Product type =]{.mark} [Chargeable service]{.mark} [+ hodnota event atributu typu = Chargeable service ze vstupu (i.e.]{.mark} [OBU sending fee),]{.mark}

[za použití případu užití Oceň produkt (SYS.PCRE.1.4).]{.mark}

[Postup pokračuje krokem **Společný postup pro všechny poplatky**]{.mark} [s]{.mark} [Number of units = spočítaný počet zásilek.]{.mark}

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

Jde o Toll Transaction s Registration type = EETS, Exempted, Exempted not compliant nebo Exempted trip, nebo jde o Post-paid card registration type po úspěšné platbě kartou

Rated toll event ještě není agregován do Bill session.

#### Popis

Systém na základě nastavení VCM.Exemption partner, VCM.Account nebo ECM.EETS Provider, vyhledá Bill session, která odpovídá podmínkám:

- Pro Subject type = Account a Registration type = Post-paid invoice:

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Post-paid invoice

  - VCM.Account.bill cycle platný v době event time = Bill session.bill cycle

  - Bill session content type = Toll

- Pro Subject type = Account a Registration type = Post-paid card (po úspěšné platbě):

  - Toll transaction.event time spadá do intervalu Bill session

  - Bill session.bill session aggregation type = Post-paid card

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

  - Customer bill, pokud Bill session.bill session aggregation type = Post-paid card nebo Post-paid invoice

  - EETS Provider bill, pokud Subjekt type = EETS Provider

  - Exemption partner bill, pokud Subjekt type = Exemption partner

- Bill recurrence type = Periodical bill

- Bill category = Toll

- Bill issue status = In progress

- Bill payment status =

  - Payment not needed, pokud jde o Bill session.bill session aggregation type = Post-paid card (tj. po úspěšné platbě kartou (SYS.BAR.1.10.HR)

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

- Card number (jen pro Bill session.bill session aggregation type = Post-paid card),

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

    - je Toll transaction type = Rating

      - a pokud je v aktuální session, pak Regular bill item,

      - a pokud není v aktuální session a Price amount \>=0, pak Corrective bill item -- credit,

      - a pokud není v aktuální session a Price amount \< 0, pak Corrective bill item -- debit

    - je Toll transaction type = Cancelling, pak Corrective bill item -- credit

    - je Toll transaction type = ReRating a pokud Price amount \>=0, pak Corrective bill item - debit, jinak Corrective bill item -- credit

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

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Pokud Systém nenašel Bill session a nejde o opoždenou nebo opětovně oceněnou nebo rušenou mýtnou událost, Systém [zaloguje chybu a]{.mark} nastaví stav Toll transaction na Rejected.

#### Poznámky

Nejsou

### Vytvoř výzvy na úhradu za přestupky (SYS.BAR.0.13.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování výzev na úhradu za mýtné transakce, od jejichž zprocesování uběhlo déle než určitá doba.

#### Spuštění případu

V pravidelných intervalech na základě naplánované operace BEm.OffenceRfP.

#### Podmínky spuštění

Nejsou.

#### Normální postup

Systém vyhledá přestupky, od jejichž přepnutí do stavu Offence uběhlo déle než je časové období nakonfigurované v daném konfiguračním klíči (tj. (Unpaid Toll Transactions, které jsou ve stavu Offence, kdy rozdíl dnů mezi Sysdate a UTT.Offence time \>= BE_DaysPriorOffencesRfPCreation).

Systém seskupí nalezené nezaplacené mýtné transakce podle:

- Registration number,

- Registration country,

- Account (pokud je znám, jinak null).

V případě, že je skupina UTT bez účtu (tj. patří neregistrovanému provozovateli vozidla; tj. Subject type = Not registered), nebo že je skupina UTT s účtem, ale patřící anonymnímu zákazníku (tj. VCM.Customer.anonymous registration = true), Systém se pokusí získat kontaktní adresu provozovatele vozidla z veřejných rejstříků na základě registrační značky vozidla a země registrace, za použití systémové funkce Získej data z EUCARIS (SYS.TDP.9.1):

- V případě, že nebyla nalezena žádná kontaktní adresa, Systém takovéto nezaplacené mýtné transakce odfiltruje a tento proces generování Offence RfP pro ně, pro tento běh, končí.

- V případě, že byla nalezena kontaktní adresa, Systém ji použije pro vygenerování Offence RfP jako fakturační adresu.

Systém rozdělí seskupené UTT podle Bill isser a zjistí počet přestupků.

Systém vygeneruje RfP (HR business nazývá Formal Notice) pro každou skupinu Unpaid Toll Transactions (tj. pokud má účet vozidlo se 3 neuhrazenými mýtnými transakcemi, z nichž každá patří jinému Bill issuer, vygenerují se 3 Offence RfPs -- jedno pro každého Bill issuer, přičemž každé obsahuje odpovídající UTT a odpovídající administrativní poplatek):

- Systém zjistí BIBA na základě Bill issuer a Reason = Offence.

- Systém naúčtuje administrativní poplatek za každou nezaplacenou mýtnou transakci Bill issuera, za použití systémové funkce užití Naúčtuj jednorázový poplatek (SYS.BAR.0.7.HR).

- Systém seskupí oceněné události za administrativní poplatek podle atributů Rated Service Events:

  - Subject number (tj. Account nebo null),

  - Billing service,

  - Unit price VAT,

  - Unit price,

  - Tax rate,

  - Product type,

  - Basic unit price definition method,

  - Discount rate.

- A pro každou kombinaci vytvoří Bill Item s parametry:

  - Bill item category = Dunning fee

  - Bill item type = Regular bill item

  - Unit price = Unit price z RSE

  - Unit price VAT = Unit price VAT z RSE

  - Number of units = součet z Number of units RSE

  - Metric unit = Piece

  - Tax rate = Tax rate z RSE

  - Price amount = částka poplatků bez daně, tj. součet z Price amount z RSE

  - Price amount VAT = částka poplatků s daní, tj. součet z Price amount VAT z RSE

  - Billing service = Billing service z RSE

- Systém pro každou skupinu Unpaid Toll Transactions a jejich Rated Toll Events vytvoří Bill Items:

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

Systém vytvoří vytvoří Bill s parametry:

- Bill number = Unikátní číslo faktury podle schématu z Číslování faktur v závislosti na Bill type, Bill issue type, Bill category a Bill issuer.

- Bill type = Request for payment (Offence RfP)

- Bill issue type = Regular bill

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

[Systém zjistí jazyk faktury Účtu (tj. ze Account.Preferred document language nebo EETS Provider.Preferred document language).]{.mark}

Systém, s ohledem na [zjištěný preferovaný jazyk,]{.mark} vygeneruje dokument faktury v pdf formátu Výzva k úhradě za přestupky (DOC.BE.22.HR), s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém změní stav Unpaid Toll Transactions, které byly zahrnuty do Formálního oznámení, na „RfP generated" (nebudou se již samostatně zobrazovat na Offence portálu jako samostatné Offences.

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

### Vytvoř jednorázovou fakturu za mýto (SYS.BAR.0.14.HR)

#### Cíl

Cílem tohoto případu užití je vygenerování jednorázové faktury za zaplacené Přestupky nebo Výzvy za zaplacení za přestupky.

#### Spuštění případu

Případ užití je vloženou součástí případů užití:

- Offence

  - Uhraď přestupek (UC.BAR.0.20.HR)

#### Podmínky spuštění

Je znám výčet zaplacených Toll Transactions, jejich Rated Toll Events a případně výčet Request for Payments (a tudíž výčet jejich zaplacených Toll Transactions a jejich Rated Toll Events).

Je znám Account nebo Registrační značka vozidla, případně POS a informace o platbě.

#### Normální postup

Systém zjistí BIBA na základě Bill issuer a Reason = Offence.

Systém dohledá Rated Toll Events zaplacených Toll Transactions a Toll Transactions ze zaplacených Offence RfPs:

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

  - [Card number = maskované číslo platební karty použité pro platbu (pokud je na vstupu)]{.mark}

Pokud jde o zaplacení Offence RfPs s naúčtovanými administrativními poplatky:

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

  - Bill item category = Dunning fee.

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

  - [Card number = maskované číslo platební karty použité pro platbu (pokud je na vstupu)]{.mark}

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

      - pokud vypočtený rozdíl je větší než 0, pak Corrective bill item -- credit,

      - jinak Corrective bill item -- debit

    - Basic unit price = absolutní hodnota vypočteného rozdílu

    - Basic unit price definition method = None

    - Unit price = Price amount

    - Unit price VAT = Price amount VAT

    - Number of units = 1

    - Metric unit = Piece

    - Tax rate = null

    - Price amount = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

    - Price amount VAT = podle výsledku výpočtu, buď absolutní hodnota rozdílu, jinak null

    - Billing service = Systém zjistí billing service z PCRE na základě Billing service.abbreviation = ADJ-ROUNDING

V případě, že se jedná o zaplacení skupiny UTT nebo Offence RfP, které všechny jsou bez účtu (tj. patří neregistrovanému provozovateli vozidla; tj. Subject type = Not registered), nebo patřící anonymnímu zákazníku (tj. VCM.Customer.anonymous registration = true), Systém se pokusí získat kontaktní adresu provozovatele vozidla z veřejných rejstříků na základě registrační značky vozidla a země registrace, za použití systémové funkce Získej data z EUCARIS (SYS.TDP.9.1):

- Pokud se podařily kontaktní údaje získat, použijí se pro generování dokumentu faktury.

- Pokud se nepodařily získat, Systém vygeneruje zjednodušenou fakturu bez kontaktních údajů.

Systém vytvoří vytvoří Bill s parametry:

- Bill number = Unikátní číslo faktury podle schématu z Číslování faktur v závislosti na Bill type, Bill issue type, Bill category a Bill issuer.

- Fiscal verification number = vygeneruje se Fiskální verifikační číslo ze sekvence pro číslování faktur (BNF77) s Business Premises BO, určeným podle user profile

- ZKI = vyplní se Ochranný kód vystavitele faktury (Issuer\'s Protection Code)

- Bill type = Customer bill

- Bill issue type =

  - Regular bill, pokud je známa adresa pro fakturaci

  - [jinak Simplified bill]{.mark}

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

- Due date = sysdate

- [Date of beginning = aktuální datum]{.mark}

- [Date of end = aktuální datum]{.mark}

- Matched amount = 0

- Subject type = Toll transaction.Subject type (pokud alespoň jedno TT má subject type Account, použije se jako subject faktury)

- Subject number = Toll transaction.Subject number (pokud alespoň jedno TT má subject type Account, použije se jako subject faktury)

- Bill issuer bank account = zjištěná BIBA

- Bill issuer = Toll transaction.Bill issuer

Pokud jde o zaplacení RfPs

:

Systém přenastaví na zaplacených Výzvách na úhradu:

- Bill issue status = Replaced

- Replaced by bill = reference na novou fakturu.

Systém informace o faktuře v XML formátu odešle do ePorezna na fiskalizaci (Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR). 

Systém propíše Unique Invoice Identifier (JIR) z ePorezna odpovědi do Bill.JIR atributu.

[Systém zjistí jazyk faktury Účtu nebo Poskytovatele EETS (tj. ze Account.Preferred document language nebo EETS Provider.Preferred document language).]{.mark}

Pokud se případ užití spustil na POS (MEV, Kiosk, POS), Systém zjistí, zda se má dokument generovat ve variantě (DOC.BE.x) v případě A4 formátu nebo (DOC.BE.x**B**) v případě thermo tisku na POS (podle POS.Printer type).

Systém, s ohledem na [zjištěný preferovaný jazyk,]{.mark} na zjištěnou variantu dokumentu, vygeneruje dokument faktury v pdf formátu Faktura za mýtné (DOC.BE.10.HR) v případě A4 formátu nebo (DOC.BE.10B.HR) v případě thermo tisku, s využitím případu užití Vytvoř a ulož dokument (SYS.DFRP.1.1).

Systém zjistí, zda se má faktura vygenerovat také v xml formátu jako elektronická faktura (tj. pokud CM.Account.Preferred electronic invoice format = FINA).

V případě požadovaného XML formátu, Systém navíc vygeneruje eFakturu (DOC.BE.21.HR). Systém dokument uloží s využitím případu užití Ulož externí dokument (SYS.DFRP.1.4).

Systém updatuje na Bill.Bill document = identifikátor vygenerovaného PDF dokumentu faktury.

Systém případně updatuje Bill.E-Bill document = identifikátor vytvořeného XML dokumentu faktury.

Pokud vygenerování faktury proběhlo na POS (MEV, Kiosk, POS), Systém pdf dokument nabídne ke stažení.

Systém odešle pdf a případně XML verzi faktury na zákazníkův email společně s  notifikací Oznámení o vystavení faktury (NTF.BAR.21.HR).

Systém případně odešle XML verzi faktury přes eFINA přes Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR).

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

## Zpracování mýtných transakcí

### Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR) 

#### Cíl

Cílem tohoto případu užití je pro oceněný průjezd mýtnou trasou vytvořit mýtnou transakci (unpaid Toll Transaction nebo Toll Transaction), odpovídající oceněnou mýtnou událost (Rated toll event) a případně je zagregovat do Bill session.

#### Spuštění případu

Případ užití je vloženou součástí následujících případů užití:

- Odešli oceněnou mýtnou transakci (SYS.VTP.2.5)

#### Podmínky spuštění

Toll Trip Record byl oceněn.

Pro oceněný Toll Trip Record s Registration type \<\> Not registered, vždy na vstupu bude buď identifikace VCM.Account nebo ECM.EETS Provider nebo VCM.Exemption partner [nebo VCM.Fleet card issuer]{.mark}.

Poznámka: U Toll Trip Record s Exempted trip registration type, bude na vstupu buď jedna transakce nebo dvě transakce, pokud byla zjištěna jiná kategorie vozidla než na kterou se vztahuje osvobození. V případě dvou transakcí, obě budou odkazovat na jeden VTP.Toll Trip Record:

- vždy se pošle na uložení transakce s Exempted trip registration type,

- případně také transakce s registration type určenou podle vozidla (tj. EETS, Pre-paid, Post-paid invoice, Post-paid card, Not registered) na částku nad rámec částky osvobozeného průjezdu.

#### Popis

Pre-paid registration type

U Toll Trip Record s Pre-paid registration type, vždy na vstupu bude informace (Toll Trip Record.is covered by Pre-paid balance), zda byla celková částka za průjezd stržena z Pre-paid balance nebo bylo zjištěno, že zůstatek není dostatečný.

Pokud byla celková částka za průjezd stržena z Pre-paid balance (tj. Toll Trip Record.is covered by Pre-paid balance = true), Systém vytvoří Toll transaction a odpovídající Rated toll event a postup končí.

Pokud nebyla celková částka za průjezd stržena z Pre-paid balance, protože zůstatek nebyl dostatečný (tj. Toll Trip Record.is covered by Pre-paid balance =false),

- Systém vytvoří Unpaid Toll Transaction ve stavu Offence a odpovídající Rated Toll Event.

- Systém informuje zákazníka o neúspěšném zaplacení mýtné transakce pomocí notifikace (**NTF.**BAR**.**13.HR nebo **NTF.**BAR**.**14.HR) a postup končí.

- Systém přidá vozidlo na Alert list

- [Agregace/DI to ERP?]{.mark}

Post-paid card registration type

Systém vytvoří Unpaid Toll Transaction ve stavu Ready for processing, odpovídající Rated Toll Event a odpovídající Card Payment Request, a postup končí.

Poznámka: Následně proces pokračuje zaplacením mýtné transakce za užití systémové funkce Zaplať mýtnou transakci (SYS.BAR.1.10.HR)

Post-paid invoice registration type

Systém vytvoří Toll transaction a odpovídající Rated toll event.

Systém zagreguje Rated toll event do Bill session pro Post-paid, kdy Bill bude s Bill payment status = Unpaid za použití systémové funkce Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) a postup končí.

EETS registration type

Systém vytvoří Toll transaction a odpovídající Rated toll event.

Systém zagreguje Rated toll event do Bill session pro EETS za použití systémové funkce Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) a postup končí.

Poznámka: Následně proces pokračuje vytvořením Billing details za užití systémové funkce Vytvoř billing details (SYS.BAR.1.9.HR).

Not registered registration type

Systém vytvoří Unpaid Toll Transaction ve stavu Offence a odpovídající Rated Toll Event a postup končí.

Exempted registration type

Systém vytvoří Toll transaction a odpovídající Rated toll event.

Systém zagreguje Ratel toll event do Bill session pro Exemption partner se subjektem = Exemption partner odpovídající dané kategorii osvobození za použití systémové funkce Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR).

Poznámka 1: Pokud žádný VCM.Exemption partner nebude definován pro dané osvobození, pak nikdo osvobození nebude kompenzovat a takovéto oceněné Toll TripRecords se do BAR ani nepošlou.

Poznámka 2: Subjektem Toll Transaction bude Exemption partner, ale bude vyplněna reference na Vehicle nebo EETS Vehicle, aby bylo zřejmé, kdo mýtnou trasu projel.

Exempted **trip** registration type

Systém vytvoří Toll Transaction a odpovídající Rated Toll Event.

System zagreguje Rated Toll Event do Bill session pro Exemption partner se subjektem = Exemption partner odpovídající dané kategorii osvobození za použití systémové funkce Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR) a postup končí.

Poznámka: Subjektem Toll Transaction bude Exemption partner, ale bude vyplněna reference na Vehicle nebo EETS Vehicle, aby bylo zřejmé, kdo mýtnou trasu projel.

- 

[Exempted not compliant registration type]{.mark}

[Systém vytvoří Toll transaction a odpovídající Rated toll event.]{.mark}

[Systém zagreguje Ratel toll event do Bill session pro Exemption partner se subjektem = Exemption partner odpovídající dané kategorii osvobození, nebo do Bill session pro Post-paid se subjektem = Account (tj.]{.mark} [podle příslušnosti vozidla) za použití systémové funkce Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR).]{.mark}

[Poznámka: Subjektem Toll Transaction bude Exemption partner, ale bude vyplněna reference na Vehicle nebo EETS Vehicle, aby bylo zřejmé, kdo mýtnou trasu projel.]{.mark}

- 

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Vytvoření Unpaid Toll Transaction a Rated Toll Event,

pokud jde o Registration type = Post-paid card, Pre-paid (v případě nedostatečného zůstatku) nebo Not registered:

Systém na základě údajů ze vstupu vytvoří Unpaid Toll Transaction:

- Toll transaction type = ze vstupu

  - 0 = Rating (send)

  - [1 = Cancelling (revoke)]{.mark}

  - [3 = Rerating (adjust)]{.mark}

- Unpaid toll transaction status =

  - Ready for processing, v případě že jde o Post-paid card registration type

  - Offence, v případě že jde o Pre-paid bez dostatečného zůstatku, nebo Not registered registration type

- Vehicle category = ze vstupu

- Emission class = ze vstupu

- Emission class CO2= ze vstupu

- Registration number = ze vstupu

- Registration country = ze vstupu

- OBU serial number = ze vstupu

- OBU assignment status = ze vstupu

- Event time = ze vstupu

- Offence time = sysdate time pokud status je Offence, jinak null

- Creation time = sysdate time

- Agregation time = null

- Discount applied = pokud Unpaid toll transaction status = Offence, pak false, jinak true.

- Transaction amount = suma (Rated Toll Event.Price amount)

- Transaction amount VAT = suma (Rated Toll Event.Price amount VAT)

- Transaction discount amount =

  - pokud Discount applied = false a alespoň jeden Rated toll event.Discount rate \<\>0, pak 0, jinak null.

  - pokud Discount applied = true, je to součet slev (tj. suma (Rated Toll Event.Discount amount))

- Transaction discount amount VAT =

  - pokud Discount applied = false a alespoň jeden Rated toll event.Discount rate \<\>0, pak 0, jinak null.

  - pokud Discount applied = true, je to součet slev s daní (tj. suma (Rated Toll Event.Discount amount VAT))

- Transaction discount rate = Rated Toll Event.Discount rate (z první RTE)

- Vehicle = ze vstupu

- EETS vehicle = ze vstupu

- Subject type = ze vstupu

- Subject number = ze vstupu

- Original toll transaction = ze vstupu

- Cancelled = false

- Registration type = ze vstupu

  - Post-paid card

  - Pre-paid (v případě nedostatečného zůstatku)

  - Not registered

- Toll trip record = ze vstupu

- Toll trip = ze vstupu

- Bill issuer = ze vstupu (tj. System operator)

Systém pro každou oceněnou složku mýta události zpoplatnění vytvoří Rated toll event:

- Charge type = ze vstupu

- Basic unit price = ze vstupu

- Basic unit price definition method = ze vstupu

- Unit price = ze vstupu

- Unit price VAT = ze vstupu

- Number of units = ze vstupu

- Metric unit = ze vstupu

- Price amount =

  - pokud Discount applied = false, pak Price amount ze vstupu,

  - jinak Price amount ze vstupu -- Discount amount

- Price amount VAT =

  - pokud Discount applied = false, pak Price amount VAT ze vstupu,

  - jinak Price amount VAT ze vstupu -- Discount amount VAT

- Tax rate = ze vstupu

- Discount amount = ze vstupu

- Discount amount VAT = ze vstupu

- Discount rate = ze vstupu

- Billing service = ze vstupu

- Unpaid toll transaction = reference na Unpaid Toll Transaction

Vytvoření Card Payment Request,

pokud jde o Registration type = Post-paid card:

Systém vytvoří Card Payment request:

- Attempt count = 0

- Created on = aktuální datum a čas

- Process on = budoucí datum a čas, kdy se má záznam zprocesovat

- Unpaid toll transaction = reference na nově vytvořený Unpaid toll transaction

Vytvoření a odeslání notifikace,

pokud jde o Registration type = Pre-paid v případě nedostatečného zůstatku.

Systém zjistí zda existuje vyplněný kontakt (na VT Vehicle, pokud tam není tak na VT Account, pokud tam neni tak na VT Customer). Pokud je vyplněn:

- E-mail address, Systém vygeneruje emailovou notifikaci (NTF.BAR.13.HR) a odešle ji.

- [Phone number, Systém vygeneruje SMS notifikaci (NTF.BAR.14.HR) a odešle ji.]{.mark}

Přidání na Alert list,

pokud jde o Registration type = Pre-paid v případě nedostatečného zůstatku (tj. jakmile se UTT přenastaví do stavu Offence).

Systém na základě nezaplacené mýtné transakce vytvoří nebo updatuje záznam na Alert listu pro dané SPZ, navýší Total due amount o celkovou nezaplacenou částku transakce a Offence count navýší o 1 přestupek, za použití systémové funkce Zaeviduj Offence na Alert list (SYS.TDP.5.6):

- UTT.Registration number a UTT.Registration country

- Bill.Bill issuer

- Unpaid toll transaction.Transaction amount VAT

- 1 (tj. navýší počet přestupků +1)

Vytvoření Toll Transaction a Rated Toll Event,

pokud jde o Registration type = EETS, Exempted, [Exempted not compliant,]{.mark} Exempted trip, Post-paid invoice nebo Pre-paid s dostatečným zůstatkem:

Systém na základě údajů ze vstupu vytvoří Toll Transaction:

- Toll transaction type = ze vstupu

  - 0 = Rating (send)

  - [1 = Cancelling (revoke)]{.mark}

  - [3 = Rerating (adjust)]{.mark}

- Toll transaction status = Processed

- Vehicle category = ze vstupu

- Emission class = ze vstupu

- Emission class CO2= ze vstupu

- Registration number = ze vstupu

- Registration country = ze vstupu

- OBU serial number = ze vstupu

- OBU assignment status = ze vstupu

- Event time = ze vstupu

- Creation time = sysdate time

- Agregation time = null

- Unpaid toll transaction creation time = null

- Discount applied = true

- Transaction amount = suma (Rated Toll Event.Price amount)

- Transaction amount VAT = suma (Rated Toll Event.Price amount VAT)

- Transaction discount amount = suma (Rated Toll Event.Discount amount)

- Transaction discount amount VAT = suma (Rated Toll Event.Discount amount VAT)

- Transaction discount rate = Rated Toll Event.Discount rate (z první RTE)

- Vehicle = ze vstupu

- EETS vehicle = ze vstupu

- Subject type = ze vstupu

- Subject number = ze vstupu

- Original toll transaction = ze vstupu

- Cancelled = false

- Registration type = ze vstupu

  - EETS

  - Pre-paid (v případě dostatečného zůstatku)

  - Exempted

  - [Exempted not compliant]{.mark}

  - Exempted trip

- Toll trip record = ze vstupu

- Toll trip = ze vstupu

- Bill issuer = ze vstupu (tj. System operator)

- 

Systém pro každou oceněnou složku mýta události zpoplatnění vytvoří Rated toll event:

- Charge type = ze vstupu

- Basic unit price = ze vstupu

- Basic unit price definition method = ze vstupu

- Unit price = ze vstupu

- Unit price VAT = ze vstupu

- Number of units = ze vstupu

- Metric unit = ze vstupu

- Price amount = Price amount ze vstupu -- Discount amount

- Price amount VAT = Price amount VAT ze vstupu -- Discount amount VAT

- Tax rate = ze vstupu

- Discount amount = ze vstupu

- Discount amount VAT = ze vstupu

- Discount rate = ze vstupu

- Billing service = ze vstupu

- Toll transaction = reference na Toll Transaction

Postup končí.

#### Alternativní postupy

[Původní záznamy pro re-rating nebo cancelling se nenašly]{.mark}

[Pokud pro re-rating nebo cancelling události Systém nenajde původní záznamy, tak se tyto záznamy odloží.]{.mark}

Nulové Rated Toll Events na fakturách

Pokud jde o nulový Rated Toll Event (Price amount VAT = 0 a zároveň Discount rate = null) a konfigurační klíč = BE_AggregateZeroTollTransactions = false, RTE se neagreguje do Bill Item a Bill session.

Postup končí

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou.

### Vytvoř billing details (SYS.BAR.1.9.HR)

#### Cíl

Cílem tohoto případu užití je na základě vytvořených Toll Transactions a Rated toll events vytvořit Billing Details za každého Bill issuer a zaslat je příslušnýcm Poskytovatelům mýtných služeb.

#### Spuštění případu

V pravidelných intervalech na základě naplánované operace BEm.ExportBillingDetailsHr.

#### Podmínky spuštění

Nejsou.

#### Popis

Systém pro každého Pokytovatele mýtných služeb najde všechny Toll Transaction, které ješte nebyly zahrnuty do Billing Details a pak je pro každého Poskytovatele mýtných služeb postupně zpracovává.

Systém seskupí Toll transactions podle Bill issuer, aby se vytvořily Billing Details za každého Bill issuer zvlášť (= apduOriginator).

Jako informationSenderId bude uveden System operator s příznakem System owner = true (tj. HAC).

Systém pro apci sekci vygeneruje apduIdentifier ze sekvence outgoingApduIdentifierSequence.

Systém dohledá odpovídající Rated Toll Events k nalezeným Toll Transactions.

Systém pro každou Toll Transaction vytvoří jeden BillingDetailsAdu element, pro který vygeneruje aduIdentifier ze sekvence outgoingAduIdentifierSequence.

Systém spočítá na základě nalezených oceněných událostí:

- billingDetailAmount.PaymentFeeAmount = SUM (Rated toll events.price amount)

- billingDetailAmount.VatRate = VAT rate z první RTE

Pokud jde o Toll Transaction typu Rerating nebo Cancelling, Systém do sekce billingDetailsAdu/relatedBillingDetails uvede referenci na původní billing details (Toll Transaction.EETS Export Billing details pro Toll Transaction number z Toll Transaction, která je uvedena jako Toll Transaction.Original toll transaction).

Systém pro každou Toll Transaction ze skupiny vytvoří usageList, který vyplní následovně:

- v sekci usageListEntry:

<!-- -->

- forSectionedRoads uvede:

  - Toll Transaction.Invoice agregation number,

  - podsekci usedSections, kde ve uvede:

    - tollContext = Bill issuer = VCM.System operator,

    - chargeObjectDesignation = Toll Transaction.Toll trip (ID podle Context data zaslaných TSP),

    - appliedLocationClass = 0

    - tollEventTime = Toll Transaction.Event time

    - podsekci usedSectionFee, kde uvede Price amount a VAT rate z Rated toll event s Charge type = Infrastructure nebo Toll.

    - podsekci usedSectionExternalCosts, kde uvede Price amount a VAT rate z Rated toll event s:

    <!-- -->

    - Charge type = Pollution v podsekci externalCostsAir,

    - Charge type = Emission CO2 v podsekci externalCostsCo2.

  - podsekci appliedTariffTableVersion = [TBD]{.mark} [(pro začátek budeme plnit = 1)]{.mark}

  - podsekci appliedLocalVehicleClass, kde uvede:

    - appliedLocalVehicleClassId = Toll Transaction.Vehicle category

  - podsekci vehicleDescription, kde uvede:

    - 

    - 

    - environmentalCharacteristics = Toll Transaction.Emission class

    - futureCharacteristics = Toll Transaction.Emission class CO2

  - usageFee = usedSectionFee

  - usageExternalCosts = korespondující usedSectionExternalCosts

- v sekci includedDiscounts uvede Discount rate, VAT rate a Discount amount pro ostatní Rated toll events s nenulovou Discount rate.

Systém vytvoří zprávu Billing details (DEX.BAR.29.HR).

Systém vyexportuje Billing details za použití rozhraní (INT.BAR.26.HR).

Systém na příslušné Toll Transaction na základě provedeného exportu updatuje atributy:

- EETS Export Billing details Toll transaction number = z billingDetailsAdus.aduIdentifier

- Export date

- Export log

- EETS Toll declaration ID = null

Systém pokračuje se stejným nebo dalším Poskytovatelem mýtných služeb dokud existují další Toll Transactions na zpracování.

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Poznámka 1: Pokud jde o Rerating nebo Cancelling Toll transactions (případně i při souběhu s původní Toll transaction), tak údaje Toll transactions musí být v Billing details uvedené v pořadí Rating, Cancelling a Rerating.

Poznámka 2: Prázdý export Billing details teď nebude podporován, dokud se nezjistí způsob, jak takové BD vytvářet.

### Zaplať mýtnou transakci tokenem (SYS.BAR.1.10.HR)

#### Cíl

Cílem tohoto případu užití je uhradit uloženou Unpaid Toll Transaction.

#### Spuštění případu

V pravidelných intervalech na základě [naplánované operace]{.mark} BEm.ExecuteTokenPaymentPolling.

#### Podmínky spuštění

Systém vytvořil Unpaid Toll Transaction ve stavu Ready for processing, v rámci případu užití Ulož oceněnou mýtnou transakci (SYS.BAR.1.8.HR).

#### 

#### Popis

Systém dohledá Unpaid Toll Transactions ve stavu Ready for processing a seřadí je podle podle počtu již provedených pokusů o zaplacení (Card Payment Request.Attempt count) od nejmenšího k největšímu, a následně je seřadí podle UTT.Event time od nejstaršího k nejnovějšímu (budou se zpracovávat prvně ty, které ještě nemají pokus o zaplacení, pak ty které už pokus mají, atd., v případě shodného počtu pokusů budou zpracovávány od nejstaršího).

Systém pak zpracovává jeden Unpaid Toll Transaction po druhém.

Systém zjistí zda již existuje Payment session pro Card Payment Request pro zpracovávaný Unpaid Toll Transaction:

- - - 
    - 
  - 
  - - 
    - 
    - 
    - 
    - 
    - 
    - 
  - - 
    - 
    - 
  - 

- Pokud aktivní Payment session již existuje (tj. buď Payment session existuje a je ve stavu New nebo In progress):

  - a na Payment session není vyplněn Card token, Systém jej prvně získá -- postup pokračuje od kroku získání Tokenu v postupu při vytvoření nové Payment session,

  <!-- -->

  - a na Payment session je vyplněn Card token, Systém zjistí stav transakce na CorvusPay bráně, a podle získaného Response code a konfigurace (CorvusPay Response Code a Process Step Scheduling) zjistí, zda jde o:

    - zamítnutou transakci, pak postup pokračuje Chybovým postupem = Zamítnutí transakce,

    - transakce ještě není zprocesována, pak [Systém:]{.mark}

      - [na Payment session updatuje Transaction result podle odpovědi z brány, Request time a Process count o 1]{.mark}

      - [na Card payment request updatuje Process on podle konfigurace Process step scheduling a aktuální hodnoty Payment session.Process count,]{.mark}

    - transakce je zamítnuta, ale může se zopakovat, pak postup pokračuje Alternativním postupem = Zamítnutá transakce s možným opakováním.

  <!-- -->

  - - transakce je schválená, postup pokračuje společným postupem, pro případ úspěšného dokončení platební transakce.

- Pokud aktivní Payment session neexistuje (tj. buď Payment session neexistuje nebo existuje a není ve stavu New nebo In progress):

  - Systém vytvoří Payment session:

    - Online payment identifier =unikátní identifikátor platební transakce přiřazený Systémem (guid generovaný z CO)

    - Payment session type = Toll

    - Payment session status = New

    - Payment amount = částka platby

    - Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

    - Internet banking channel =

      - pokud Card Payment Request.count = 0, pak Corvus System api (synchro api pro první pokus)

      - pokud Card Payment Request.count \>0, pak Corvus Tokenize api (asynchro api pro každý další pokus)

    - Created on = aktuální datum a čas

    - Card payment request = reference na odpovídající Card Payment Request

  - 

  - 

  - 

  - 

  - Systém zjistí Payment card, kterou má k platbě použít (první Payment card, která existuje ve směru od Vehicle k Account).

  - Systém updatuje na Payment session:

    - Card number = z VCM.Payment card.Masked card number (z první Payment card, která existuje ve směru od Vehicle k Account)

    - Card token = z VCM.Payment card.Payment card token (z první Payment card, která existuje ve směru od Vehicle k Account)

  - Systém vyvolá synchroní (pokud jde o první pokus) nebo asynchronní komunikaci s CorvusPay platební bránou (rozhraní INT.BAR.27.HR), kdy inicializuje platební transakci za pomocí tokenu a identifikace cílového příjemce platby (tj. Unpaid Toll Transaction.Bill issuer). Systém do platební brány pošle částku platby, měnu platby, token, [Bill issuer (jako store_id)?]{.mark}:

    - 

    - Pokud jde o asynchronní komunikaci a Systém obdržel kladnou odpověď o přijetí a zařazení transakce do fronty na zpracování na straně CorvusPay, změní stav Payment session na In progress a nastaví Process count = 0 a postup končí. Poznámka: Systém se následně periodicky dotazuje CorvusPay na stav transakce a následně pokaždé updatuje na Payment session atribut Status request time a Process count dokud nedostane finální Response code.

    - Jinak Systém na základě získaného Response code z platební brány a konfigurace (CorvusPay Response Code a Process Step Scheduling) zjistí, zda jde o:

      - zamítnutou transakci, pak postup pokračuje Chybovým postupem = Zamítnutí transakce,

      <!-- -->

      - zamítnutou transakci, ale může se zopakovat, pak postup pokračuje Alternativním postupem = Zamítnutá transakce s možným opakováním.

      - schválenou transakci, postup pokračuje společným postupem, pro případ úspěšného dokončení platební transakce.

V případě úspěšného dokončení platební transakce, Systém:

- na Payment session uloží do Result code návratový kód z platební brány,

- změní Payment session status na Realized.

Systém vytvoří Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type = Toll payment

- Payment method = Bank card payment

- Payment category = Credit payment

- Payment status = Realized

- Matching status = Recognized -- matching not needed

- Variable symbol = Variable symbol z Payment session

- Specific symbol = Subject number z Unpaid Toll Transaction

- Payment amount = částka platby

- Date of payment = aktuální datum

- Date of collection = aktuální datum

- Comment = null

- Subject type = z Unpaid Toll Transaction (Account)

- Subject number = z Unpaid Toll Transaction (Account.number)

- Bill issuer bank account = zjištěné číslo bankovního účtu Bill issuera (BIBA) pro Reason = toll

- Bill issuer = z Unpaid Toll Transaction

Systém na základě Unpaid Toll Transaction vytvoří odpovídající Toll Transaction ve stavu Processed, kdy se zkopírují hodnoty odpovídajících atributů z Unpaid Toll Transaction.

Systém převěsí na Toll Transaction odpovídající Rated Toll Events.

Systém updatuje atributy Toll Transaction:

- Unpaid Toll Transaction creation time = z Unpaid Toll Transaction.creation time

- Payment = referenci na realizovanou platbu

Systém zruší Unapid Toll Transaction.

Systém zagreguje Rated toll Event do Bill session, za použití systémové Zagreguj oceněné události do fakturační dávky (SYS.BAR.0.12.HR).

Postup končí.

#### Alternativní postupy

Zamítnutá transakce s možným opakováním

Pokud Systém při zjišťování stavu transakce na CorvusPay bráně dostal Response code, který podle konfigurace (CorvusPay Response Code a Process Step Scheduling) znamená, že transakce je zamítnuta, ale může se zopakovat, pak Systém:

- na Payment session updatuje

  - Status = Rejected by bank,

  - Result code podle odpovědi z brány,

  - Status request time podle posledního dotazu

  - Process count navýší o 1,

- na Card payment request

  - navýší Attempt count o 1,

  - Process on updatuje podle konfigurace Process step scheduling a aktuální hodnoty Attempt count,

- vyhodnotí, zda počet platebních pokusů dosáhl nakonfigurovaného maxima (tj. Card Payment Request.attempt count \> BE_maximalCountOfPaymentAttempts):

  - Pokud maximum bylo dosaženo:

    - Systém updatuje Card Payment Request:

      - Deleted on = sysdate

    - Systém na Rated Toll event:

      - z Rated Toll Event.Price amount VAT odečte Discount amount VAT,

      - z Rated Toll Event.Price amount odečte Discount amount,

    - Systém na Unpaid Toll Transaction:

      - změní stav na Offence

      - uloží datum Offence time

      - dopočítá Transaction amount VAT = suma (Rated Toll Event.Price amount VAT)

      - dopočítá Transaction amount = suma (Rated Toll Event.Price amount),

    - Systém informuje Alert list: Systém na základě nezaplacené mýtné transakce vytvoří nebo updatuje záznam na Alert listu pro dané SPZ, navýší Total due amount o celkovou nezaplacenou částku transakce a Offence count navýší o 1 přestupek, za použití systémové funkce Zaeviduj Offence na Alert list (SYS.TDP.5.6):

      - UTT.Registration number a UTT.Registration country

      - Bill.Bill issuer

      - \+ Unpaid toll transaction.Transaction amount VAT

      - \+ 1 offence (tj. navýší počet přestupků +1)

    - Systém zjistí zda existuje vyplněný kontakt (na VT Vehicle, pokud tam není tak na VT Account, pokud tam neni tak na VT Customer). Pokud je vyplněn:

      - E-mail address, Systém vygeneruje emailovou notifikaci (NTF.BAR.13.HR) a odešle ji.

      - Phone number, Systém vygeneruje SMS notifikaci (NTF.BAR.14.HR) a odešle ji.

  - Pokud počet platebních pokusů nedosáhl nakonfigurovaného maxima:

    - Systém vytvoří novou Payment session:

      - Online payment identifier =unikátní identifikátor platební transakce přiřazený Systémem (guid generovaný z CO)

      - Payment session type = Toll

      - Payment session status = New

      - Payment amount = částka platby

      - Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

      - Internet banking channel = CorvusPay Tokenize api (asynchro api pro každý další pokus)

      - Created on = aktuální datum a čas

      - Card payment request = reference na odpovídající Card Payment Request

    - Systém updatuje Card Payment Request.process on = sysdate.

#### Chybové postupy

Chybějící platná Payment card

Pokud se žádná platná Payment card na Vehicle nebo Account nenašla, Systém nastaví Payment session status na Rejected a uloží do Result code chybový kód značící chybějící kartu. Systém na Card Payment Request updatuje Attempt count o 1.

- - 
  - - 
    - 
    - 
    - 
  - - 
    - 
- - 
  - 

Postup postup pokračuje Alternativním postupem a to krokem, kdy Systém zjišťuje, zda počet platebních pokusů dosáhl nakonfigurovaného maxima.

Neúspěšné přijetí transakce platební branou při asynchronní komunikaci (transakce nebyla zařazena do fronty)

Pokud jde o asynchronní komunikaci a Systém obdržel negativní odpověď o přijetí a zařazení transakce do fronty na zpracování na straně CorvusPay, Systém:

- na Payment session updatuje Process count o 1

- 

- na Card Payment Request updatuje Process on podle Process Step Scheduling a attempt count. (Poznámka: V tomto případě se nebude updatovat Card Payment Request.Attemp count atribut, jelikož jde o technické zamítnutí transakce) .

Postup končí

Zamítnutí transakce

Pokud transakce nebyla schválena a není možné opakování podle konfigurace (CorvusPay Response Code a Process Step Scheduling):

- Systém na Payment session updatuje:

  - Status = Rejected by bank,

  - Result code podle odpovědi z brány,

  - Status request time podle posledního dotazu

  - Process count navýší o 1,

- Systém na Card payment request:

  - navýší Attempt count o 1,

  - Deleted on = sysdate,

- 

- Systém na Rated Toll event:

  - z Rated Toll Event.Price amount VAT odečte Discount amount VAT,

  - z Rated Toll Event.Price amount odečte Discount amount,

- Systém na Unpaid Toll Transaction:

  - změní stav na Offence

  - uloží datum Offence time

  - dopočítá Transaction amount VAT = suma (Rated Toll Event.Price amount VAT)

  - dopočítá Transaction amount = suma (Rated Toll Event.Price amount),

- Systém informuje Alert list: Systém na základě nezaplacené mýtné transakce vytvoří nebo updatuje záznam na Alert listu pro dané SPZ, navýší Total due amount o celkovou nezaplacenou částku transakce a Offence count navýší o 1 přestupek, za použití systémové funkce Zaeviduj Offence na Alert list (SYS.TDP.5.6):

  - UTT.Registration number a UTT.Registration country

  - Bill.Bill issuer

  - \+ Unpaid toll transaction.Transaction amount VAT

  - \+ 1 offence (tj. navýší počet přestupků +1)

- Systém zjistí zda existuje vyplněný kontakt (na VT Vehicle, pokud tam není tak na VT Account, pokud tam neni tak na VT Customer). Pokud je vyplněn:

  - E-mail address, Systém vygeneruje emailovou notifikaci (NTF.BAR.13.HR) a odešle ji.

  - Phone number, Systém vygeneruje SMS notifikaci (NTF.BAR.14.HR) a odešle ji.

Postup končí

#### Poznámky

Nejsou

## Operace s platbami

### Zaplať událost online přes platební bránu (SYS.BAR.2.15.HR)

#### Cíl

Cílem tohoto případu užití je uhradit oceněnou událost online přes CorvusPay platební bránu.

#### Spuštění případu

Případ užití je vloženou součástí následujících případů užití:

- Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

  - online platba z Web portalu nebo Mobile App

- Uhraď přestupek (UC.BAR.0.20.HR)

  - online platba z Offence portálu

  - online platba z Web portalu nebo Mobile App

  - 

  - 

  - 

#### Podmínky spuštění

Je znám Bill issuer, důvod platby, částka a Account.

[Account není terminovaný.]{.mark}

Žádost o platbu přišla z:

- Rozhraní Web Portal API (INT.BAR.33.HR) -- online platba.

#### Popis

Systém na základě vstupních dat vytvoří Payment Session:

- Online payment identifier =unikátní identifikátor platební transakce přiřazený Systémem (guid generovaný z CO)

- Payment session type = podle důvodu ze vstupu:

  - Top-up, pokud důvodem transakce je Top-up

  - Offence, pokud jde o placení přestupků (placení UTT ve stavu Offence),

  - Offence RfP payment, pokud jde o placení RfP za přestupky,

  - jinak Services

  - [TBD]{.mark}

- Payment session status = New

- Payment amount = částka platby

- Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

- Internet banking channel = Online CorvusPay payment

- Created on = aktuální datum a čas

- Card payment request = null

- Selected payment method = null

Systém vyvolá komunikaci s CorvusPay platební bránou (rozhraní INT.BAR.27.HR). Systém do platební brány pošle částku platby, měnu platby, Online payment identifier (jako order_id), Bill issuer (jako store_id), Variable symbol (jako additional_order_number), required complete = false, subscription = false.

Platební brána vrátí redirect url.

Systém přesměruje Aktéra na stránku platební brány (pokud operace byla inicializována v rámci Systému) nebo pošle redirect url externímu systému,který přesměruje svého uživatele.

Aktér na stránce platební brány zvolí platební metodu z nabízeného seznamu a následně zadá patřičné platební údaje a autorizuje transakci.

V případě úspěšného dokončení platby, Systém na Payment session uloží do:

- Selected payment method = zákazníkem vybraná CorvusPay platební metodu na bráně

- Card type = Typ karty zaslaný z platební brány

- Card expiry = Expirace karty zaslaný z platební brány

- Card number = Číslo (maskované) karty zaslaný z platební brány

- Card brand = Brand karty zaslaný z platební brány

- Result code návratový kód z platební brány

- změní Payment session status na Realized.

Systém zjistí BIBA pro fakturaci na základě Bill issuer a Reason:

- Offence, pokud Payment session type = Offence

- Top-up, pokud Payment session type = Top-up

- jinak Services.

Systém vytvoří Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type =

  - Top-up payment, pokud jde o Top-up,

  - jinak Bill payment.

- Payment method = pokud

  - Payment Session.selected payment method = Card payment a Card type má Card type.type = Bank card, pak Bank card payment

  - Payment Session.selected payment method = Card payment a Card type má Card type.type = Bank card má Card type.type = Fleet card , pak Fleet card payment

  - [Payment Session.selected payment method = Apple Pay, pak Bank card payment]{.mark}

  - [Payment Session.selected payment method = Google Pay, pak Bank card payment]{.mark}

  - Payment Session.selected payment method = Pay by IBAN, pak Bank transfer payment

  - [Payment Session.selected payment method = Quick wallet payment, pak Wallet payment]{.mark}

  - [Payment Session.selected payment method = paysafecard, pak Gift card payment]{.mark}

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

- Subject type = ze vstupu nebo podle Unpaid Toll Transaction

- Subject number = ze vstupu nebo podle Unpaid Toll Transaction

- FCI = FCI karty, v případě platby tankovací kartou

- Bill issuer bank account = zjištěný BIBA

- Bill issuer = ze vstupu nebo podle Unpaid Toll Transaction

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Neúspěšná transakce

Pokud dojde k chybě při komunikaci s platební bránou (např. transakace není dokončena do lhůty stanovené konfiguračním klíčem [*BE.PaymentReversalTimeout*)]{.mark} nebo platební brána vrátí chybový návratový kód, Systém:

- uloží do Selected payment method vybranou CorvusPay platební methodu

- nastaví Payment session status na Rejected

- uloží do Result code chybový kód z platební brány

- 

Postup končí

#### Poznámky

Nejsou

### Zaplať událost platbou z externího systému (SYS.BAR.2.16.HR)

#### Cíl

Cílem tohoto případu užití je uhradit oceněnou událost platbou realizovanou v externím systému.

#### Spuštění případu

Případ užití je vloženou součástí následujících případů užití:

- Zaplať předplacený kredit -- Pre-paid in single domain (UC.BAR.0.1.HR)

  - jiná než online platba z Web portalu nebo Mobile App

  - platba přes NexGo EFT na MEV

  - platba na externí POS

- Uhraď přestupek (UC.BAR.0.20.HR)

  - [jiná než online platba z Web portalu nebo Mobile App]{.mark}

  - platba přes NexGo EFT na MEV

  - [platba na externí POS]{.mark}

- 

#### Podmínky spuštění

Je znám Bill issuer, důvod platby, částka a Account.

[Account není terminovaný.]{.mark}

Informace o platbě přišla z:

- Rozhraní ERP Navision (INT.BAR.30.HR) -- platba bankovním převodem

- Rozhraní Web Portal API (INT.BAR.33.HR) -- jiná platba než online (tj. platba SMS nebo Voucherem)

- Rozhraní Web Portal API (INT.BAR.33.HR) -- platba přes NextGo EFT

- Rozhraní POS API (INT.BAR.34.HR) -- platba na externí POS přes její EFT nebo hotovostí

#### Popis

Systém zjistí BIBA pro fakturaci na základě Bill issuer a Reason:

- Offence, pokud jde o Offence operaci

- Top-up, pokud jde o Top-up

- jinak Services.

Systém na základě vstupních dat vytvoří Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type =

  - Top-up payment, pokud jde o Top-up,

  - jinak Bill payment.

- Payment method [=]{.mark} []{.mark}

  - [ze vstupu]{.mark}

  - [jinak Bank transfer payment]{.mark}

- Payment category = Credit payment

- Payment status = Realized

- Matching status = Recognized -- not matched

- Variable symbol = [Null]{.mark}

- Specific symbol = Subject number

- Payment amount = částka platby

- Matched amount = 0

- Date of payment = ze vstupu

- Date of collection = ze vstupu

- Comment = null

- Subject type = podle Subject number

- Subject number = ze vstupu

- FCI = FCI karty, v případě platby tankovací kartou

- Bill issuer bank account = zjištěný BIBA

- Bill issuer = ze vstupu

- 

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Nejsou

#### Poznámky

Nejsou

### Tokenizuj kartu přes platební bránu (SYS.BAR.2.17.HR)

#### Cíl

Cílem tohoto případu užití je tokenizovat bankovní nebo fleet kartu přes CorvusPay platební bránu.

#### Spuštění případu

Případ užití je vloženou součástí následujících případů užití:

- [TBD]{.mark}

Žádost o tokenizaci přišla z:

- Rozhraní Web Portal API (INT.BAR.33.HR) -- tokenizace.

  - 

#### Podmínky spuštění

Je znám Bill issuer, Account a případně Vozidlo.

[Account není terminovaný.]{.mark}

#### Popis

Systém na základě vstupních dat vytvoří Payment Session:

- Online payment identifier =unikátní identifikátor platební transakce přiřazený Systémem (guid generovaný z CO)

- Payment session type = Subscription payment

- Payment session status = New

- Payment amount = 0,01

- Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

- Internet banking channel = Corvus System api nebo CorvusPay Tokenize api, podle procesu

- Created on = aktuální datum a čas

- Card payment request = null

- Selected payment method = null

- Required complete = true

- Subscription required = true

Systém vyvolá komunikaci s CorvusPay platební bránou (rozhraní INT.BAR.27.HR). Systém do platební brány pošle částku platby 0,01 EUR, Online payment identifier (jako order_id), Bill issuer (jako store_id), Variable symbol (jako additional_order_number), required complete = true, subscription required = true.

Platební brána vrátí redirect url.

Systém přesměruje Aktéra na stránku platební brány (pokud operace byla inicializována v rámci Systému) nebo pošle redirect url externímu systému,který přesměruje svého uživatele.

Aktér na stránce platební brány zadá patřičné údaje karty a autorizuje tokenizaci.

V případě úspěšného dokončení tokenizace, Systém na Payment session uloží do:

- Selected payment method = card

- Card type = Typ karty zaslaný z platební brány

- Card expiry = Expirace karty zaslaná z platební brány

- Card number = Číslo (maskované) karty zaslané z platební brány

- Card brand = Brand karty zaslaný z platební brány

- Result code návratový kód z platební brány

- změní Payment session status na Realized.

Systém uloží token a další relevantní údaje o platební kartě na Vozidlo nebo Account, podle toho, pro kterou entitu byla tokenizace inicializována.

Systém zjistí BIBA na základě Bill issuer a Reason Top-up.

Systém vytvoří credit Payment s parametry:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type = Tokenization reservation

- Payment method = pokud

  - Payment Session.selected payment method = Card payment a Card type má Card type.type = Bank card, pak Bank card payment

  - Payment Session.selected payment method = Card payment a Card type má Card type.type = Bank card má Card type.type = Fleet card , pak Fleet card payment

- Payment category = Credit payment

- Payment status = Realized

- Matching status = Recognized --matched

- Variable symbol = Variable symbol z Payment session, pokud existuje, jinak Null

- Specific symbol = Subject number

- Payment amount = částka platby

- Matched amount = částka platby

- Date of payment = aktuální datum

- Date of collection = aktuální datum

- Comment = null

- Subject type = ze vstupu

- Subject number = ze vstupu

- FCI = FCI karty, v případě platby tankovací kartou

- Bill issuer bank account = zjištěný BIBA

- Bill issuer = ze vstupu

Systém vytvoří debit Payment jako kopii kreditní platby, s vyjímkou parametrů:

- Payment number = Unikátní číslo platby podle číslovacího schématu.

- Payment type = Tokenization reservation cancel

- Payment category = Debit payment

- Payment status = Registered

- Matching status = Recognized --matched

- [Date of collection =]{.mark} [null]{.mark}

Systém napáruje kreditní platbu s debetní platbou, tj. vytvoří pro ně Matching s následujícími parametry:

- Date of matching = Datum a čas, kdy bylo párování provedeno

- [Effective date of matching = vyšší datum z datumů obou párovaných]{.mark} stran (tj. payment.date of collection)

- Payment -- debit matching side = debit payment

- Payment -- credit matching side = credit payment

- Matched amount = částka platby

- Matching method = Automatic

- Disconnect allowed = False

- BO Operátor = System

Systém pro debetní platbu vytvoří Payment session pro zrušení tokenizační transakce jako kopii původní Payment session, s vyjímkou parametrů:

- Payment session type = Subscription payment cancel

- Payment session status = New

- Variable symbol = vygenerovaný ze sekvence pro variabilní symboly (PNFVS)

- Created on = aktuální datum a čas

- Required complete = false,

- Subscription required = false

- Selected payment method = null

- Result code = null

- Payment session status = New

- Authorisation code = null.

- 

Systém vyvolá komunikaci s CorvusPay platební bránou (rozhraní INT.BAR.27.HR). Systém do platební brány pošle původní částku platby (tj. 0,01 EUR), Online payment identifier, který byl použit pro tokenizaci karty (jako order_id), Bill issuer (jako store_id), Variable symbol (jako additional_order_number), required complete = false, subscription required = false.

V případě úspěšného dokončení zrušení tokenizační transakce, Systém na Payment session uloží do:

- Selected payment method = card

- Result code návratový kód z platební brány

- změní Payment session status na Realized.

Systém na debetní platbě změní:

- Payment status = Realized

- [Collection date =]{.mark} [sysdate]{.mark}

Systém na Matchingu plateb updatuje Effective date of matching.

Postup končí.

#### Alternativní postupy

Nejsou

#### Chybové postupy

Neúspěšná transakce

Pokud platební brána vrátí chybový návratový kód (TransactionRejected), Systém:

- nastaví Payment session status na Rejected by bank

- uloží do Result code chybový kód z platební brány

Postup končí

#### Poznámky

Nejsou

### 

#### 

- 

- 

- 

- 

#### 

#### 

- - 

    - 
    - 

  - 

  - 

- 

- 

#### 

#### 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

  - 

  - - 
    - 

  - 

  - 

  - 

  - 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

-