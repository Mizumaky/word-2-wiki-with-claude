# Doménový model

## Diagram doménového modelu

![](output_md\TEST_FS\v01\media/media/image3.png){width="6.6930555555555555in" height="5.2555555555555555in"}

Obrázek 1: Diagram doménového modelu

<table>
<caption>Tabulka 2: Verze doménového modelu</caption>
<thead>
<tr>
<th><strong>Verze</strong></th>
<th><strong>Datum</strong></th>
<th><strong>Popis změn</strong></th>
<th><strong>Int. issue</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>0.01</td>
<td>4.22025</td>
<td><p>První verze domain modelu.</p>
<p>Nové entity:</p>
<p>Toll Transaction</p>
<p>Unpaid Toll Transaction</p>
<p>Settlement Record</p>
<p>ERP Export</p>
<p>ERP Import</p>
<p>ERP Log</p>
<p>Card Payment Request</p></td>
<td></td>
</tr>
<tr>
<td>0.02</td>
<td>14.7.2025</td>
<td><p>Nové atributy:</p>
<p>Product Package</p>
<p>Payment Session Item</p>
<p>Změna vazby: Account – Toll Transaction Base</p></td>
<td></td>
</tr>
<tr>
<td>0.03</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Atributy entit

### Test entity

<table>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td>An identifier</td>
<td>Unikátní číslo faktury podle číslovacího schématu. Slouží jako číslo účetního dokladu</td>
<td>Number</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>An attribute to be deleted</td>
<td><p>Unikátní číslo faktury ze sekvence (BNF77), přiřazené fakturám zasílaným do ePorezna k fiskalizaci (ve ePorezna interface: <mark>xxx Invoice identifier</mark>).</p>
<p>Slouží jako číslo účetního dokladu.</p></td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>An attribute to be edited</td>
<td>Unikátní identifikace faktury (Unique Invoice Identifier), která vzniká po uspěšné fiskalizaci faktury v ePorezne.</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
</tbody>
</table>

### Bill (Faktura)

