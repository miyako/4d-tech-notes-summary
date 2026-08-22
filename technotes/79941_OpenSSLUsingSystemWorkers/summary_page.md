# Tech Note 26-02: OpenSSL in 4D using System Workers

**Author:** Al Mahdi Bakkali, Technical Support Engineer, 4D Inc.
**Published:** February 27, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79941
**Download:** https://kb.4d.com/TN/2026/26-02_OpenSSL.zip

## Proposition
Generating cryptographic assets (private keys, CSRs, certificates, signed documents) is a
fundamental requirement for compliance, e-invoicing, and secure data exchange, but these
operations can take seconds to minutes and, run synchronously via `LAUNCH EXTERNAL PROCESS`,
would block the application thread and freeze the UI. This note shows how to run OpenSSL
asynchronously from 4D using `4D.SystemWorker`, keeping the interface responsive throughout.

## Key Points
- **Class-based callback pattern.** An `OpenSSLWorker` class centralizes five SystemWorker
  callbacks — `onResponse`, `onData` (incremental output), `onDataError` (stderr), `onError`
  (execution failures), and `onTerminate` (guaranteed cleanup) — using `This` for state
  management across invocations.
- **Workers, not plain processes.** `Execute_OpenSSLAsynch` checks `Process info(Current
  process).type` and, if not already a worker, self-spawns one via `CALL WORKER`, since
  asynchronous SystemWorker callbacks only fire inside a process created that way (never `New
  process`), and the method never calls `wait()` so it returns immediately.
- **Unified file-generation callback.** A single `onFileGenerated` project method handles
  completion for private keys, CSRs, certificates, and signed XML alike, converting the output
  path to a 4D `File` object and using its `platformPath` property so `SHOW ON DISK` resolves
  correctly cross-platform (Windows needs non-POSIX paths).
- **Headless CSR automation via `openssl.cnf`.** Setting `prompt = no` in the configuration file
  lets OpenSSL fill Distinguished Name fields and serial numbers from the file instead of pausing
  for interactive terminal input, which a background worker cannot provide.
- **Binary-safe XML signing.** Signed XML documents are produced with OpenSSL's `smime` command
  using `-binary` (prevents line-ending conversions that would silently invalidate the signature)
  and `-nodetach` (bundles the original content with the signature in one file).
- **Direct integration with 4D's web server.** Generated certificate/key files are copied (via
  `.copyTo()` with `fk overwrite`) to `cert.pem`/`key.pem` in the project root, and the
  `4D.WebServer` class is used to stop, reconfigure, and restart the server with HTTPS enabled.

## Featured Technology
- **`4D.SystemWorker`** — asynchronous, callback-driven wrapper around external process execution.
- **`CALL WORKER`** — required mechanism for spawning a worker process capable of firing async
  callbacks.
- **OpenSSL CLI (genrsa, req, x509, smime)** — private key, CSR, self-signed cert, and XML signing
  operations.
- **`openssl.cnf`** — configuration-driven, non-interactive Distinguished Name automation.
- **4D `File`/`Folder` objects, `platformPath`** — cross-platform file handling and `SHOW ON DISK`
  support.
- **`4D.WebServer` class** — programmatic HTTPS/HTTP server configuration using generated
  certificates.

## Best Practices Highlighted
1. *Never block on cryptographic operations* — always use SystemWorker's async callback pattern
   rather than `wait()` or legacy `LAUNCH EXTERNAL PROCESS`.
2. *Restrict private key file permissions* — chmod 600 on Unix-like systems, equivalent NTFS ACLs
   on Windows, immediately after key generation.
3. *Never commit private keys to version control* — even in private repos, since history retains
   deleted files; exclude `.key`/`.pem` via `.gitignore`.
4. *Use CA-issued certificates in production* — self-signed certificates are unacceptable for
   public-facing services due to browser trust warnings.

## Context / Positioning
Published under 4D v21 LTS (2026), this note reflects 4D's continued emphasis on modern
asynchronous primitives (`SystemWorker`) as the recommended way to integrate external
command-line tooling, and ties cryptographic infrastructure directly to 4D's built-in web server
— relevant to the compliance and e-invoicing requirements increasingly common in regulated
industries during this period.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
