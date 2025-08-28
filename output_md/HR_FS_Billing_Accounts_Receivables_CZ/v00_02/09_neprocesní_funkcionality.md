# Neprocesní funkcionality

## Fakturace

### Číslování faktur

Číslování faktur (Bill number) bude prováděno podle následujícího schématu **(10 znaků)**:

<table>
<thead>
<tr>
<th>Číslovací schéma</th>
<th>Popis</th>
<th>Číslovací logika</th>
</tr>
</thead>
<tbody>
<tr>
<td><mark>BNF13</mark></td>
<td><mark>Faktury za mýtné a služby NDS</mark></td>
<td><mark>1{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill issuer = 3 (NDS)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>BNF23</mark></td>
<td><mark>Dobropisy za mýtné a služby NDS</mark></td>
<td><mark>2{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill issuer = 3 (NDS)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>BNF33</mark></td>
<td><mark>Vrubopisy za mýtné a služby NDS</mark></td>
<td><mark>3{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill Bill issuer = 3 (NDS)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>BNF14</mark></td>
<td><mark>Faktury za mýtné a služby NDS pro Poskytovatele</mark> mýtných služeb</td>
<td><mark>1{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill issuer = 4 (NDS TC)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>BNF24</mark></td>
<td><mark>Dobropisy za mýtné a služby NDS pro Poskytovatele</mark> mýtných služeb</td>
<td><mark>2{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill issuer = 4 (NDS TC)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>BNF34</mark></td>
<td><mark>Vrubopisy za mýtné a služby NDS pro Poskytovatele</mark> mýtných služeb</td>
<td><mark>3{Bill issuer:B}{Date:YY}{SEQ:000000}</mark><br><mark>kde:</mark><br><mark>Bill Bill issuer = 4 (NDS TC)</mark><br><mark>SEQ – serial number in the current business year</mark></td>
</tr>
<tr>
<td><mark>1YY0XXXXXX</mark></td>
<td><mark>NDS invoices (toll invoices)</mark></td>
<td></td>
</tr>
<tr>
<td><mark>2YY0XXXXXX</mark></td>
<td><mark>NDS invoices (service invoices)</mark></td>
<td></td>
</tr>
<tr>
<td><mark>3YY0XXXXXX</mark></td>
<td><mark>OBU deposit</mark></td>
<td></td>
</tr>
<tr>
<td><mark>4YY0XXXXXX</mark></td>
<td><mark>NDS credit notes</mark></td>
<td></td>
</tr>
<tr>
<td><mark>5YY0XXXXXX</mark></td>
<td><mark>NDS credit notes EETS Provider</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY0XXXXXX</mark></td>
<td><mark>NDS invoice EETS Provider</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY02XXXXX</mark></td>
<td><mark>Daily closing RfP sent to retail partner</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY03XXXXX</mark></td>
<td><mark>Cash-box closing RfP sent to retail partner</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY04XXXXX</mark></td>
<td><mark>Collateral and bank guarantees</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY05XXXXX</mark></td>
<td><mark>Debit payments (money transfers, payment refunds etc.)</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY06XXXXX</mark></td>
<td><mark>Automated top-up</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY07XXXXX</mark></td>
<td><mark>Supplementary toll collection</mark></td>
<td></td>
</tr>
<tr>
<td><mark>6YY09XXXXX</mark></td>
<td><mark>Overall payment (more invoices covered by one payment)</mark></td>
<td></td>
</tr>
<tr>
<td><mark>7YY0XXXXXX</mark></td>
<td><mark>NDS debit notes<br />
</mark></td>
<td></td>
</tr>
<tr>
<td><mark>8YY0XXXXXX</mark></td>
<td><mark>NDS debit notes EETS Provider</mark></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

- 

POZNÁMKA: číslo faktury uvedené výše představuje variabilní symbol (VS) příslušné faktury. Číslo účtu představuje specifický symbol (SS) příslušné faktury. U FCI specifický symbol (SS) příslušné faktury se nevyplňuje.

- 

### Číslování plateb

Číslování Variabilních symbolů **(10 znaků)** a Plateb **(12 znaků)** bude prováděno podle následujícího schématu:

| **Číslovací schéma** | **Popis**                                                                                                                                                                                        | **Číslovací logika**       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| PNFVS                | Payment Variable Symbol sequence for payments.`<br>`{=html}(Může obsahovat díry v číslování). Použití pro situace kdy se VS generuje před vykonáním platby a je možné celý proces platby zrušit. | {SEQ:0000000000} (10pozic) |
| PNF1                 | Payment number sequence for Billien payments (sekvence s dírama)                                                                                                                                 | 1{Date:YY}{SEQ:000000000}  |
|                      |                                                                                                                                                                                                  |                            |
|                      |                                                                                                                                                                                                  |                            |

: Tabulka : Číslovaní plateb

- 
- 

### Zaokrouhlování

Viz aktuální konfigurace [Rounding (Zaokrouhlování)](#_Rounding_(Zaokrouhlování)).

#### Bill rounding 

Všechny částky včetně dopočítavaných částek na entitách TD, RTE a RSE budou uloženy s přesností na 10 desetinných míst.

Na úrovni nedaňových bill item se sumarizované částky Price amount budou držet na 10 desetinných míst, po vytvoření tax item se nedaňové bill items zaokrouhlí na 2 desetinná místa (Price amount):

- Základ daně se zaokrouhlí matematicky s přesností na dvě desetinná místa. Daň se zaokrouhlí stejným algoritmem (s přesností na dvě desetinná místa).

  - Tedy základ daně = zaokrouhlený (SOUČET(všech mýtných událostí);2) a

  - Daň = zaokrouhlený (základ daně \* sazba daně;2)

#### POS rounding

Dopočítavaná částka platby v hotovosti na POS se bude zaokrouhlovat v závislosti na POS měně:

- Pokud POS měna je CZK, převedná částka se zaokrouhlí na celé číslo.

- Pokud POS měna je EUR, převedná částka se zaokrouhlí na nejbližší pěticent (tj. 102,02 🡪 102,00; 102,03 🡪 102,05; 102,26 🡪 102,25; 99,98 🡪 100,00).

- Pokud POS měna je HUF, převedná částka se zaokrouhlí na nejbližší 5 HUF.

- Pokud POS měna je PLN, převedná částka se zaokrouhlí na 2 desetinná místa

### Variabilní symbol

Logika na vyplňování Variable symbolu je následující:

- VS na Payment session se vyplňuje podle číslovacího schématu PNFVS

- VS na Payment, který vznikl na základě Payment session, se vyplňuje VS z Payment session

- VS na Payment, který vznikl jako úhrada nějakého Bill, se vyplňuje Bill number

- VS na Payment v ostatních případech (neznáma platba, odchozí platba za depozit) se vyplní Payment number

- VS pro top-up platbu začíná na 2

- VS pro depozit platbu začíná na 3

- VS pro hotovostní záruku Post-paid acoount začíná na 40

- VS pro hotovostní záruku EETS Provider začíná na 41

- 

- 

- 

### [Atributy dokumentu pro dobropis a vrubopis]{.mark}

[Následující pravidla budou používána na atributy dokumentů (např. trvalá/zasílací adresa, číslo zákazníka/účtu) dobropis a vrubopis:]{.mark}

| **[Dobropis (opětovně oceňované události)]{.mark}** | [Všechny atributy dokumentu nastavené dle data ukončení pravidelné fakturační dávky s typem normální, která se uzavírá]{.mark} |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **[Vrubopis (opětovně oceňované události)]{.mark}** | [Všechny atributy dokumentu nastavené dle data ukončení pravidelné fakturační dávky s typem normální, která se uzavírá]{.mark} |
| **[Vrubopis (opožděné události)]{.mark}**           | [Všechny atributy dokumentu nastavené dle data ukončení pravidelné fakturační dávky s typem normální, která se uzavírá]{.mark} |
| **[Dobropis (korekce)]{.mark}**                     | [Všechny atributy dokument nastavené dle aktuálního data]{.mark}                                                               |
| **[Vrubopis (korekce)]{.mark}**                     | [Všechny atributy dokument nastavené dle aktuálního data]{.mark}                                                               |

: Tabulka : Atributy dokumentu pro dobropis a vrubopis

## BIBA - pravidla pro určení BIBA

Systém, při dohledávání BIBA, musí na vstupu uvést Systém operátor a Currency, navíc Systém může uvést Reason.

Systém se snaží dohledat prvně BIBA, odpovídající požadované trojkombinaci.

Pokud nenajde, dohledá BIBA pro kombinaci Systém operátor, Currency a Reason= ANY.

Pokud BIBA pro tuto kombinaci neexistuje, Systém dohledá BIBA pro kombinaci Systém operátor, jeho default currency a Reason =ANY.

## Vliv plateb na BM Balance

Platby následujících Payment types ovlivňují odpovídající BM Balance:

<table>
<thead>
<tr>
<th><strong>Name EN</strong></th>
<th><strong>Payment category</strong></th>
<th><strong>Related Balance</strong></th>
<th><strong>Module</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Bill payment</td>
<td>Příchozí platba</td>
<td>Post-paid balance</td>
<td>BAR</td>
</tr>
<tr>
<td>Credit note refund</td>
<td>Odchozí platba</td>
<td>Post-paid balance,<br />
EETS Provider balance</td>
<td>BAR</td>
</tr>
<tr>
<td>Deposit payment</td>
<td>Příchozí platba</td>
<td>Total deposit,<br />
Available deposit</td>
<td>BAR</td>
</tr>
<tr>
<td>Deposit refund</td>
<td>Odchozí platba</td>
<td>Total deposit,<br />
Available deposit</td>
<td>BAR</td>
</tr>
<tr>
<td>Payment refund</td>
<td>Odchozí platba</td>
<td>Post-paid balance,<br />
EETS Provider balance</td>
<td>BAR</td>
</tr>
<tr>
<td>Collateral guarantee payment</td>
<td>Příchozí platba</td>
<td>Total guarantee,<br />
Available guarantee</td>
<td>CM</td>
</tr>
<tr>
<td>Collateral guarantee refund</td>
<td>Odchozí platba</td>
<td>Total guarantee,<br />
Available guarantee</td>
<td>CM</td>
</tr>
<tr>
<td>Collateral guarantee forfeiture</td>
<td>Odchozí platba</td>
<td>Total guarantee,<br />
Available guarantee</td>
<td>CM</td>
</tr>
<tr>
<td>Bill payment from collateral guarantee</td>
<td>Příchozí platba</td>
<td>Post-paid balance</td>
<td>BAR</td>
</tr>
<tr>
<td>EETS Provider bill payment</td>
<td>Příchozí platba</td>
<td>EETS Provider balance</td>
<td>BAR</td>
</tr>
</tbody>
</table>