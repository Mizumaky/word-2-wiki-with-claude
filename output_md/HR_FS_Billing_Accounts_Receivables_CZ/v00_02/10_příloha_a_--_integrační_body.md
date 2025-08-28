# Příloha A -- Integrační body

## Rozhraní TC HR -- HAC (INT.BAR.26.HR)

[Interface implementovaný na straně Správce mýtné domény slouží k výměně informací o registrovaných vozidlech, mýtných deklaracích a dat zpoplatnění mezi Správcem mýtné domény (TC) a Poskytovatelem]{.mark} mýtných služeb [(TSP).]{.mark}

[Popis implementace rozhraní je uveden ve specifikaci Common Functionalities (FS CO) - Rozhraní EETS pro odesílání a příjem EDE zpráv (INT.CO.20).]{.mark}

Bulkový online interface implementovaný jako Web service na straně Billien 5.8 umožňuje export oceněných Billing details podle ISO 12855:2022.

Typy EDE zpráv (systém TC) relevantní pro Billing:

- Billing Details (odchozí zpráva DEX.BAR.29.HR) - Soubor oceněných Billing details HR -- HAC Toll Chargerem zasílaný Poskytovatelům mýtných služeb (např. ITIS).

- Ack / List Acknowledgement (příchozí/odchozí zpráva DEX.BAR.100.HR) --potvrzení Poskytovatele mýtných služeb o přijetí souboru Billing Details Details

## Rozhraní Platební brána CorvusPay (INT.BAR.27.HR)

Online interface implementovaný na straně CorvusPay, který umožňuje:

- vytvoření tokenu platební karty

- verifikace tokenu platební karty

- online platbu tokenem platební karty

- online platbu platební kartou.

Specifikace rozhraní na Confluence.

### Online platba tokenem platební karty

![](output_md\HR_FS_Billing_Accounts_Receivables_CZ\v00_02\media/media/image11.emf){width="5.182798556430447in" height="3.2291666666666665in"}

### 

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |

### 

|     |     |     |     |     |
|-----|-----|-----|-----|-----|
|     |     |     |     |     |
|     |     |     |     |     |
|     |     |     |     |     |

#### Request

| Atribut      | Formát | Délka | Mandatory | Popis                     |
|--------------|--------|-------|-----------|---------------------------|
| store_id     | Int    |       | y         | Point of sale ID          |
| version      | Double |       | y         | API version, always 1.4   |
| token_value  | string | 22    | y         | token                     |
| order_number | string | 36    | y         | unique order number       |
| amount       | float  |       | y         | order amount              |
| currency     | string | 3     | y         | currency                  |
| cart         | string | 255   | n         | shopping cart description |
| signature    | string | 64    | y         | HMAC-SHA256 signature     |

#### Response

| Atribut              | Formát | Délka | Mandatory | Popis                                                                                                   |
|----------------------|--------|-------|-----------|---------------------------------------------------------------------------------------------------------|
| response-code        | Int    |       | y         | Value 1 is expected which means that request validated and scheduled for`<br>`{=html}further processing |
| response-message     | string | 255   | y         | Value can be accepted or declined                                                                       |
| acceptance-date-time | string | 22    | y         | Acceptance date and time in format`<br>`{=html}yyyyMMddHHmmss                                           |

### Online platba platební kartou

#### Prepare order

| Atribut          | Formát | Délka | Mandatory | Popis                     | Mapování na atributy Payment session |
|------------------|--------|-------|-----------|---------------------------|--------------------------------------|
| store_id         | Int    |       | y         | Point of sale ID          | Mapování z Bill Issuer               |
| version          | Double |       | y         | API version, always 1.4   |                                      |
| require_complete | bool   |       | y         | If token required.        |                                      |
| order_number     | string | 36    | y         | unique order number       | Online payment identifier            |
| amount           | float  |       | y         | order amount              | Payment amount                       |
| currency         | string | 3     | y         | currency                  |                                      |
| cart             | string | 255   | n         | shopping cart description |                                      |
| signature        | string | 64    | y         | HMAC-SHA256 signature     |                                      |

