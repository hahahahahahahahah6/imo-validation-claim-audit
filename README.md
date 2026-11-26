# Ship-number claim audit

An offline static audit compares documented ship-number claims with Python source evidence. It does not execute the inspected code. An IMO number has seven digits; its final digit is a weighted mod-10 check digit.

```sh
imo-validation-claim-audit audit . --json
python3 -m imo_validation_claim_audit audit . --fail-on medium
```

The optional repository defaults to the current directory. Repeat `--ignore PREFIX` to omit paths. Use `--verbose` for the audited path. The default threshold is high; `--fail-on medium` also fails on test-only evidence. Exit codes are 0 for pass, 2 for findings at the threshold, and 1 for usage or I/O errors.

```text
documented-imo-validation-claim-false
documented-no-imo-validation-claim-false
```

A positive documented claim without production evidence is high severity, or medium when evidence appears only in tests. A negative claim with production evidence is high severity. A positive claim without Python files is high severity; a negative claim without Python files passes.

The scanner examines the root README and Markdown files under docs, excluding fenced blocks while counting inline code. It recognizes calls to the two judging operations in `stdnum.imo` and the specified generic named calls in a single module. Imports alone do not count. Local definitions and rebound imports shadow routes. Files under fixtures, docs, and examples do not provide source evidence; tests are considered separately.

## Differentiation

The generic validation family covers a separate capability.

The ISBN-validation family covers a separate capability.

The ISSN-validation family covers a separate capability.

The IBAN-validation family covers a separate capability.

The UUID-validation family covers a separate capability.

The semver-validation family covers a separate capability.

The MAC-address-validation family covers a separate capability.

The BIC-validation family covers a separate capability.

The cron-expression-validation family covers a separate capability.

The cron-expression-description family covers a separate capability.

The scheduled-execution family covers a separate capability.

The date-validation family covers a separate capability.

The timeout family covers a separate capability.

The payment-processing family covers a separate capability.

The credit-card-extraction family covers a separate capability.

The auth family covers a separate capability.

The password-hashing family covers a separate capability.

The password-generation family covers a separate capability.

The PDF-encryption family covers a separate capability.

The email-sending family covers a separate capability.

The SMS-sending family covers a separate capability.

The document-extraction family covers a separate capability.

The barcode-scanning family covers a separate capability.

The email-validation family covers a separate capability.

The phone-validation family covers a separate capability.

The password-strength family covers a separate capability.

The JSON-Schema-validation family covers a separate capability.

The credit-card-validation family covers a separate capability.

The domain-validation family covers a separate capability.

The URL-validation family covers a separate capability.

The IP-validation family covers a separate capability.

The JSON-parsing family covers a separate capability.

The regex family covers a separate capability.

The URL-parsing family covers a separate capability.

The URL-fetching family covers a separate capability.

The DNS family covers a separate capability.

The barcode-generation family covers a separate capability.

The account-extraction family covers a separate capability.

The VIN-extraction family covers a separate capability.

The VIN-decoding family covers a separate capability.

The VIN-history-lookup family covers a separate capability.

The hex-color-validation family covers a separate capability.

The ORCID-validation family covers a separate capability.

The ISNI-validation family covers a separate capability.

The DOI-validation family covers a separate capability.

The CASRN-validation family covers a separate capability.

The SEDOL-validation family covers a separate capability.

The ISIN-validation family covers a separate capability.

The ISIN-record-query family covers a separate capability.

The ISIN-extraction family covers a separate capability.

The CUSIP-validation family covers a separate capability.

The IMEI-validation family covers a separate capability.

The MEID-validation family covers a separate capability.

The ESN-validation family covers a separate capability.

The ISMN-validation family covers a separate capability.

The ISAN-validation family covers a separate capability.

The GRid-validation family covers a separate capability.

The EAN-validation family covers a separate capability.

The generic-serial-number family covers a separate capability.

The FIGI-validation family covers a separate capability.

The FIGI-record-query family covers a separate capability.

The FIGI-extraction family covers a separate capability.

The ISRC-validation family covers a separate capability.

The Ethereum-address-validation family covers a separate capability.

The Binance-Smart-Chain-address-validation family covers a separate capability.

The Tron-address-validation family covers a separate capability.

The Litecoin-address-validation family covers a separate capability.

The Dogecoin-address-validation family covers a separate capability.

The bitcoin-address-validation family covers a separate capability.

The transaction-hash-validation family covers a separate capability.

The private-key-validation family covers a separate capability.

The block-explorer family covers a separate capability.

The address-generation family covers a separate capability.

The address-extraction family covers a separate capability.

The payment-receipt family covers a separate capability.

The spreadsheet-reading family covers a separate capability.

The spreadsheet-generation family covers a separate capability.

The Word-reading family covers a separate capability.

The Word-generation family covers a separate capability.

The presentation-reading family covers a separate capability.

The presentation-generation family covers a separate capability.

The PDF-extraction family covers a separate capability.

The PDF-generation family covers a separate capability.

The PDF-merging family covers a separate capability.

The PDF-splitting family covers a separate capability.

The PDF-rotation family covers a separate capability.

The PDF-form-filling family covers a separate capability.

The PDF-watermarking family covers a separate capability.

