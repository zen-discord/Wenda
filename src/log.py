import datetime
from string import Template

from rich import print

COLORED_LEVELS = {
    "info": "[green]LOG[/green]",
    "debug": "[magenta]DEBUG[/magenta]",
    "warn": "[yellow]WARNING[/yellow]",
    "error": "[red]ERROR[/red]"
}


class Logger:
    def __init__(self,
                 process_name: str,
                 log_format: Template,
                 time_format: str) -> None:
        self.name = process_name
        self.format = log_format
        self.time_format = time_format

    def info(self, message) -> None:
        time = datetime.datetime.now().strftime(self.time_format)
        log = self.format.substitute(time=time, process=self.name, level=COLORED_LEVELS['info'],
                                     message=f'[white]{message}[/white]')
        print(f"[gray]{log}[/gray]")

    def debug(self, message) -> None:
        time = datetime.datetime.now().strftime(self.time_format)
        log = self.format.substitute(time=time, process=self.name, level=COLORED_LEVELS['debug'],
                                     message=f'[white]{message}[/white]')
        print(f"[gray]{log}[/gray]")

    def warn(self, message) -> None:
        time = datetime.datetime.now().strftime(self.time_format)
        log = self.format.substitute(time=time, process=self.name, level=COLORED_LEVELS['warn'],
                                     message=f'[white]{message}[/white]')
        print(f"[gray]{log}[/gray]")

    def error(self, message) -> None:
        time = datetime.datetime.now().strftime(self.time_format)
        log = self.format.substitute(time=time, process=self.name, level=COLORED_LEVELS['error'],
                                     message=f'[white]{message}[/white]')
        print(f"[gray]{log}[/gray]")


def get_logger(process_name: str = __name__,
               log_format: Template = Template("[$time $process] [$level] $message"),
               time_format: str = "%D/%M/%Y %H:%M:%S") -> Logger:
    return Logger(process_name, log_format, time_format)