<table>
<caption>Tabulka 4: Atributy Faktury</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td>Bill number (Číslo faktury)</td>
<td>Unikátní číslo faktury podle číslovacího schématu. Slouží jako číslo účetního dokladu</td>
<td>Number</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Fiscal verification number (Fiskální verifikační číslo)</td>
<td><p>Unikátní číslo faktury ze sekvence (BNF77), přiřazené fakturám zasílaným do ePorezna k fiskalizaci (ve ePorezna interface: <mark>xxx Invoice identifier</mark>).</p>
<p>Slouží jako číslo účetního dokladu.</p></td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>JIR (JIR)</td>
<td>Unikátní identifikace faktury (Unique Invoice Identifier), která vzniká po uspěšné fiskalizaci faktury v ePorezne.</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>ZKI (ZKI)</td>
<td><p>Ochranný kód vystavitele faktury (Issuer's Protection Code).</p>
<p>Skládá se z 32 znaků (jednotlivé znaky jsou čísla 0-9 a malá písmena a-f).</p>
<p><mark>Algorithm:</mark></p>
<p><mark>(Tax number + IssueDateTime + InvoiceNumber + BusinessPremiseID + ElectronicDeviceID + InvoiceAmount)</mark></p></td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td>Klasif.</td>
<td>Bill type (Typ faktury)</td>
<td><p>Typ faktury.</p>
<p>Možné hodnoty Customer bill (Zákaznická faktura), FCI bill (Faktura vydavateli tankovacích karet), FCI RfP (Výzva na úhradu vydavateli tankovacích karet), Pre-paid bill (Předplacená faktura), EETS Provider bill (Faktura Poskytovatele mýtných služeb), Exemption partner bill (Faktura partnerovi osvobození),</p>
<p>Možné hodnoty pro HR:</p>
<p>Customer bill (Zákaznická faktura),</p>
<p>EETS Provider bill (Faktura</p>
<p>Poskytovatele mýtných služeb), Exemption partner bill (Faktura partnerovi osvobození),</p>
<p>Request for payment (tj. Offence RfP) (Výzva na úhradu za přestupky<mark>),FCI bill (Faktura vydavateli tankovacích karet),</mark></p>
<p><mark>FCI RfP (Výzva na úhradu vydavateli tankovacích karet),</mark></p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill issue type (Typ vystavení faktury)</td>
<td><p>Typ vystavení faktury. Možné hodnoty:</p>
<p>Regular bill (Řádná faktura), <mark>Simplified bill (Zjednodušená faktura asi zatim nepotrebujeme</mark></p>
<p><mark>),</mark> Corrective bill – credit (Opravná faktura kreditní), Corrective bill – debit (Opravná faktura debetní), Advance bill (Zálohová faktura), Corrective advance bill – credit (Opravná zálohová faktura kreditní), Proforma bill (Proforma faktura),</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill recurrence type (Důvod vystavení faktury)</td>
<td><p>Důvod vystavení faktury. Možné hodnoty: Periodical bill (Řádná faktura), <mark>Hot bill (Ukončovací faktura),</mark> One-time bill (Jednorázová faktura)</p>
<p>Možné hodnoty pro HR: Periodical bill (Řádná faktura), One-time bill (Jednorázová faktura)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill category (Kategorie faktury)</td>
<td><p>Kategorie faktury.</p>
<p>Možné hodnoty: Toll (Mýtné), Top-up (Předplacení mýtného), Services (Služby), <mark>Automated top-up (Automatické předplacení mýtného),</mark> Toll discount (Sleva na mýtném), FC payments (Platby takovací kartou), Penalty (Smluvní pokuty), Late payment interest (Úroky z prodlení), Dunning fee (Náklady vymáhání)</p>
<p>Možné hodnoty pro HR:</p>
<p>Toll (Mýtné), Top-up (Předplacení mýtného), Services (Služby), <mark>FC payments (Platby takovací kartou),</mark> Offence (Přestupek), OBU (OBU), Penalty (Pokuty), OBU accessories (OBU příslušenství), Product package (Produktový balíček)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Stav</td>
<td>Bill issue status (Stav vystavení faktury)</td>
<td><p>Stav vystavení faktury.</p>
<p>Možné hodnoty In progress (Vytváří se), Waiting for print (Čeká na tisk), Print failed (Chyba tisku), Issued (Vystavený), Replaced (Nahrazený),</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill payment status (Stav splacení faktury)</td>
<td><p>Stav splacení faktury.</p>
<p>Možné hodnoty: Unpaid (Neuhrazená), Paid partially (Částečně uhrazená), Paid fully (Plně uhrazená), Payment not needed (Nevyžaduje platbu)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill correction status (Stav korekce faktury)</td>
<td><p>Stav korekce faktury, zda je již plně korigovaná nebo ne.</p>
<p>Možné hodnoty: Not corrected, Partially corrected, Fully corrected</p>
<p>* Povinné pro Bill kategorie Services a Penalty</p></td>
<td>Enum</td>
<td>Ne*</td>
<td>Ne</td>
</tr>
<tr>
<td>Detail</td>
<td>Comment (Komentář)</td>
<td>Libovolný komentář k faktuře</td>
<td>Text(255)</td>
<td>Ne</td>
<td>Ano</td>
</tr>
<tr>
<td></td>
<td>Bill amount (Částka faktury bez daně)</td>
<td>Částka faktury bez daně</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Tax amount (Částka daně)</td>
<td>Částka daně</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Total amount (Celková částka faktury)</td>
<td>Celková částka faktury (částka faktury bez daně + částka daně)</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Date of issue (Datum vystavení)</td>
<td>Datum vystavení faktury</td>
<td>Date</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Due date (Datum splatnosti)</td>
<td>Datum splatnosti faktury</td>
<td>Date</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Date of beginning (Začátek fakturačního období)</td>
<td>Začátek fakturačního období</td>
<td>Date</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Date of end (Konec fakturačního období)</td>
<td>Konec fakturačního období, počítá se jako datum uskutečnění zdanitelného plnění</td>
<td>Date</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Matched amount (Splacená částka faktury)</td>
<td>Částka ve zúčtovací měně, která je již vypořádaná (platbou nebo dobropisem)</td>
<td>Money</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Registration number (Registrační značka)</td>
<td>Registrační značka vozidla</td>
<td>Text (14)</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Registration country (Země registrace)</td>
<td><p>Země, ve které je vozidlo zaregistrováno</p>
<p>Dostupné hodnoty z číselníku Country</p></td>
<td>List of values (CO.Country.Abbreviation)</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Subject type (Typ subjektu)</td>
<td><p>Typ subjektu, ke kterému se vztahuje bill.</p>
<p>Možné hodnoty : Account (Účet), Fleet card issuer (Vydavatel tankovací karty), EETS Provider (Poskytovatel mýtných služeb), Exemption partner (Partner osvobození),</p>
<p>Možné hodnoty pro HR:</p>
<p>- Account (Účet),</p>
<p>- EETS Provider (Poskytovatel mýtných služeb),</p>
<p>- Exemption partner (Partner osvobození),</p>
<p>- <mark>Fleet card issuer (Vydavatel tankovací karty),</mark></p>
<p>- No subject (Bez subjektu)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td>Reference</td>
<td>Subject number</td>
<td><p>Číslo subjektu.</p>
<p>Pro HR obsahuje referenci na:</p>
<p>- VCM.VT Account.number pro Subject type = Account,</p>
<p>- ECM.EETS Provider.Number pro subject type = EETS Provider</p>
<p>- VCM.Business partner.Number (s Business partner.Type = Exemption partner) pro Subject type = Exemption partner</p>
<p><mark>- VCM.Business partner.Number (s Business partner.Type = Fleet Card Issuer) pro Subject type = Fleet Card Issuer</mark></p>
<p>* Nepovinné pro Subject type = No subject</p></td>
<td>Reference</td>
<td>Ne*</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Bill document (Dokument faktury)</td>
<td>PDF dokument faktury vygenerovaný v DF</td>
<td>Reference (DF.Document.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>E-Bill document (Dokument elektronické faktury)</td>
<td>XML dokument faktury vygenerovaný systémem</td>
<td>Reference (DF.Document.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Bill attachment (Příloha faktury)</td>
<td>Příloha faktury</td>
<td>Reference (DF.Document.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Corrected bill (Opravená faktura)</td>
<td>Faktura, která je opravovaná. *Povinné pro Bill issue type = Corrective bill – credit, Corrective bill – debit,</td>
<td>Reference (Bill.Number)</td>
<td>Ne*</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Default bill (Faktura v prodlení)</td>
<td>Faktura v prodlení, ke které byla vystavena faktura s úroky z prodlení nebo náklady upomínání.</td>
<td>Reference (Bill.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Replaced proforma bill (Nahrazená proforma faktura)</td>
<td>Číslo Proforma faktury, která je nahrazená touto fakturou.</td>
<td>Reference (Bill.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Replaced advance bill (Nahrazená zálohová faktura)</td>
<td>Číslo zálohové faktury, která je nahrazená touto fakturou.</td>
<td>Reference (Bill.Number)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Replaced by bill (Nahrazující faktura)</td>
<td><p>Faktura, která nahrazuje tuto fakturu.</p>
<p>* Povinné, pokud Bill.bill issue status = Replaced</p></td>
<td>Reference (Bill.Number)</td>
<td>Ne*</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Bill issuer bank account (Bankovní účet vystavitele faktur)</td>
<td>Bankovní účet vystavitele faktur (BIBA)</td>
<td>Reference (VCM.Bill issuer bank account.bank account)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Bill issuer (Vystavitel faktur)</td>
<td>Vystavitele faktury</td>
<td>Reference (VCM.Business partner.Type = System operator and Is bill issuer = true)</td>
<td>Ano</td>
<td>Systém</td>
</tr>
</tbody>
</table>

Obrázek 1: Stavový diagram faktury

![](output_md\TEST_FS\v01\media/media/image4.png){width="6.754582239720035in" height="6.14878937007874in"}

### Bill Item (Položka faktury)

<table>
<caption>Tabulka 5: Atributy Položky faktury</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Klasif.</td>
<td>Bill item category (Kategorie položky faktury)</td>
<td><p>Kategorie položky faktury.</p>
<p>Možné hodnoty: Toll event (Mýtná událost), Top-up event (Předplacení mýtného), Penalty event (Smluvní pokuta), Tax (Daň), Service event (Servis), Discount event (Sleva), FC payment (Platba tankovací kartou), <mark>Currency adjustment (Dorovnání kurzovního rozdílu),</mark> Rounding adjustment (Dorovnání zaokrouhlovacího rozdílu), <mark>Adjustment Bill</mark> <mark>Item (Korekční položka faktury),</mark> Late payment interest (Úroky z prodlení), Dunning fee (Náklady vymáhání)</p>
<p>Možné hodnoty pro HR: Toll event (Mýtná událost), Tax (Daň), <mark>FC payment (Platba tankovací kartou),</mark> Rounding adjustment (Dorovnání zaokrouhlovacího rozdílu), Service event (Servis), Penalty (Pokuta), Top-up event (Předplacení mýtného), OBU event (OBU), OBU accessories event (OBU příslušenství), Product package event (Produktový balíček)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Product type (Typ productu)</td>
<td><p>Typ produktu.</p>
<p>Hodnoty z PCRE např.:</p>
<p>Dunning fee, OBU deposit, OBU fine, Top-up, Chargeable service,</p></td>
<td>PC.product type</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Charge type (Typ poplatku)</td>
<td><p>Typ poplatku z Rated toll event.</p>
<p>Dostupné hodnoty:</p>
<p>Project/Domain:</p>
<table>
<thead>
<tr>
<th><mark>Infrastructure (Pozemní komunikace)</mark></th>
<th><mark>CZT<br />
ITIS/HU<br />
VO1<br />
SKT</mark></th>
<th><mark>1</mark></th>
</tr>
</thead>
<tbody>
<tr>
<td><mark>Pollution (Znečištění ovzduší)</mark></td>
<td><mark>CZT<br />
VO1<br />
SKT</mark></td>
<td><mark>2</mark></td>
</tr>
<tr>
<td><mark>Noise (Hluk z provozu)</mark></td>
<td><mark>CZT</mark><br />
<mark>VO1 (test only)</mark></td>
<td><mark>3</mark></td>
</tr>
<tr>
<td><mark>Emission CO2 (Emise CO2)</mark></td>
<td><mark>CZT<br />
ITIS/HU<br />
VO1<br />
SKT</mark></td>
<td><mark>6</mark></td>
</tr>
<tr>
<td><mark>Toll (Mýtné)</mark></td>
<td>SKT<br />
VO1<br />
ITIS/HU<br />
ITIS/PL<br />
ITIS/BG</td>
<td>4</td>
</tr>
<tr>
<td><mark>Discount (Sleva)</mark></td>
<td><mark>SKT<br />
CZT<br />
VO1</mark></td>
<td><mark>5</mark></td>
</tr>
<tr>
<td><mark>Pollution - Noise (Znečištění ovzduší a hluk z provozu)</mark></td>
<td><mark>ITIS/HU</mark></td>
<td><mark>7</mark></td>
</tr>
<tr>
<td>External costs (Externí náklady)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Congestions (Zácpy)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>None (Bez rozpadu)</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td>Enum (PCRE.Charge type)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill item type (Typ položky faktury)</td>
<td>Možné hodnoty: Regular bill item (Řádná položka faktury), Corrective bill item – credit (Opravná položka faktury kreditní), Corrective bill item – debit (Opravná položka faktury debetní),</td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Detail</td>
<td>Price amount (Cena za položku)</td>
<td><p>Celková cena za položku bez daně.</p>
<p>Pro položku s Bill item type category = tax je to výše daně za položku.</p></td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Price amount VAT (Cena s daní za položku)</td>
<td>Celková částka za položku s daní</td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Unit price (Jednotková cena bez daně)</td>
<td>Jednotková cena bez daně po aplikaci zvláštní ceny (price override)</td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Unit price VAT (Jednotková cena s daní)</td>
<td>Jednotková cena s daní po aplikaci zvláštní ceny (price override)</td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card number (Číslo karty)</td>
<td><p>Maskované číslo platební karty úspěšně použité pro úhradu <mark>mýtné transakce,</mark></p>
<p>např. 1234456****** 5789</p></td>
<td>Text 21</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card type (Typ karty)</td>
<td><p>Typ platební karty úspěšně použité pro úhradu <mark>mýtné transakce,</mark></p>
<p>např. DKV, Visa,</p></td>
<td>Text 21</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Number of units (Počet jednotek)</td>
<td>Počet fakturovaných jednotek</td>
<td>Number</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Metric unit (Měrná jednotka)</td>
<td>Měrná jednotka</td>
<td>List of Values (CO.Metric unit. Metric unit code)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Discount amount (Sleva)</td>
<td>Výše slevy (neobsahuje daň).</td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Discount amount VAT (Sleva s daní)</td>
<td>Výše slevy s daní</td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Discount rate (Sleva v %)</td>
<td>Výše slevy vyjádřená v procentech.</td>
<td>Percentage (5.2)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Tax base (Základ daně)</td>
<td><p>Základ daně.</p>
<p>Pro položku s Bill item type category = tax je to výše základu daně.</p></td>
<td>Money</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Tax rate (Sazba daně)</td>
<td><p>Sazba daně (pokud je aplikována).</p>
<p>*Povinná pro Bill item category = Tax</p></td>
<td>Percentage (5.2)</td>
<td>Ne*</td>
<td>Ne</td>
</tr>
<tr>
<td>Reference</td>
<td>Billing service (Fakturovaná služba)</td>
<td><p>Fakturovaná služba události.</p>
<p>* Nepovinné pro Bill item category = tax</p></td>
<td>Reference (PC.Event.billing service</td>
<td>Ano*</td>
<td>Ne</td>
</tr>
</tbody>
</table>

### Bill Session (Fakturační dávka)

<table>
<caption>Tabulka 6: Seznam atributů fakturační dávky</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td>Bill session number (Číslo fakturační dávky)</td>
<td>Číslo fakturační dávky ve formátu RRMMDDXXXX, kde RR jsou poslední dvě číslice roku, MM jsou měsíc konce fakturační dávky, DD jsou den konce fakturační dávky a XXXX je sekvenční číslo</td>
<td>Text</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Klasif.</td>
<td>Bill session aggregation type (Typ agregace fakturační dávky)</td>
<td><p>Typ fakturační dávky.</p>
<p>Možné hodnoty: Post-paid (S následným placením), Post-paid invoice (S následným placením na fakturu), Post-paid card (S následným placením kartou), FCI (S následným placením VTK), Pre-paid (Předplacený), EETS Provider (Poskytovatel mýtných služeb)</p>
<p>Možné hodnoty pro HR:</p>
<p>Post-paid invoice (S následným placením na fakturu), Post-paid card (S následným placením kartou), EETS Provider (Poskytovatel mýtných služeb), Exemption partner (Partner osvobození), Pre-paid (Předplacený),</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill session content type (Obsah fakturační dávky)</td>
<td><p>Obsah fakturační dávky.</p>
<p>Možné hodnoty: Toll (Mýto), Services (Služby), FC payments (Platby tankovací kartou)</p>
<p>Možné hodnoty pro HR:</p>
<p>Toll (Mýto), <mark>FC payments (Platby tankovací kartou)</mark></p></td>
<td>Enum</td>
<td>Ano</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Bill session type (Typ fakturační dávky)</td>
<td>Typ pravidelné fakturační dávky. Možné hodnoty: Normal (Normální), Delayed (Opožděné události), <mark>Rejected (Zamítnuté faktury),</mark> Rerated (Znovuoceněné události)</td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Status</td>
<td>Bill session status (Stav fakturační dávky)</td>
<td>Stav fakturační dávky. Možné hodnoty: Open (Otevřená), Closing (Zavíraná), Closed (Uzavřená), Closed with error (Uzavřená s chybou tisku), Reprocessing (Znovuuzavíraná)</td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td>Detail</td>
<td>Bill period start (Počáteční datum fakturační dávky)</td>
<td>Počáteční datum fakturační dávky určuje spodní hranici data událostí, které budou zahrnuté do fakturační dávky</td>
<td>Date</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill period end (Koncové datum fakturační dávky)</td>
<td>Koncové datum fakturační dávky určuje horní hranici data událostí, které budou zahrnuté do fakturační dávky</td>
<td>Date</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill cycle (Fakturační cyklus)</td>
<td><p>Fakturační cyklus. Možné hodnoty: Month (Měsíční), 15-days (Patnáctidenní), 10-days (Desetidenní), 5-days (Pětidenní)</p>
<p>Možné hodnoty pro HR:</p>
<p>Month (Měsíční), 15-days (Patnáctidenní)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Reference</td>
<td>Derived bill session (Původní fakturační dávka)</td>
<td><p>Reference na původní bill session v případě vytvoření Rejected bill session.</p>
<p>V případě, že bill session type = Rejected, pak je povinný.</p></td>
<td>Text</td>
<td>Ne*</td>
<td>Ne</td>
</tr>
</tbody>
</table>

Obrázek 2: Stavový diagram Fakturační dávky

![A diagram of a bill AI-generated content may be incorrect.](output_md\TEST_FS\v01\media/media/image5.png){width="5.2034722222222225in" height="6.111111111111111in"}

### Payment (Platba)

<table>
<caption>Tabulka 7: Atributy platby</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td>Payment number (Číslo platby)</td>
<td>Unikátní číslo platby podle číslovacího schématu. Slouží jako číslo účetního dokladu.</td>
<td>Number</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Klasif.</td>
<td>Payment type (Typ platby)</td>
<td>Typ platby určuje, z jakého důvodu byla vytvořena</td>
<td>List of Values (Payment type.Name)</td>
<td>Ano</td>
<td>Ano</td>
</tr>
<tr>
<td></td>
<td>Payment method (Způsob platby)</td>
<td><p>Způsob, jakým byla platba provedena</p>
<p>Možné hodnoty:</p>
<p>Bank card payment (Platba bankovní kartou), Fleet card payment (Platba tankovací kartou), Cash payment (Platba v hotovosti), Bank transfer payment (Platba bankovním převodem), Virtual payment (Virtuální platba), <mark>Service payment (Platba službou)</mark>, Wallet payment, Gift card payment (Platba darovací kartou)</p>
<p>Možné hodnoty pro HR:</p>
<p>Bank card payment (Platba bankovní kartou), <mark>Fleet card payment (Platba tankovací kartou),</mark> Cash payment (Platba v hotovosti), Bank transfer payment (Platba bankovním převodem), Virtual payment (Virtuální platba), <mark>Wallet payment, Gift card payment (Platba darovací kartou)</mark></p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Payment category (Kategorie platby)</td>
<td><p>Kategorie platby.</p>
<p>Možné hodnoty: Credit payment (Příchozí platba), Debit payment (Odchozí platba)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Stav</td>
<td>Payment status (Stav platby)</td>
<td><p>Stav platby.</p>
<p>Možné hodnoty: Registered (Registrovaná), Realized (Realizovaná)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Matching status (Stav párování)</td>
<td><p>Stav platby z pohledu párování plateb.</p>
<p>Možné hodnoty: Unrecognized (Nerozpoznaná), Recognized – matching not needed (Rozpoznaná – nepáruje se), Recognized – not matched (Rozpoznaná – nenapárovaná), Recognized – partially matched (Rozpoznaná – částečně napárovaná), Recognized – matched (Rozpoznaná – napárovaná), Unidentified (Neidentifikovatelná)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td>Detail</td>
<td>Variable symbol (Variabilní symbol)</td>
<td>Variabilní symbol platby</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Specific symbol (Specifický symbol)</td>
<td>Specifický symbol platby</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Payment amount (Částka)</td>
<td>Částka platby</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Matched amount (Napárovaná částka platby)</td>
<td>Částka, která je již vypořádaná (fakturou nebo debetní platbou)</td>
<td>Money</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Date of payment (Datum platby)</td>
<td>Datum, kdy byla platba uskutečněná</td>
<td>DateTime</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Date of collection (Datum připsání platby)</td>
<td>Datum, kdy byla platba připsána na účet</td>
<td>Date</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Comment (Komentář)</td>
<td>Komentář k platbě</td>
<td>Text</td>
<td>Ne</td>
<td>Ano</td>
</tr>
<tr>
<td></td>
<td>Subject type (Typ subjektu)</td>
<td><p>Typ subjektu, ke kterému se vztahuje platba.</p>
<p>Možné hodnoty : Account (Účet), Fleet card issuer (Vydavatel tankovací karty), EETS Provider (Poskytovatel mýtných služeb), Exemption partner (Partner osvobození),</p>
<p>Možné hodnoty pro HR:</p>
<p>- Account (Účet),</p>
<p>- EETS Provider (Poskytovatel mýtných služeb),</p>
<p>- Exemption partner (Partner osvobození),</p>
<p>- <mark>Fleet card issuer (Vydavatel tankovací karty),</mark></p>
<p>- No subject (Bez subjektu)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td>Reference</td>
<td>Subject number</td>
<td><p>Číslo subjektu.</p>
<p>Pro HR obsahuje referenci na:</p>
<p>- VCM.VT Account.number pro Subject type = Account,</p>
<p>- ECM.EETS Provider.Number pro subject type = EETS Provider</p>
<p>- VCM.Business partner.Number (s Business partner.Type = Exemption partner) pro Subject type = Exemption partner</p>
<p><mark>- VCM.Business partner.Number (s Business partner.Type = Fleet Card Issuer) pro Subject type = Fleet Card Issuer</mark></p>
<p>* Nepovinné pro Subject type = No subject</p></td>
<td>Reference</td>
<td>Ne*</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>POS (Obchodní místo)</td>
<td>* Povinné jen pro payment method = cash nebo (bank card nebo fleet card payment přes EFT terminál)</td>
<td>Reference <mark>(VCM.Point of Sale/POS.number)</mark></td>
<td>Ano*</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td><mark>FCI (VTK)</mark></td>
<td><mark>Reference na vystavitele tankovacích karet</mark></td>
<td><mark>Reference (VCM.Business partner.Number (s Business partner.Type = Fleet Card Issuer))</mark></td>
<td><mark>Ne</mark></td>
<td><mark>Systém</mark></td>
</tr>
<tr>
<td></td>
<td><mark>FCI RfP (RfP vydavateli tankovacích karet)</mark></td>
<td><mark>Reference na RfP vydavatele tankovacích karet</mark></td>
<td><mark>Reference (Bill.number)</mark></td>
<td><mark>Ne</mark></td>
<td><mark>Systém</mark></td>
</tr>
<tr>
<td></td>
<td>Bill issuer bank account (Bankovní účet vystavitele faktur)</td>
<td>Bankovní účet vystavitele faktur podle konfigurace (BIBA)</td>
<td>Reference (VCM.Bill issuer bank account.bank account)</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Bill issuer (Vystavitel faktur)</td>
<td>Vystavitele faktury</td>
<td>Reference (VCM.Business partner.Type = System operator and Is bill issuer = true)</td>
<td>Ano</td>
<td>Systém</td>
</tr>
</tbody>
</table>

Obrázek 3: Stav párování platby

![](output_md\TEST_FS\v01\media/media/image6.png){width="6.434978127734033in" height="5.176930227471566in"}

Obrázek 4: Stav platby

![](output_md\TEST_FS\v01\media/media/image7.png){width="6.257234251968504in" height="6.886000656167979in"}

### Payment Session (Platební transakce)

<table>
<caption>Tabulka 8: Atributy platby</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td>Online payment identifier (Identifikátor online platby)</td>
<td>Identifikátor online platby generovaný protistranou případně naší stranou v CO (guid).</td>
<td>Text(1024)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td>Klasif.</td>
<td>Payment session type (Typ platební transakce)</td>
<td><p>Typ platební transakce.</p>
<p>Možné hodnoty: Bill payment (Platba faktury) (Pozn. toto je default hodnota v případě placení přes EFT terminal, kdy nemáme určený jiný kontext),</p>
<p>Top-up (Dobití kreditu), Deposit (Depozit), Bill payment (Platba faktury), <mark>Service (Služba), Penalty (Smluvní pokuta)</mark>, Toll (Mýtné), Offence payment (Platba přestupku), Offence RfP payment (Platba RfP za přestupky), Subscription payment (Vytvoření platby k získání tokenu), Subscription payment cancel (Zrušení platby k získání tokenu), Subscription validation (Ověření tokenu), OBU (OBU), Product package (Produktový balíček)</p>
<p>Možné hodnoty HR: Top-up (Dobití kreditu), Toll (Mýtné), Service (Služba), Offence payment (Platba přestupku), Offence RfP payment (Platba RfP za přestupky), Subscription payment (Vytvoření platby k získání tokenu), Subscription payment cancel (Zrušení platby k získání tokenu), OBU (OBU), Product package (Produktový balíček)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Stav</td>
<td>Payment session status (Stav platební transakce)</td>
<td>Stav platební transakce. Možné hodnoty: New (Nová), In progress (Zpracovává se), Realized (Realizovaná), Rejected by bank (Zamítnutá bankou), Cancelled (Zrušená), Rejected (Zamítnutá)</td>
<td>Enum</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td>Detail</td>
<td>Payment amount (Částka platby)</td>
<td>Částka platby.</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Authorization code (Autorizační kód)</td>
<td>Autorizační kód platby</td>
<td>Text</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Variable symbol (Variabilní symbol)</td>
<td>Variabilní symbol, se kterým byla platba poslána protistraně.</td>
<td>Number</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Internet banking channel (Kanál internetového bankovnictví)</td>
<td><p>Kanál internetového bankovnictví. Možné hodnoty: <mark>Online Bank card payment (Platba kartou),</mark> Online Fleet card payment (Platba tankovací kartou), EFT payment (Platba přes platební terminál), <mark>Online Fleet card authorization (Autorizace tankovací karty),</mark> CorvusPay Online payment (Platba online přes bránu Besteron), CorvusPay payment by token (Platba tokenem přes CorvusPay), CorvusPay tokenization (Tokenizace přes CorvusPay)</p>
<p>Možné hodnoty HR:</p>
<p>Online Bank card payment (Platba kartou), <mark>Online Fleet card payment (Platba tankovací kartou),</mark> EFT payment (Platba přes platební terminál), CorvusPay Online payment (Platba online přes bránu CorvusPay), CorvusPay System api (Synchroní platba tokenem přes CorvusPay), CorvusPay Tokenize api (Asynchroní platba tokenem přes CorvusPay)</p></td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>EFT terminal ID (ID platebního terminálu)</td>
<td>Identifikátor platebního terminálu</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Created on (Datum vytvoření)</td>
<td>Datum a čas vytvoření platební trasakce</td>
<td>Datetime</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Subscription required (Token požadován)</td>
<td>Příznak, zda se požaduje vytvoření Tokenu</td>
<td>Bool</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Subsequent charge (Platba tokenem)</td>
<td>Příznak, zda platba je na základě existujícího Tokenu.</td>
<td>Bool</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Require complete (Požadováno dokončení)</td>
<td>Příznak, zda platba je finální (false) nebo jen preauthorizace (true), která se musí doprocesovat.</td>
<td>Bool</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Process count (Počet pokusů)</td>
<td>Aktuální počet pokusů o zprocesování</td>
<td>Number</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Card type (Typ karty)</td>
<td>Typ karty</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card expiry (Expirace karty)</td>
<td><p>Expirace karty</p>
<p>Na GUI se zobrazuje ve formátu: MM/YY</p></td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card number (Číslo karty)</td>
<td><p>Číslo karty</p>
<p>Zobrazuje se ve formátu:</p>
<p>**** **** **** 1111</p></td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card brand (Brand karty)</td>
<td>Brand karty (v textové formě typ karty, pokud je na výstupu paltební brány)</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Card token (Token karty)</td>
<td>Token platební karty přiřazené k vozidlu nebo účtu</td>
<td>Text</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Status Request DateTime (Datum a čas dotazu na stav)</td>
<td>Datum a čas posledního dotazování na Payment session status</td>
<td>Datetime</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Result code (Návratový kód platební transakce)</td>
<td>Návratový kód platební transakce tak, jak je poslaný platební bránou nebo vyplněný Systémem v případě chybějící platné karty.</td>
<td>Text</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td>Reference:</td>
<td>Payment card (Platební karta)</td>
<td>Reference na použitou platební kartu (buď z Account nebo z Vehicle)</td>
<td>Reference (VCM.Payment card.id)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Payment (Platba)</td>
<td>Reference na výslednou platbu</td>
<td>Reference (Payment)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Selected payment method (Vybraný způsob platby)</td>
<td><p>Vybraný způsob platby z nabízených platební branou třetí strany.</p>
<p>Pozn. aktuálně implementovány CorvusPay Payment Method</p></td>
<td>Reference (CorvusPay Payment Method)</td>
<td>Ne</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Application code (Kód aplikace)</td>
<td>Kód aplikace, ze které byla platba iniciována.</td>
<td>Reference (AC.Application)</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Card Payment Request (Požadavek na platbu kartou)</td>
<td>Požadavek na platbu kartou v rámci kterého se vytvořila tato Payment session.</td>
<td>Reference (Card Payment Session)</td>
<td>ne</td>
<td>Systém</td>
</tr>
</tbody>
</table>

![](output_md\TEST_FS\v01\media/media/image8.png){width="5.776388888888889in" height="6.5125in"}

Obrázek : Stavový diagram Platební transakce

| **Původní stav** | **Nový stav** | **Případ užití**                          |
|------------------|---------------|-------------------------------------------|
| N/A              | New           | Zaplať mýtnou transakci (SYS.BAR.1.10.HR) |
| New              | In progress   | Zaplať mýtnou transakci (SYS.BAR.1.10.HR) |
| New              | Rejected      | Zaplať mýtnou transakci (SYS.BAR.1.10.HR) |
| In progress      | Realized      | Zaplať mýtnou transakci (SYS.BAR.1.10.HR) |
| In progress      | Rejected      | Zaplať mýtnou transakci (SYS.BAR.1.10.HR) |

: Tabulka změn stavů Platební transakce

### 

<table>
<caption><span id="_Toc205285658" class="anchor"></span>Payment Session Item (Položka platební transakce)Tabulka 8: Atributy platby</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td>Identif.</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Klasif.</td>
<td>Payment session type (Typ platební transakce)</td>
<td><p>Typ položky platební transakce.</p>
<p>Možné hodnoty: Top-up (Dobití kreditu), Toll (Mýtné), Service (Služba), Offence payment (Platba přestupku), Offence RfP payment (Platba RfP za přestupky), Subscription payment (Vytvoření platby k získání tokenu), Subscription payment cancel (Zrušení platby k získání tokenu), OBU (OBU), Product package (Produktový balíček)</p></td>
<td><p>Enum</p>
<p>Payment session type</p></td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Detail</td>
<td>Number of units (Počet jednotek)</td>
<td>Počet jednotek</td>
<td>Number</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Reference:</td>
<td>RfP (RfP)</td>
<td>Reference na RfP které se má uhradit</td>
<td>Reference (BAR.Bill)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Product package (Produktový balíček)</td>
<td>Reference na Produktový balíček, které se má uhradit</td>
<td>Reference (PCRE.Product package)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Chargeable service (Zpoplatněná služba)</td>
<td>Reference na určitou hodnotu Event attribute type = Zpoplatněná služba, reprezentující položku, která se má uhradit</td>
<td>Reference (PCRE.Chargeable service)</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Payment session (Platební transakce)</td>
<td>Platební transakce ke které se vztahuje daná položka.</td>
<td>Reference (BAR.Payment session)</td>
<td>Ano</td>
<td>Ne</td>
</tr>
</tbody>
</table>

### Matching (Párování plateb)

<table>
<caption>Tabulka 9: Atributy párování plateb</caption>
<thead>
<tr>
<th><strong>Typ atributu</strong></th>
<th><strong>Název atributu EN (CZ)</strong></th>
<th><strong>Popis atributu</strong></th>
<th><strong>Datový typ</strong></th>
<th><p><strong>Povinný</strong></p>
<p><em>Ano/Ne</em></p></th>
<th><p><strong>Měnit.</strong></p>
<p><em>Ano/Ne</em></p></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>Date of matching (Datum párování)</td>
<td>Datum a čas, kdy bylo párování provedeno</td>
<td>DateTime</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Effective date of matching (Účetní datum párování)</td>
<td>Datum, ke kterému dojde k zaúčtování párovací operace (Vyšší datum z datumů obou párovaných stran). V ERP odpovídá atributu ApplicationDate (Datum vyrovnání).</td>
<td>Date</td>
<td>Ano</td>
<td>Systém</td>
</tr>
<tr>
<td></td>
<td>Matched amount (Párovaná částka)</td>
<td>Párovaná částka ve zúčtovací měně (nižší částka z obou párovaných operací)</td>
<td>Money</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Matching method (Metoda párování)</td>
<td>Metoda, jak došlo k napárování. Možné hodnoty: Automatic (automatické), Manual (manuální)</td>
<td>Enum</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Disconnect allowed (Povoleno odpárování)</td>
<td>Určuje, zda může být párovací operace zrušena. Možné hodnoty Ano, Ne</td>
<td>Boolean</td>
<td>Ano</td>
<td>Ne</td>
</tr>
<tr>
<td>Reference</td>
<td>Bill – debit matching side (Faktura – Debetní strana)</td>
<td>Identifikátor faktury na debetní straně párování (každá párovací operace má jednu referenci na debetní straně fakturu nebo platbu a jednu reference na kreditní straně – opět fakturu nebo platbu)</td>
<td>Reference</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Bill – credit matching side (Faktura – Kreditní strana)</td>
<td>Identifikátor faktury na kreditní straně párování (každá párovací operace má jednu referenci na debetní straně fakturu nebo platbu a jednu reference na kreditní straně – opět fakturu nebo platbu)</td>
<td>Reference</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Payment – credit matching side (Platba – Kreditní strana)</td>
<td>Identifikátor platby na kreditní straně párování (každá párovací operace má jednu referenci na debetní straně fakturu nebo platbu a jednu reference na kreditní straně – opět fakturu nebo platbu)</td>
<td>Reference</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>Payment – debit matching side (Platba – Debetní strana)</td>
<td>Identifikátor platby na debetní straně párování (každá párovací operace má jednu referenci na debetní straně fakturu nebo platbu a jednu reference na kreditní straně – opět fakturu nebo platbu)</td>
<td>Reference</td>
<td>Ne</td>
<td>Ne</td>
</tr>
<tr>
<td></td>
<td>BO Operator (Backoffice Operator)</td>
<td>Backoffice Operator, který provedl párování</td>
<td>Reference</td>
<td>Ne</td>
<td>Ne</td>
</tr>
</tbody>
</table>