#!/usr/bin/env python3
"""Inject classic Bukkit plugin.yml into an official MCKotlin-Paper jar."""

from __future__ import annotations

import argparse
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_PLUGIN_YML = ROOT / "plugin.yml"


def patch(src: Path, dst: Path, plugin_yml: Path) -> None:
    yml = plugin_yml.read_bytes()
    if not yml.strip():
        raise SystemExit(f"empty plugin.yml: {plugin_yml}")

    shutil.copy2(src, dst)
    # zipfile cannot replace cleanly in-place; rebuild via temp members
    tmp = dst.with_suffix(dst.suffix + ".tmp")
    with zipfile.ZipFile(dst, "r") as zin, zipfile.ZipFile(
        tmp, "w", compression=zipfile.ZIP_DEFLATED
    ) as zout:
        for info in zin.infolist():
            if info.filename == "plugin.yml":
                continue
            zout.writestr(info, zin.read(info.filename))
        zout.writestr("plugin.yml", yml)
    tmp.replace(dst)

    with zipfile.ZipFile(dst, "r") as z:
        names = z.namelist()
        if "plugin.yml" not in names:
            raise SystemExit("patch failed: plugin.yml missing")
        if "paper-plugin.yml" not in names:
            raise SystemExit("unexpected jar: paper-plugin.yml missing")
        print(z.read("plugin.yml").decode("utf-8", "replace"))
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "input_jar",
        type=Path,
        help="Official MCKotlinPaper-*.jar (Paper-only metadata)",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output path (default: <input>-bukkit.jar)",
    )
    p.add_argument(
        "--plugin-yml",
        type=Path,
        default=DEFAULT_PLUGIN_YML,
        help="plugin.yml to inject",
    )
    args = p.parse_args()
    src = args.input_jar
    if not src.is_file():
        raise SystemExit(f"not found: {src}")
    dst = args.output or src.with_name(src.stem + "-bukkit.jar")
    patch(src, dst, args.plugin_yml)


if __name__ == "__main__":
    main()
