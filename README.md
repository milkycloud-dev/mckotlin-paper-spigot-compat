# MCKotlin-Paper Spigot / Arclight compat

Unofficial drop-in patch for **[MCKotlin-Paper](https://github.com/4drian3d/MCKotlin)** so the jar loads on **Spigot**, **Arclight**, and other servers that only understand classic Bukkit `plugin.yml`.

| | |
|---|---|
| Upstream | MCKotlin-Paper **1.5.1-k2.4.0** |
| Minecraft | 1.20+ API (`api-version: 1.20`) |
| Tested on | Arclight NeoForge **1.21.1** (hybrid) |
| License | MIT (patch scripts / docs); jar = upstream + injected metadata |

---

## The problem

Official MCKotlin-Paper ships **only** `paper-plugin.yml` (Paper plugin loader).

Bukkit / Spigot / Arclight plugin loaders look for **`plugin.yml`**. Without it the plugin never registers, so Kotlin-based plugins (e.g. **ZAutoBroadcast**) fail with missing `kotlin.*` classes.

## The fix

Inject a classic Bukkit `plugin.yml` pointing at the same main class:

```yaml
api-version: '1.20'
name: MCKotlin-Paper
version: 1.5.1-k2.4.0
main: io.github._4drian3d.mckotlin.paper.PaperPlugin
description: Kotlin stdlib for Paper plugins (Bukkit/Spigot/Arclight loader compat)
load: STARTUP
author: 4drian3d
```

`paper-plugin.yml` is left intact, so Paper servers keep working.

## Install

1. Download `MCKotlinPaper-1.5.1-k2.4.0-bukkit.jar` from [Releases](../../releases).
2. Put it in `plugins/` (remove any previous MCKotlin jar).
3. Restart, or load with PlugMan after ensuring load order: **MCKotlin first**, then Kotlin plugins.
4. Confirm in logs:

```text
Loading MCKotlin-Paper v1.5.1-k2.4.0
Enabling MCKotlin-Paper v1.5.1-k2.4.0
```

Optional soft warning from dependents that do not declare `depend` / `softdepend` on MCKotlin is harmless.

## Build the patched jar yourself

```bash
# 1) Download the official MCKotlin-Paper jar from Modrinth / Hangar / upstream
# 2) Run:
python patch_mckotlin.py MCKotlinPaper-1.5.1-k2.4.0.jar -o MCKotlinPaper-1.5.1-k2.4.0-bukkit.jar
```

## Why not change ZAutoBroadcast only?

ZAB needs the Kotlin stdlib on the classpath. Patching MCKotlin once fixes every Kotlin Paper plugin on Spigot/Arclight, not just one consumer.

## Upstream

Reported to the author so this can be fixed in the official Paper artifact:

- Issue: [4drian3d/MCKotlin#125](https://github.com/4drian3d/MCKotlin/issues/125): Paper jar missing classic `plugin.yml`

This repo is a temporary workaround until upstream ships Bukkit metadata.

## Credits

- Upstream: [4drian3d / MCKotlin](https://github.com/4drian3d/MCKotlin)
- Compat patch: milkycloud-dev (NoteBuns ops)
