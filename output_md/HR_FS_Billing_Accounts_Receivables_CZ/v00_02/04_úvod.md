# Úvod

Předmětem této specifikace je popis modulu Billing and Accounts Receivables informačního systému Billien.

## Procesy HR

Modul podporuje následující procesy:

### Předplacení kreditu

Zákazník si předplácí kredit při registraci nového předplaceného účtu nebo kdykoliv poté přímo ze Kiosku, Web portálu, MEV nebo obchodního místa.

Kredit si zákazník může navýšit hotovostí, bankovní nebo tankovací kartou na POS, bankovní nebo tankovací kartou na Kiosku, Voucherem, bankovní nebo tankovací kartou nebo okamžitým bankovním převodem na Web portalu, nebo standardním bankovním převodem na základě předem vystavené Proforma faktury (z BO, [Web portálu]{.mark}). Informace o provedé platbě bankovním převodem Systém obdrží od ERP přes rozhraní (INT.BAR.30.HR).

Platba za předplacený kredit musí být větsí než minimálně povolená částka pro předplacení kreditu a nový zůstatek předplaceného kreditu musí dosáhnout minima pro balance předplaceného kreditu. Částka v hotovosti musí být menší než maximální povolená částka pro předplacení kreditu hotovostí.

O předplacený kredit se navýší zákazníkův předplacený balance účtu. Kredit je využit na pokrytí mýtných transakcí.

[Pokud byl předplacený kredit uhrazen tankovací kartou, platba je zahrnuta do VTK]{.mark} [faktury a zákazník obdrží jen potvrzení o provedení platby.]{.mark}

Za dobití kreditu se automaticky vygeneruje zálohová faktura za top-up a napáruje se na top-up platbu.

Zálohová faktura se fiskalizuje u chorvatské finanční autority (Porezna uprava).

Denně se provádí settlement mezi Bill issuers za předplacený kredit a projeté mýto. Výsledkem jsou zúčtovací platby mezi Bill issuers.

Projeté mýtné se průběžně strhává z pre-paid balance a na konci měsíce se vystaví zúčtovací faktura za mýtné per Bill issuer. Za spotřebovaný pre-paid credit se vystaví Credit notes k zálohovým fakturám za top-up.

Credit notes k zálohovým fakturám a settlement platby se pak použijí pro vypárování faktur za mýtné.

Pokud dojde k re-ratingu, který vede k dobropisu za mýtné, které bylo stržené z pre-paid balance, vystaví se nová zálohová faktura za kredit, který se vrátí na pre-paid balance.

Poznámka: Pokud dojde k re-ratingu, který vede k dobropisu za mýtné, které bylo stržené z product balance, vrátí se kredit na product balance.

| **CODE** | **TYPE**                       | **TC** | **AMOUNT** | **NOTE**                    |
|----------|--------------------------------|--------|------------|-----------------------------|
| 1        | Credit payment - top up        | HAC    | 10         |                             |
| 2        | Credit payment - top up        | HAC    | 10         |                             |
| 3        | Credit payment - top up        | HAC    | 10         |                             |
|          |                                |        |            |                             |
| A        | Advance invoice                | HAC    | 10         |                             |
| B        | Advance invoice                | HAC    | 10         |                             |
| C        | Advance invoice                | HAC    | 10         |                             |
|          |                                |        |            |                             |
| 4        | Debit payment - settlement     | HAC    | 10         |                             |
| 5        | Credit payment - settlement    | BINA   | 10         |                             |
| 6        | Debit payment - settlement     | HAC    | 10         |                             |
| 7        | Credit payment - settlement    | AZM    | 10         |                             |
|          |                                |        |            |                             |
|          |                                |        |            |                             |
| D        | Toll invoice                   | HAC    | 10         |                             |
| E        | Toll invoice                   | BINA   | 10         |                             |
| F        | Toll invoice                   | AZM    | 10         |                             |
|          |                                |        |            |                             |
| G        | Credit note to Advance invoice | HAC    | 10         | on pdf to be displayed A, D |
| H        | Credit note to Advance invoice | HAC    | 10         | on pdf to be displayed B, E |
| I        | Credit note to Advance invoice | HAC    | 10         | on pdf to be displayed C, F |
|          |                                |        |            |                             |
| J        | Credit note to Toll invoice    | BINA   | 2          |                             |
| K        | Advance invoice                | BINA   | 2          | balance update              |
|          |                                |        |            |                             |
|          | MATCHING                       |        |            |                             |
| A        | 1                              | HAC    | 10         |                             |
| B        | 2                              | HAC    | 10         |                             |
| C        | 3                              | HAC    | 10         |                             |
| D        | G                              | HAC    | 10         |                             |
| E        | 5                              | BINA   | 10         |                             |
| F        | 7                              | AZM    | 10         |                             |
| H        | 4                              | HAC    | 10         |                             |
| I        | 6                              | HAC    | 10         |                             |
| J        | K                              | BINA   | 2          |                             |

