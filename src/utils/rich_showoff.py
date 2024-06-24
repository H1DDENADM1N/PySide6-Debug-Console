import asyncio
from datetime import datetime

from rich import print
from rich.progress import Progress
from rich.table import Table

# 打印带样式的文本
print("[bold red]Hello[/bold red] [green]World![/green]")


# 显示一个表格
def display_table():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table = Table()
    table.add_column("Date", style="magenta")
    table.add_column("Time", justify="right", style="cyan")
    table.add_row(current_time.split()[0], current_time.split()[1])
    print(table)


# 使用进度条
# def show_progress():
#     for _ in track(range(100), description="Processing..."):
#         # 模拟一些处理过程
#         time.sleep(0.01)


# 使用进度条
async def show_progress(progress: Progress, name: str, sleep_time: float):
    task = progress.add_task(f"[cyan]Processing {name} ...", total=100)
    for _ in range(100):
        await asyncio.sleep(sleep_time)
        progress.update(task, advance=1)


def raise_error():
    raise ValueError("Something went wrong!")


# 主函数
async def main():
    display_table()
    progress = Progress()
    progress.start()
    await asyncio.gather(
        show_progress(progress, "Task 1", 0.01),
        show_progress(progress, "Task 2", 0.02),
        show_progress(progress, "Task 3", 0.03),
    )
    progress.stop()
    print("[bold green]Progress done.[/bold green]")
    # raise_error()


# 程序入口
if __name__ == "__main__":
    asyncio.run(main())