#### Response to Prepare order

| Atribut      | Formát | Délka | Mandatory | Popis        |
|--------------|--------|-------|-----------|--------------|
| redirectUrl  |        |       | y         | redirectUrl  |
| redirectData |        |       | y         | redirectData |
|              |        |       |           |              |

#### Checkt transaction status

| Atribut      | Formát | Délka | Mandatory | Popis                   |
|--------------|--------|-------|-----------|-------------------------|
| store_id     | Int    |       | y         | Point of sale ID        |
| version      | Double |       | y         | API version, always 1.4 |
| order_number | string | 36    | y         | unique order number     |
| currency     | string | 3     | y         | currency                |
| signature    | string | 64    | y         | HMAC-SHA256 signature   |

#### Response to Checkt transaction status

| Atribut                 | Formát | Délka | Mandatory | Popis                                                                                                   | Mapování na atributy Payment session |
|-------------------------|--------|-------|-----------|---------------------------------------------------------------------------------------------------------|--------------------------------------|
| response-code           | Int    |       | y         | Value 1 is expected which means that request validated and scheduled for`<br>`{=html}further processing | Result code                          |
| response-message        | string | 255   | y         | Value can be accepted or declined                                                                       | Result code                          |
| order_number            | string | 36    | y         | unique order number                                                                                     | Online payment identifier            |
| transaction-date-time   | string | 22    | y         | Transaction date and time in format`<br>`{=html}yyyyMMddHHmmss                                          |                                      |
| transaction-amount      | Int    |       | y         | Transaction amount                                                                                      | Payment amount                       |
| status                  |        |       |           | Status of the transaction (e.g. completed)                                                              |                                      |
| currency-code           | string | 3     | y         | Currency of the transaction                                                                             |                                      |
| cc-type                 |        |       |           | Card type                                                                                               | Card type                            |
| cardholder-name         |        |       |           | Cardholder name                                                                                         |                                      |
| cardholder-surname      |        |       |           | Cardholder surname                                                                                      |                                      |
| cardholder-address      |        |       |           | Cardholder address - street                                                                             |                                      |
| cardholder-city         |        |       |           | Cardholder city                                                                                         |                                      |
| cardholder-zip-code     |        |       |           | Cardholder zip code                                                                                     |                                      |
| cardholder-email        |        |       |           | Cardholder email                                                                                        |                                      |
| cardholder-phone        |        |       |           | Cardholder phone                                                                                        |                                      |
| cardholder-country      |        |       |           | Cardholder country                                                                                      |                                      |
| card-details            |        |       |           | Card number                                                                                             | Card number                          |
| reference-number        |        |       |           | Reference number                                                                                        |                                      |
| approval-code           |        |       |           | Approval code                                                                                           |                                      |
| transaction-type        |        |       |           | Transaction type                                                                                        |                                      |
| additional-order-number |        |       |           | Additional order number                                                                                 | Variable symbol                      |
| installment-number      |        |       |           | Installment number (not used, always 0)                                                                 |                                      |

## Rozhraní EFT Terminal NexGo (INT.BAR.28.HR)

Integrace terminálu NexGo se Systémem bude zprosdředkována přes Web portal API (INT.BAR.33.HR).

## Rozhraní EFT Terminal Ingenico (INT.BAR.29.HR)

Integrace terminálu Ingenico EFT-POS se Systémem umožňuje bezpečnou tokenizaci karty a zpracování plateb prostřednictvím přímého komunikačního kanálu mezi Systémem a zařízením EFT-POS.

Podporovány jsou dva případy primárního použití:

- Tokenizace: Systém odešle do terminálu požadavek na tokenizaci a vyzve uživatele, aby vložil nebo přejel kartou. Terminál zpracuje požadavek a vrátí token karty, který lze použít pro budoucí transakce bez nutnosti použití fyzické karty.

- Zpracování platby: Systém zahájí požadavek na platbu, specifikuje částku a volitelně uložený token (pokud je k dispozici). Pokud není token k dispozici, vyzve uživatele, aby vložil nebo přejel kartou. Terminál zpracovává transakci a komunikuje s CorvusPay za účelem autorizace. Po dokončení se vrátí zpráva s odpovědí označující schválení nebo odmítnutí transakce.

