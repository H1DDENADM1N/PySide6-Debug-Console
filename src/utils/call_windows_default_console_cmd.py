import subprocess
from pathlib import Path

__Current_Script_Path__ = Path(__file__).resolve()
__Project_Root__ = __Current_Script_Path__.parent.parent.parent
__Python_Path__ = __Project_Root__ / ".venv" / "Scripts" / "python.exe"
__Script_Path__ = __Project_Root__ / "src" / "utils" / "rich_showoff.py"


def call_windows_default_console_cmd() -> int:
    """
    在 Windows 默认命令行窗口运行 rich_showoff.py
    """
    return subprocess.call(
        [
            str(__Python_Path__),
            str(__Script_Path__),
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )


if __name__ == "__main__":
    return_code = call_windows_default_console_cmd()
    print(return_code)  # 0: success !0: error