Pokud dojde žádosti k ukončení předplacenéhomýtného účtu, Systém vygeneruje Credit note ke zálohové faktuře za top-up. Vrácení kreditu na bankovní účet zákazníka proběhne přes ERP.

### Uložení mýtných transakcí

Systém obdrží oceněný mýtný průjezd a uloží jej jako mýtnou transakci, která je buď:

- již zaplacena z Pre-paid balance nebo z Product balance a zagreguje se do Bill session,

- nebo nezaplacena kvůli chybějící registraci provozovatele vozidla, nebo kvůli nedostatečnému zůstatku na Pre-paid balance, nebo se bude platit tokenizovanou kartou,

- nebo se bude agregovat do bill session.

Konkrétní postup zavisí na Registration type transakce (pre-paid, post-paid, EETS, etc).

Pokud mýtná transakce zůstane nezaplacena, je označena jako Offence a musí ji provozovatel vozidla zaplatit přes Offence portal anebo Web portal, POS, případně MEV při zastavení na dálnici. Po zaplacení se vystaví jednorázová faktura za mýtné.

Nezaplacené mýtné transakce, u kterých není známa adresa provozovatele vozidla, se po určité době označí jako technická ztráta (Technical loss).

Nezaplacené mýtné transakce, u kterých je známa adresa provozovatele vozidla, se po určité době seskupí, naúčtuje se za jejich procesování administrativní poplatky a vystaví se RfP, které se dále vymáhá (vytvoří se následně pro něj Debt v DU).

Systém okamžitě odešle do ERP informace o nezaplacených RfP.

RfP musí provozovatel vozidla zaplatit přes Offence portal anebo Web portal, POS, případně MEV při zastavení na dálnici.

Pokud je RfP zaplaceno bankovním převodem, informuje nás o tom ERP.

Po zaplacení RfP se vystaví jednorázová faktura za přestupek (mýtné + administrativní poplatky).

Systém okamžitě odešle do ERP informace o zaplacených RfP, pokud nebylo zaplaceno bankovním převodem.

Nezaplacené RfP se po určité době může prodat vymáhací agentuře. O prodeji RfP agentuře dostaneme zprávu z ERP. [TBD -- buď se RfP jen označí jako prodané a dál se už nebude vracet v seznamu na zaplacení, nebo se vystaví na základě RfP faktura a ta se odepíše?.]{.mark}

Systém zagregované mýtné transakce periodicky (denně) posílá do ERP.

Systém periodicky odešle do ERP informace o zaplacených bills.

### Vystavení pravidelné faktury za mýtné 