![](output_md\HR_FS_Billing_Accounts_Receivables_CZ\v00_02\media/media/image12.png){width="5.495138888888889in" height="3.7083333333333335in"}

Obrázek 8: Sekvenční schéma komunikace s terminálem Ingenico

Poznámka: „ECR" v tomto diagramu představuje HR-Toll PC, zatímco „Host" je back-end server dodavatele EFT terminálu.

Níže jsou uvedeny definice zpráv používaných v procesu transakce.

### Authorization Request (Systém → EFT)

Inicializuje požadavek na transakci ze Systému na EFT Ingenico.

Vybraný obsah:

<table>
<caption>Tabulka 36: Vybrané atributy Ingenico zprávy Authorization Request</caption>
<thead>
<tr>
<th><strong>Field</strong></th>
<th><strong>Type</strong></th>
<th><strong>Mandatory</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Transaction Type</em></td>
<td>Num</td>
<td>Yes</td>
<td>01 : Sale<br>02 : Pre-authorization<br>03 : Cash Advance<br>04 : Cash Back<br>05 : Refund<br />
…</td>
</tr>
<tr>
<td><em>Transaction Amount</em></td>
<td>Num</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td><em>INFO</em></td>
<td>Alpha-Num<br>extended</td>
<td>No</td>
<td>Nepovinné informace o transakci.<br>Hodnoty musí být uloženy v následujícím formátu:<br>&lt;FieldID&gt;&lt;Value&gt;;<br />
<br />
TOKENIZE<br>Používá se k označení požadavku na tokenizaci a očekávaného tokenu transakce ve zprávě autorizační odpovědi.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Úplnou definici zprávy Authorization Request lze nalézt na Confluence: CorvusPay-ECR--Ingenico_EFT-POS-vXXX.

### Authorization Request Confirmation (EFT → Systém)

Potvrzuje přijetí žádosti o autorizaci a indikuje, že terminál je připraven pokračovat v procesování požadavku.

### Authorization Response (EFT → Systém)

Odešle konečný výsledek zpracování transakce do Systému.

Vybraný osah:

| **Field** | **Type** | **Mandatory** | **Description** | **Mapování na atributy Payment session** |
|----|----|----|----|----|
| *Transaction* *Number* | Num | Yes | Číslo transakce přidělené terminálem.`<br>`{=html}Formát:`<br>`{=html}CCTTTT, where CC is company number, and TTTT,`<br>`{=html}ticket number or STAN (for ISO 8583 transactions) | Online payment identifier |
| *Transaction flag* | Num | Yes | 00 : Error in the format of the request message`<br>`{=html}01 : Transaction accepted without authorization code`<br>`{=html}02 : Transaction accepted with authorization`<br>`{=html}03 : Needs Voice referral`<br>`{=html}04 : Transaction Refused`<br>`{=html}05 : Needs Manual card data entry`<br>`{=html}06 : Authorization Call Failure (Referral disabled)`<br>`{=html}07 : Card is on the black list`<br>`{=html}08 : Card is not supported`<br>`{=html}09 : Card is expired`<br>`{=html}10 : Incorrect PAN`<br>`{=html}11 : Card is not yet activated`<br>`{=html}12 : Card is blocked`<br>`{=html}13 : There is no paper for printing`<br>`{=html}14 : Needs to be forced on-line`<br>`{=html}15 : Terminal-Host communication error`<br>`{=html}16 : Transaction is not allowed`<br>`{=html}17 : Incorrect amount`<br>`{=html}18 : There is no such transaction`<br>`{=html}19 : Supervisor permission is needed`<br>`{=html}20 : The key is not loaded`<br>`{=html}21 : Old black-list`<br>`{=html}30 : Missing reference loyalty card number`<br>`{=html}50 : Canceled by user`<br>`{=html}60 : Logon required`<br>`{=html}61 : Close batch required`<br>`{=html}99 : Transaction accepted without authorization and`<br>`{=html}the terminal sends batch upload | Result code |
| *Company name* | Alpha-`<br>`{=html}Num`<br>`{=html}extended | No | Jméno spojené s typem karty. | Card type |
| *Transaction token* | Alpha-Num`<br>`{=html}extended | No | Transakční token poskytnutý autorizačním systémem, pokud je podporována tokenizace. |  |
|  |  |  |  |  |

