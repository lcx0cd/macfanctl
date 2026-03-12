# macfanctl

`macfanctl` is a small headless control bridge for `Macs Fan Control` on macOS.

[中文说明](README.zh-CN.md)

Related design note:

- [OpenClaw Capability + Billing Gateway](docs/OPENCLAW_CAPABILITY_BILLING_GATEWAY.md)

It does not click UI. It writes the `ActivePreset` preference, restarts `Macs Fan Control`
in the background, and keeps the app hidden. This lets other tools drive fan state through
a clean CLI while reusing the already-installed privileged helper.

## Why this exists

- modern SSD storage is priced like gold while a Mac mini fan is a cheap wear part
- high-temperature storage management is worth trading for a little fan life
- around `1800 RPM` on a `Mac mini` is nearly inaudible in real use
- if a near-silent fan floor protects expensive storage, that trade is rational
- `Macs Fan Control` can already write fan state on Apple Silicon Macs
- its GUI is not a good automation surface
- a tiny CLI is easier to embed in thermal controllers, menu bar apps, pets, or agents

In plain terms:

> Storage is expensive. Fans are cheap.  
> If a nearly inaudible `1800 RPM` floor can improve SSD thermal conditions by spending fan
> life instead of storage life, that is the right trade.

## Commands

```bash
macfanctl status
macfanctl auto
macfanctl fixed 1963
macfanctl raw Unsaved:VU5TQVZFRHwxLDE5NjM=
```

## Local usage

Without installing the package:

```bash
/Users/lvchuanxin/macfanctl/bin/macfanctl status
/Users/lvchuanxin/macfanctl/bin/macfanctl fixed 1963
/Users/lvchuanxin/macfanctl/bin/macfanctl auto
```

With packaging:

```bash
cd /Users/lvchuanxin/macfanctl
python3 -m pip install -e .
macfanctl status
```

## Current model

- `auto`
  - writes `Predefined:0`
- `fixed <rpm>`
  - encodes `UNSAVED|1,<rpm>` into the `ActivePreset` format used by `Macs Fan Control`
- `status`
  - decodes the current preset into a human-readable form when possible

## Requirements

- macOS
- `Macs Fan Control.app` installed in `/Applications`
- Accessibility permission for hiding the app process

## Notes

- this project currently targets single-fan `Mac mini` style setups
- it intentionally relies on `Macs Fan Control`'s existing helper instead of reverse-engineering
  the private SMC write path
- it is designed for people who would rather spend fan lifetime than cook expensive storage