Pravidelná faktura za mýtné je vystavována podle Registration type transakce (pro Pre-paid, Post-paid invoice, EETS Provider, Exemption partner, Fleet card issuer (za mýtné transakce uhrazené fleet kartou).

Po ukončení fakturačního období, Systém vytvoří fakturu za každého Bill issuera (System operatora), po jejichž úsecích vozidla jezdila během příslušného fakturačního období.

Pokud součet oceněných mýtných událostí je záporný, Systém vytvoří dobropis. Jinak Systém vystaví fakturu.

V případě přeceněných mýtných událostí, Systém vystaví vrubopis nebo dobropis k původní faktuře, obsahující přeceněné události.

V případě opožděných mýtných událostí, Systém vystaví vrubopis nebo dobropis k původní faktuře za časové období, do které patří opožděné události.

Zúčtovací období 15-denní (EETS Provider bill) nebo měsíční (ostatní), případně se bude brát nastavení z Account nebo Business partner.

Systém vytvoří dokument faktury s agregací po bill items. Dokument obsahuje také daňovou rekapitulaci. Dokument je v pdf formátu, případně v xml formátu (e-faktura), pokud jej zákazník nebo business partner požaduje.

Faktura se fiskalizuje u chorvatské finanční autority (Porezna uprava).

V příloze faktury je detailní výpis mýtných transakcí (kromě EETS Provider a Fleet card issuer bills).

Faktura (pdf, případně i xml) je zaslána emailem a je dostupná na Web portálu. V Případě e-faktury je zaslána navíc pře eFina službu.

Systém okamžitě odešle do ERP informace o nezaplacených bills.

Systém periodicky odešle do ERP informace o zaplacených fakturách.

Pokud je bill zaplacen bankovním převodem, informuje nás o tom ERP.

### Vystavení jednorázové faktury 

Jednorázová faktura je vystavována za prodej OBU, předplacení kreditu, produktových balíčků, zaplacení nezaplacených mýtných transakcí nebo RfP.

Systém vytvoří dokument faktury s agregací po bill items. Dokument obsahuje také daňovou rekapitulaci. Dokument je v pdf formátu, případně v xml formátu (e-faktura), pokud jej zákazník nebo business partner požaduje.

Faktura se fiskalizuje u chorvatské finanční autority (Porezna uprava).

V příloze faktury za zaplacené mýtné transakce je detailní výpis mýtných transakcí.

Faktura (pdf, případně i xml) je zaslána emailem a je dostupná na Web portálu. V Případě e-faktury je navíc zaslána pře eFina službu.

Systém periodicky odešle do ERP informace o zaplacených bill.

### [Vystavení pravidelné výzvy na úhradu za platby tankovací kartou]{.mark} 

[Pravidelné RfP za platby tankovací kartou je vystavována FCI platby provedené jejich takovacími kartami (platba za OBU, mýtné transakce nebo předplaceného kreditu).]{.mark}

[Po ukončení fakturačního období, Systém vytvoří RfP za každého Bill issuer platby tankovací kartou provedenou v příslušném fakturačním období.]{.mark}

[Zúčtovací období je měsíční.]{.mark}

[Systém vypočítá dobu splatnosti RfP podle nastavení VTK.]{.mark}

[RfP je automaticky napárovaná na nevypárované kreditní platby nebo dobropisy.]{.mark}

[Systém vytvoří dokument RfP s agregací po bill items. Dokument je v pdf formátu.]{.mark}

[Faktura je zaslána emailem.]{.mark}

[Systém odešle do ERP informace o bill.]{.mark}

### Re-rating

Re-rating bude inicializován nad Toll Trip Record (VTP).

V návaznosti na požadavek na re-rating, Systém zcancluje původní Toll transaction a jeho Rated Toll Events, a o zrušenou částku updatuje pre-paid nebo product balance, která byla použita pro úhradu původní transakce.

Po přecenění Toll Trip Record s novými údaji Systém obdrží novou cenu a vytvoří nová Toll Transaction s odpovídajícími Rated Toll Events, které bude procesovat jako standardní oceněný trip.