"""
Pass click options as Environment variables.
So the same script called here can be used from ci/cd 
with variables injected by the pipeline instead of cli parameters.
"""

import click
import os
import subprocess


A_DEFAULT_1 = "O1"
"""
Sensible default for one
"""

B_DEFAULT_2 = "02"
"""
Sensible default for two
"""

COMMAND = "env"
"""
The command to execute
"""


def print_options(param, ctx, value):
    """
    Click callback to output option values before running
    """
    print(ctx.opts[0], "=", value)
    return value


@click.command()
@click.option(
    "--option_1",
    "-1",
    default=A_DEFAULT_1,
    callback=print_options,
    show_default=True,
    help="A default 1",
)
@click.option(
    "--option_2",
    "-2",
    default=B_DEFAULT_2,
    callback=print_options,
    show_default=True,
    help="B default 2",
)
def this_command(**kwargs):
    """
    Run command
    """

    def export_all_params():
        "Export click options as environment variables"
        for key, value in kwargs.items():
            os.environ[key.upper()] = value

    export_all_params()

    subprocess.call(COMMAND)


this_command()
