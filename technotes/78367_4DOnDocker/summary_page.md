# Tech Note 19-20: 4D on Docker

**Author:** Ayoub Khali, Technical Services Engineer, 4D Inc.
**Published:** December 3, 2019 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78367
**Download:** https://kb.4d.com/DLTN/TN/2019/19-20_4DonDocker.pdf

## Proposition
Docker had become a DevOps staple by 2019 for its consistency, portability, and resource efficiency versus full virtual machines. This note introduces Docker fundamentals and walks through containerizing a 4D Server deployment, positioning containers as a viable production deployment option for 4D.

## Key Points
- **Docker engine architecture**: the `dockerd` daemon/server, a REST API for management, and a CLI client that sends commands to the daemon.
- **Docker registries**: public (Docker Hub) or private repositories storing images, used via `docker pull`/`push`/`run`.
- **Image/container/volume lifecycle**: read-only layered images (from a registry or a `Dockerfile`) spawn one or more runnable containers; volumes persist data independently of a container's writable layer/lifecycle.
- **4D-specific prerequisites**: remove startup GUI windows/dialogs, pre-register licenses (an embedded-license standalone server build is recommended), and — only if GUI display is truly needed — add a VNC server inside the container paired with a host-side VNC client, or an X Server setup.
- **Demo build steps**: write a Dockerfile (Step 1), build an image from it (Step 2), and run a container from that image (Step 3), then introduce volumes for persistent 4D Server data.
- **Sharing images**: images can be distributed via Docker Hub or exported/imported directly.

## Featured Technology
- Docker (images, containers, volumes, Dockerfile, Docker Hub)
- 4D Server standalone/embedded-license builds
- VNC / X Server (for GUI-in-container scenarios)

## Best Practices Highlighted
1. Use an embedded-license standalone 4D Server build to avoid interactive license-registration prompts inside a headless container.
2. Remove any startup windows/dialogs from the database, since containers don't display a GUI by default.
3. Use volumes rather than the container's writable layer for 4D Server data, keeping containers lightweight and data persistent across container recreation.

## Context / Positioning
This note reflects 4D extending its deployment story into the containerization/DevOps space that had already reshaped much of the broader software industry, aimed at teams wanting to deploy 4D Server with the same consistency, automation, and cloud-native tooling benefits already common for other backend services.

## Historical Commentary
**Status:** Still relevant

Containerizing 4D Server is still a valid and, if anything, increasingly common deployment approach today, particularly given 4D's later addition of native Linux support for 4D Server — which makes truly lightweight, GUI-free Linux containers a much more natural fit than the Windows/macOS-guest-in-container approach implied by parts of this 2019 note (written before 4D Server ran natively on Linux). The general Docker concepts (images, containers, volumes, Dockerfiles) are unchanged, though specific installation steps and Docker Desktop's licensing/UX have evolved since 2019 and should be cross-checked against current Docker documentation. A team containerizing 4D Server today should also evaluate 4D Server for Linux directly, which likely simplifies much of the GUI/VNC workaround guidance in this note.
