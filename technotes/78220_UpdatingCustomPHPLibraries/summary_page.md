# Tech Note 19-03: Updating Custom PHP Libraries used by 4D

**Author:** Timothy Aaron Penner, Technical Services Engineer, 4D Inc.
**Published:** February 28, 2019 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78220
**Download:** https://kb.4d.com/DLTN/TN/2019/19-03_BuildAndUpdatePHPEngine.pdf

## Proposition
4D bundles a PHP interpreter (updated to PHP 7.3 x64 as of this note) with only a 4D-tested subset of extensions, and adding modules to that bundled build is unsupported. This Tech Note shows developers how to compile their own custom PHP FastCGI engine from source, on both Mac and Windows, to add extensions 4D doesn't include.

## Key Points
- **Why a custom build is needed:** 4D's bundled PHP only supports specific tested modules; extra extensions require compiling PHP yourself.
- **Mac workflow:** compile external library dependencies first, then configure/`make`/`make install` PHP itself with `--enable-cgi --disable-cli` to get the FastCGI variant 4D needs.
- **Static vs. shared extensions:** use `--enable-static`/`--enable-shared` (or per-extension `shared`/`static` suffixes) to control how modules are linked.
- **Binary replacement:** the compiled `php-cgi` (Mac) or `php-cgi.exe` (Windows) must be renamed to `php-fcgi-4d`/`php-fcgi-4d.exe` and swap into 4D's package resources.
- **Windows toolchain:** requires Visual C++ 2015 or 2017 depending on PHP version, Microsoft's `php-sdk-binary-tools`, and the `phpsdk_buildtree.bat`/`phpsdk_deps.bat -u`/`buildconf.bat`/`configure.bat`/`nmake` pipeline.
- **Activating shared extensions:** done via `extension_dir` and `extension=` directives added to `php.ini` in the database's `Resources` folder.
- **Verification:** use `PHP Execute("";"phpversion";$result)` and `PHP Execute("";"get_loaded_extensions";$result)` after restarting 4D to confirm success.

## Featured Technology
- 4D's embedded PHP execution engine (`PHP Execute` command)
- PHP FastCGI (php-cgi / php-fcgi-4d)
- PHP source compilation toolchains (Unix `configure`/`make`; Windows PHP SDK/`nmake`)

## Best Practices Highlighted
1. Always compile external library dependencies before compiling PHP extensions that depend on them.
2. Disable the unused CLI SAPI (`--disable-cli`) since 4D only needs the CGI/FastCGI variant.
3. Verify the installed PHP version and loaded modules with `phpversion`/`get_loaded_extensions` after deployment.

## Context / Positioning
This note reflects 4D's practical, "meet developers where they are" approach to PHP interoperability: rather than expanding official support for every possible PHP extension, 4D documented a supported escape hatch for advanced customers who needed modules outside the default set, at a time (v17, PHP 7.3) when 4D was actively tracking newer PHP releases.

## Historical Commentary
**Status:** Partially superseded

The specific instructions here — PHP 7.3, Visual Studio 2015/2017, and the exact php-sdk-binary-tools workflow — are dated; 4D has since updated its bundled PHP engine to newer PHP major versions in later releases, and the corresponding build toolchains (newer Visual Studio versions, newer Xcode/macOS SDKs) have moved on, so these exact commands would need adaptation for a current 4D version.

That said, the core technique — compiling a custom FastCGI PHP build and substituting it for `php-fcgi-4d`/`php-fcgi-4d.exe` inside 4D's resources — remains the same general approach 4D developers would still use today if they need PHP extensions beyond the bundled set, since `PHP Execute` and 4D's PHP integration model have not fundamentally changed. Anyone following this note in 2026 should treat the version numbers and toolchain versions as illustrative rather than exact and consult current 4D documentation for the PHP version actually bundled with their 4D release.
