#!/opt/homebrew/bin/python3
import argparse
import base64
import subprocess
import sys
import time


APP_NAME = "Macs Fan Control"
DOMAIN = "com.crystalidea.macsfancontrol"


def preset_auto() -> str:
    return "Predefined:0"


def preset_fixed_rpm(rpm: int) -> str:
    payload = f"UNSAVED|1,{rpm}".encode("utf-8")
    encoded = base64.b64encode(payload).decode("ascii")
    return f"Unsaved:{encoded}"


def write_active_preset(value: str) -> None:
    subprocess.run(["defaults", "write", DOMAIN, "ActivePreset", value], check=True)


def read_active_preset() -> str:
    process = subprocess.run(
        ["defaults", "read", DOMAIN, "ActivePreset"],
        check=False,
        capture_output=True,
        text=True,
    )
    if process.returncode != 0:
        return ""
    return process.stdout.strip()


def hide_app() -> None:
    script = f'''
tell application "System Events"
  if exists process "{APP_NAME}" then
    set visible of process "{APP_NAME}" to false
  end if
end tell
'''
    subprocess.run(
        ["osascript", "-e", script],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def restart_app() -> None:
    subprocess.run(
        ["killall", APP_NAME],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(0.8)
    subprocess.run(
        ["open", "-gj", "-a", APP_NAME],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2.5)
    hide_app()


def describe_active_preset(value: str) -> str:
    if value == "Predefined:0":
        return "auto"
    if value.startswith("Unsaved:"):
        encoded = value.split(":", 1)[1]
        try:
            decoded = base64.b64decode(encoded).decode("utf-8")
        except Exception:
            return value
        parts = decoded.split("|", 1)
        if len(parts) != 2:
            return decoded
        mode = parts[1]
        if mode.startswith("1,"):
            return f"fixed {mode.split(',', 1)[1]}"
        return decoded
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Headless CLI bridge for Macs Fan Control")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="Show current active preset")
    subparsers.add_parser("auto", help="Restore automatic control")

    fixed = subparsers.add_parser("fixed", help="Apply a fixed RPM")
    fixed.add_argument("rpm", type=int, help="Target RPM")

    raw = subparsers.add_parser("raw", help="Write a raw ActivePreset string")
    raw.add_argument("value", help="Raw ActivePreset value")

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.command == "status":
        print(describe_active_preset(read_active_preset()))
        return 0

    if args.command == "auto":
        value = preset_auto()
    elif args.command == "fixed":
        if args.rpm <= 0:
            print("rpm must be positive", file=sys.stderr)
            return 2
        value = preset_fixed_rpm(args.rpm)
    else:
        value = args.value

    write_active_preset(value)
    restart_app()
    print(value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
