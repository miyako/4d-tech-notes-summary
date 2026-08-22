# Tech Note 10-24: Troubleshooting PHP Scripts for 4D

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** August 5, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76152
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_24-28_(AUG)/10-24_PHP_Troubleshooting.zip

## Proposition
Timothy Aaron Penner's Tech Note is a hands-on troubleshooting guide for developers running into problems with PHP scripts inside 4D v12.

## Key Points
- PHP GET FULL RESPONSE surfaces detailed PHP error output from inside 4D
- Documents installing a standalone PHP CLI interpreter for troubleshooting outside 4D
- Covers specific installation error fixes (missing oci.dll, SNMP module load failures)
- Explains PHP CLI diagnostic flags: -f, -l (lint), -i, -m, -s, -v
- Includes an example database for hands-on practice executing and debugging PHP scripts

## Featured Technology
- PHP GET FULL RESPONSE command
- PHP command-line interpreter (-f, -l, -i, -m, -s, -v flags)
- PHP script debugging inside and outside 4D

## Best Practices Highlighted
- Use -l (lint) to syntax-check a PHP script before executing it
- Reproduce failures outside 4D with the standalone CLI to isolate 4D-specific vs. PHP-specific issues

## Context/Positioning
Published to help 4D v12 developers work through the practical friction of debugging PHP integration, a then-new and relatively unfamiliar capability for many 4D developers.

## Historical Commentary
**Status:** Deprecated

This note's guidance on debugging PHP scripts both inside 4D (via PHP GET FULL RESPONSE) and outside 4D (via the standalone PHP CLI) targeted 4D's now-discontinued built-in PHP interpreter. 4D removed the built-in PHP interpreter in v20 R3 and formally deprecated the entire PHP command set in v21, recommending System Workers for running external scripts instead, so this troubleshooting workflow no longer matches how PHP integration is done in current 4D.