The PDF-redaction family covers a separate capability.

The PDF-compression family covers a separate capability.

The PDF-annotation family covers a separate capability.

The table-extraction family covers a separate capability.

The OCR family covers a separate capability.

The document-data-extraction family covers a separate capability.

The e-signature family covers a separate capability.

The screen-recording family covers a separate capability.

The video-generation family covers a separate capability.

The QR-generation family covers a separate capability.

The audio-mixing family covers a separate capability.

The audio-generation family covers a separate capability.

The audio-editing family covers a separate capability.

The audio-source-separation family covers a separate capability.

The speech-recognition family covers a separate capability.

The speech-synthesis family covers a separate capability.

The noise-reduction family covers a separate capability.

The music-generation family covers a separate capability.

The music-transcription family covers a separate capability.

The InChI family covers a separate capability.

The SMILES family covers a separate capability.

The EC-number family covers a separate capability.

The UN-transport-number family covers a separate capability.

The PubChem-query family covers a separate capability.

The chemical-structure-validation family covers a separate capability.

The other-chemical-identifiers family covers a separate capability.

The container-number-reading family covers a separate capability.

The carrier-registry family covers a separate capability.

The BIC-shipowner-code family covers a separate capability.

The container-size-type family covers a separate capability.

The container-number-generation family covers a separate capability.

The ISO-6346-validation family covers a separate capability.

The library-record-fetching family covers a separate capability.

The library-identifier-registration family covers a separate capability.

The cataloguing family covers a separate capability.

The OCLC-WorldCat family covers a separate capability.

The library-agency-listing family covers a separate capability.

The ISIL-validation family covers a separate capability.

The IMSI-validation family covers a separate capability.

The MMSI-validation family covers a separate capability.

The HIN-validation family covers a separate capability.

The ENI-validation family covers a separate capability.

The vessel-registry-lookup family covers a separate capability.

The AIS-tracking family covers a separate capability.

The ship-name-lookup family covers a separate capability.

## Limitations

A compact call only strips spaces and the prefix and changes case.

A format call only adds a prefix.

A check-digit computation alone does not judge a complete number.

An EAN call judges a barcode number.

A Luhn call uses a different check.

A regular expression checks a pattern rather than the full library judgement.

A length check alone omits the check digit.

A digit-only check alone omits the check digit.

A prefix check or strip alone does not judge the digits.

A device identifier call concerns a different identifier.

A subscriber identity call concerns a different identifier.

A maritime mobile identity call concerns a different identifier.

A hull identification number call concerns a different identifier.

A European vessel number call concerns a different identifier.

A registry lookup retrieves a record rather than judging the string.

AIS tracking retrieves a position rather than judging the string.

The validators package does not provide the relevant route.

Strings, comments, imports and bare references do not establish a call.

Syntax errors prevent source evidence.

Calls split across modules do not combine into evidence.

A subprocess invocation does not count.

Roadmap, changelog and TODO prose can produce claims without implemented code.

The weighted check misses some single-digit changes: 9319466 and 9339466 share the check digit.

The library does not establish assignment or ship existence.

The library accepts a prefix, lowercase letters and surrounding spaces.

Hyphens and tabs are not stripped by the library.

```text
validate imo
```

The bare phrase above can describe a manual runbook step.

```text
imo validation
```

The bare phrase above can describe a roadmap feature.

```text
imo validator
```

The bare phrase above can describe a hosted web page.

```text
imo check
```

The bare phrase above can describe a field-presence lint rule.

```text
check imo
```

The bare phrase above can describe a manual runbook step.

```text
verify imo
```

The bare phrase above can describe a visual owner confirmation.

```text
imo code validation
```

The bare phrase above can describe a field-presence check.

```text
valid imo
```

The bare phrase above can appear as example output.

```text
imo is valid
```

The bare phrase above can appear as example output.

```text
imo is invalid
```

The bare phrase above can appear as example error text.

```text
imo validity
```

The bare phrase above can name a configuration flag or column.

```text
imo format validation
```

The bare phrase above can describe a format without code.

```text
validate imo number
```

The bare phrase above can describe a shape-only check.

```text
imo number validation
```

The bare phrase above can name a specification section.

```text
validate imo code
```

The bare phrase above can describe a manual runbook step.

```text
check imo code
```

The bare phrase above can describe a manual runbook step.

```text
validate imo7
```

The bare phrase above can describe a manual runbook step.

```text
imo7 validation
```

The bare phrase above can name a specification section.

```text
imo number check
```

The bare phrase above can name a fleet checklist item.

```text
imo validation
```

The bare phrase above can describe a result from an external platform.

```text
imo
```

The bare phrase above alone is not a claim and can mean in my opinion.

```text
imo number
```

The bare phrase above alone names a number without judging it.

```text
validate identifier
```

The bare phrase above does not identify the relevant number family.

```text
check digit
```

The bare phrase above alone does not claim a judgement.

```text
ship
```

The bare phrase above alone does not claim a judgement.

```text
vessel
```

The bare phrase above alone does not claim a judgement.

```text
mmsi
```

The bare phrase above names a different maritime identity.

```text
hull number
```

The bare phrase above alone does not claim a judgement.