: Tabulka 37: Vybrané atributy Ingenico zprávy Authorization Response

Úplnou definici zprávy Authorization Response lze nalézt na Confluence: CorvusPay-ECR--Ingenico_EFT-POS-vXXX.

## [Rozhraní ERP Navision (INT.BAR.30.HR)]{.mark}

[TBD]{.mark}

## Rozhraní ePorezna (fiskalizace) (INT.BAR.31.HR)

Ze zákona je ve Chorvatsku povinnost provádět fiskalizaci všech vystavených faktur a dobropisů placených online platbou nebo hotovostí. [Dobrovolně lze na fiskalizaci zasílat všechny faktury, včetně faktur nezaplacených nebo placených převodem.]{.mark}

[HAC]{.mark} [se rozhodl, že budeme fiskalizovat všechny]{.mark} [vystavené]{.mark} [faktury kromě RfP]{.mark} [a Proforma bill.]{.mark}

Highl level popis rozhraní přiložen:

![](output_md\HR_FS_Billing_Accounts_Receivables_CZ\v00_02\media/media/image13.emf)

### Registrace business premisses

Aby bylo možné posílat faktury do ePorezna, na prvopočátku je potřeba zaregistrovat Business premises, ze kterých se vystavují faktury posílané na fiskalizaci. Jde o jednorázový úkon, [který je dostupný z GUI ePorezna]{.mark}.

### Fiskalizace faktury

Následná komunikace s ePorezna spočívá v odeslání zprávy s fakturou a dalších údajů. Struktura a mapování zpráv a odpovědí je uvedena v přiloženém excelu:

![](output_md\HR_FS_Billing_Accounts_Receivables_CZ\v00_02\media/media/image14.emf)

Pro faktury zasílané do ePorezna je potřeba generovat čísla faktur tak, aby byly ze nepřerušené sekvence pro každý business premises a pro každý rok. Navíc musí obsahovat identifikaci business premises a electronic device, kde byla faktura vystavena.

[Pro faktury vystavené ze selfcarů se použije business premises W901.]{.mark}

[Pro faktury vystavené na ENF BO se určí business premises podle nastavení na User Profile (OrganizationalUnit.Number). Pokud hodnota na User profile není vyplněna, použije se výchozí hodnota pro BO (D100).]{.mark}

[A pro faktury vystavené z BO se použije business premises podle nastavení na User Profile (OrganizationalUnit.Number). Pokud hodnota na User profile není vyplněna, použije se výchozí hodnota pro BO (D100).]{.mark}

[Faktury budou vystaveny ze dvou elektronických zařízení (electronic devices):]{.mark}

- [2102 = online prodej na selfcare a]{.mark}

- [2103 = prodej z ostatních business premises. 2103 je považován za centrálně nainstalovaný fakturační software, který je přístupný z pracovních stanic umístěných v různých business premises.]{.mark}

