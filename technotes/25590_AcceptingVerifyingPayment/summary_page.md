# Tech Note: Accepting / Verifying Payment Information

- **Asset ID:** 25590
- **Tech Note #:** 02-49
- **Published:** October 31, 2002
- **Product / Version:** 4D Business Kit 1.x
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=25590
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_46-50_(OCT)/02-49_Accept-Verify_Payment.hqx

## Overview

Frank Chang explains how to integrate online payment acceptance into a 4D Business Kit (4DBK) e-commerce store, opening with market statistics on U.S. online shopping to motivate the need for payment processing. He describes the general payment-gateway flow (consumer -> merchant site -> gateway -> card issuer -> settlement) and the two integration models 4DBK supports: a 'direct connect' server-to-server flow where the 4DBK server itself calls out to the gateway via the `4DBKCreditCardProcess` tag/script (keeping the customer on-site throughout, but requiring an SSL certificate and costing more), versus a browser-redirect 'link' method where the customer's browser submits a form directly to the gateway's own hosted page (cheaper, simpler, but sends customers off-site temporarily). He then details the concrete configuration and code for two named gateways -- VeriSign's PayFlowPro/PayFlowLink and Authorize.net's AIM/WebLink -- including the JavaScript calling pattern, response-code variables, and required account setup for each.

## Key Points

- Diagrams the general payment-gateway transaction flow: consumer places order -> secure connection to gateway (via browser or via the 4DBK server) -> gateway forwards an authorization request to the card issuer -> issuer responds -> gateway relays result to merchant (typically under 3 seconds) -> settlement and fund transfer to the merchant account.
- Contrasts the two 4DBK integration models: direct connect (server-to-server via `4DBKCreditCardProcess`, requires a certificate, keeps customers on-site, more automated but costs more) versus the link method (browser redirects via an HTML form to the gateway's hosted page, cheaper/simpler, but customers briefly leave the site).
- VeriSign PayFlowPro: configured via login credentials in the store's Services tab, driven by a script file `US_VeriSign_PFP.txt` located in `[4DBK Root]\Services\Payments\CreditCard`, called from JavaScript using `4DBKCreditCardProcess` with 5 parameters (script file, card number, expiration, amount, currency) wrapped in `4DBKExecute`; results returned via `4DBKCreditCardCode1` (0 = approved), `4DBKCreditCardText`, and `4DBKCreditCardTID`.
- VeriSign PayFlowLink: a simpler HTML-only integration where a form's `action` attribute posts customer/order data (extracted from 4DBK tags) directly to a VeriSign-hosted checkout page, customizable to match the store's look and feel, requiring a separate VeriSign test/production account.
- Authorize.net AIM (formerly ADC Direct Response): near-identical direct-connect flow to PayFlowPro but using script file `US_AuthorizeNet_ADC.txt` and different response codes (`4DBKCreditCardCode1`=1 for approved, plus `4DBKCreditCardCode2` and `4DBKCreditCardText`); Authorize.net WebLink is the link-method equivalent of PayFlowLink.
- Notes the EncodeURL() JavaScript helper library must be included before the HTML body to safely pass values to the 4DBKCreditCardProcess tag, and that other payment gateways not covered follow a broadly similar implementation pattern.

## Featured Technology

- 4DBKCreditCardProcess / 4DBKExecute tags
- VeriSign PayFlowPro / PayFlowLink payment gateway integration
- Authorize.net AIM (Advanced Integrated Method) / WebLink
- Direct-connect vs. HTTP-redirect (link method) payment flows
- 4D Business Kit store-property payment gateway configuration
- 4DBKCreditCardCode1/Code2/Text/TID response variables

## Historical Commentary

**Status:** obsolete

Frank Chang (4D Inc. Technical Support) explains how to wire 4D Business Kit's e-commerce store into two payment gateways of the era, VeriSign and Authorize.net, contrasting a 'direct connect' server-to-server flow (using the 4DBKCreditCardProcess tag and a gateway-specific script file such as US_VeriSign_PFP.txt) against a browser-redirect 'link' method (raw HTML forms posting to the gateway's own hosted page). 4D Business Kit itself has been discontinued, and online payment processing has since been reshaped by mature PCI-DSS compliance requirements and modern hosted-checkout APIs (Stripe, PayPal, etc.) that render this note's specific implementation obsolete -- it is useful today only as a historical snapshot of how e-commerce payment integration worked in early-2000s 4D products.

References to newer/updated information:
- 4D Business Kit has been discontinued for many years
- Modern e-commerce payment processing relies on PCI-DSS-compliant hosted checkout/gateway APIs (e.g., Stripe, PayPal, Adyen) rather than the direct-connect/link-method techniques and raw credit-card-handling tags described in this note
