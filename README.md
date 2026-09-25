<p align="center"><img src="assets/icon.png" width="128" height="128" alt="MCKotlin Paper Spigot Compat icon"></p>

<h1 align="center">MCKotlin Paper Spigot Compat</h1>

<p align="center">Unofficial patch that adds a classic Bukkit plugin.yml to the MCKotlin-Paper jar, so the Kotlin runtime loads on Spigot, Arclight and other servers without the Paper plugin loader. Tested with MCKotlin-Paper 1.5.1-k2.4.0 on Arclight NeoForge 1.21.1.</p>

<p align="center"><a href="https://github.com/milkycloud-dev/mckotlin-paper-spigot-compat/actions/workflows/release.yml"><img src="https://github.com/milkycloud-dev/mckotlin-paper-spigot-compat/actions/workflows/release.yml/badge.svg" alt="Release"></a></p>

<p align="center"><a href="#english">English</a> | <a href="#русский">Русский</a></p>

<a id="english"></a>

## English

### Problem

The official MCKotlin-Paper jar has only `paper-plugin.yml`. Bukkit, Spigot and Arclight look for `plugin.yml`, so the runtime never registers and every Kotlin plugin that needs it (ZAutoBroadcast, for example) fails with missing `kotlin.*` classes.

### Fix

`patch_mckotlin.py` copies the jar and adds this `plugin.yml`, pointing at the same main class. `paper-plugin.yml` stays, so Paper keeps using its own loader.

```yaml
api-version: '1.20'
name: MCKotlin-Paper
version: 1.5.1-k2.4.0
main: io.github._4drian3d.mckotlin.paper.PaperPlugin
load: STARTUP
author: 4drian3d
```

Patching the runtime once fixes every Kotlin plugin on the server, which is why the fix is here and not in each plugin.

### Usage

1. Download the official MCKotlin-Paper jar from [upstream](https://github.com/4drian3d/MCKotlin).
2. Run:

   ```bash
   python patch_mckotlin.py MCKotlinPaper-1.5.1-k2.4.0.jar -o MCKotlinPaper-1.5.1-k2.4.0-bukkit.jar
   ```

3. Put the result in `plugins/`, remove any other MCKotlin jar and restart. With PlugMan, load MCKotlin before the plugins that use it.
4. The log shows `Enabling MCKotlin-Paper v1.5.1-k2.4.0`. A warning from dependents that do not declare MCKotlin as a dependency is harmless.

For another upstream version, edit `version:` in `plugin.yml` and pass the file with `--plugin-yml`.

### Upstream

The missing metadata is reported as [4drian3d/MCKotlin#125](https://github.com/4drian3d/MCKotlin/issues/125). This patch is a workaround until the official jar ships a `plugin.yml`.

### Releases

A tag `v*` checks the script on GitHub Actions and publishes the patch kit (script, `plugin.yml`, README, license) with the notes from [CHANGELOG.md](CHANGELOG.md). MCKotlin itself is not part of the kit. Release `v1.5.1-k2.4.0-bukkit` holds the patched jar from the first publication.

### License

The patch script and documentation are proprietary, all rights reserved; see [LICENSE](LICENSE). MCKotlin is the work of 4drian3d and stays under its author's rights. This project is not affiliated with the author.

<a id="русский"></a>

## Русский

### Проблема

В официальном jar MCKotlin-Paper есть только `paper-plugin.yml`. Bukkit, Spigot и Arclight ищут `plugin.yml`, поэтому рантайм не регистрируется, и все плагины на Kotlin, которым он нужен (например, ZAutoBroadcast), падают без классов `kotlin.*`.

### Исправление

`patch_mckotlin.py` копирует jar и добавляет такой `plugin.yml` с тем же главным классом. `paper-plugin.yml` остаётся, так что Paper по-прежнему грузит плагин своим загрузчиком.

```yaml
api-version: '1.20'
name: MCKotlin-Paper
version: 1.5.1-k2.4.0
main: io.github._4drian3d.mckotlin.paper.PaperPlugin
load: STARTUP
author: 4drian3d
```

Один патч рантайма чинит сразу все плагины на Kotlin, поэтому исправление сделано здесь, а не в каждом плагине.

### Использование

1. Скачайте официальный jar MCKotlin-Paper у [автора](https://github.com/4drian3d/MCKotlin).
2. Выполните:

   ```bash
   python patch_mckotlin.py MCKotlinPaper-1.5.1-k2.4.0.jar -o MCKotlinPaper-1.5.1-k2.4.0-bukkit.jar
   ```

3. Положите результат в `plugins/`, уберите другие jar MCKotlin и перезапустите сервер. С PlugMan загружайте MCKotlin раньше плагинов, которые его используют.
4. В логе появится `Enabling MCKotlin-Paper v1.5.1-k2.4.0`. Предупреждение от плагинов, которые не объявили MCKotlin зависимостью, не мешает.

Для другой версии поправьте `version:` в `plugin.yml` и передайте файл через `--plugin-yml`.

### Апстрим

Отсутствие метаданных описано в [4drian3d/MCKotlin#125](https://github.com/4drian3d/MCKotlin/issues/125). Патч нужен, пока официальный jar не получит `plugin.yml`.

### Релизы

Тег `v*` проверяет скрипт в GitHub Actions и публикует набор для патча (скрипт, `plugin.yml`, README, лицензия) с описанием из [CHANGELOG.md](CHANGELOG.md). Сам MCKotlin в набор не входит. В релизе `v1.5.1-k2.4.0-bukkit` лежит патченый jar из первой публикации.

### Лицензия

Скрипт патча и документация проприетарные, все права защищены; см. [LICENSE](LICENSE). MCKotlin это работа 4drian3d, права на него остаются у автора. Проект с автором не связан.
