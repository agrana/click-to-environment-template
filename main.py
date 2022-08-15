"""
Pass click options as Environment variables.
So the same script called here can be used from ci/cd 
with variables injected by the pipeline instead of cli parameters.
"""

import click
import os
import subprocess


OPTION_1 = "O1"
OPTION_2 = "02"
COMMAND = "env"


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
    default=OPTION_1,
    callback=print_options,
    show_default=True,
    help="AWS account",
)
@click.option(
    "--option_2",
    "-2",
    default=OPTION_2,
    callback=print_options,
    show_default=True,
    help="AWS account",
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
