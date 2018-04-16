'''cli for the swarpy client'''

import click

# profiles import group
from .profiles import get_profile


@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.argument('user_id')
@click.option('-g', '--get','action', flag_value='GET',default=True)
@click.pass_context
def profile(ctx,user_id,action):
    if action == 'GET':
        click.echo(get_profile(user_id))
    else:
        ctx.get_help()