Mimo jiné se s fakturou posílá ZKI, což je Ochranný kód vystavitele faktury (Issuer\'s Protection Code). Obsahuje zakódované údaje[: (OIB]{.mark} [+ IssueDateTime + InvoiceNumber + BusinessPremiseID + ElectronicDeviceID + InvoiceAmount]{.mark}).

Pokud podání bylo úspěšné, v odpovědi z ePorezna přijde Unique Invoice Identifier (JIR), který Systém propíše do Bill.JIR atributu.

Pokud podání nebylo úspěšné, je potřeba zaslat fakturu do ePorezna opětovně se stejnými daty a s příznakem Indicator of subsequent invoice delivery.

## Rozhraní eFINA (elektronická faktura) (INT.BAR.32.HR)

Pokud zákazník nebo partner chce nebo musí dostávat e-faktury, Systém vytvoří dokument elektronické faktury eFaktura (DOC.BE.21.HR) v xml formátu podle standardů eFINA. V popisu dokumentu eFaktura (DOC.BE.21.HR) je přiloženo mapování struktury eFINA elektronické faktury na Billien atributy.

Systém eFakturu odešle [přes]{.mark} [eFINA]{.mark}.

Highl level popis rozhraní přiložen:

![](output_md\HR_FS_Billing_Accounts_Receivables_CZ\v00_02\media/media/image15.emf)

[Jako příloha se posílá pdf verze faktury.]{.mark}

## [Rozhraní Web portal API (INT.BAR.33.HR)]{.mark}

[TBD]{.mark}

## [Rozhraní POS API (INT.BAR.34.HR)]{.mark}

[TBD]{.mark}

## [Rozhraní KIOSK API (INT.BAR.35.HR)]{.mark}

[TBD]{.mark}

## [Rozhraní IEFBO API (INT.BAR.36.HR)]{.mark}

[TBD]{.mark}

## Rozhraní EUCARIS (INT.TDP.06)

### Rozhraní

#### Parametry

VRR -- Vehicle register record

| Název                                    | Datový Typ | Povinný`<br>`{=html}Ano/Ne | Entita        | Atribut        | Poznámka                                                                                                            |
|------------------------------------------|------------|----------------------------|---------------|----------------|---------------------------------------------------------------------------------------------------------------------|
| *Toll_VehicleTechnicalDataType*          |            | Ano                        |               |                |                                                                                                                     |
| /VehIdentificationNumber                 | String25   | Ne                         |               |                | *Nebudeme ukládat*                                                                                                  |
| /Make                                    | String52   | Ne                         | VRR           | Manufacturer   |                                                                                                                     |
| /CommercialName                          | String50   | Ne                         | VRR           | Model          |                                                                                                                     |
| /VehicleCategoryCode                     | Enum       | Ne                         | VRR           | Vehicle class  | Mapování viz Odvození Vehicle class                                                                                 |
| /ExhaustEmissionLevelEuro                | Enum       | Ne                         | VRR           | Emission class | Mapování viz Odvození Emission class                                                                                |
|                                          |            |                            |               |                |                                                                                                                     |
| *[VehicleHolderDataType]{.mark}*         |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| *[/VehHolderPersonalInformation]{.mark}* |            | [Ne (Choice)]{.mark}       | [VHRR]{.mark} |                | [When VehHolderLegalEntity='NP']{.mark}                                                                             |
| [//VehHolderSurname]{.mark}              |            | [Ano]{.mark}               | [VHRR]{.mark} |                |                                                                                                                     |
| [//VehHolderForenames]{.mark}            |            | [Ne\*]{.mark}              | [VHRR]{.mark} |                | [\*Mandatory when available in national register.]{.mark}                                                           |
| [//*VehHolderOtherNames*]{.mark}         |            | [Ne\*]{.mark}              | [VHRR]{.mark} |                | [\* Mandatory when available in national register. If available, all relevant name items shall be provided.]{.mark} |
| [VehHolderMiddleName]{.mark}             |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [VehHolderOtherName]{.mark}              |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [VehHolderGenderCode]{.mark}             |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [VehHolderDateOfBirth]{.mark}            |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [VehHolderPlaceOfBirth]{.mark}           |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
|                                          |            |                            |               |                |                                                                                                                     |
| [/VehHolderCompanyName]{.mark}           |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderLegalEntity]{.mark}           |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderCompanyIdentification]{.mark} |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrStreetName ]{.mark}       |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrStreetNameExtra ]{.mark}  |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrNumber ]{.mark}           |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrNrAnnex]{.mark}           |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrPostcode]{.mark}          |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrPlaceOfResidence]{.mark}  |            |                            | [VHRR]{.mark} |                |                                                                                                                     |
| [/VehHolderAddrCountryCode]{.mark}       |            |                            | [VHRR]{.mark} |                |                                                                                                                     |

: Tabulka 61: Parametry rozhraní INT.TDP.06