import click
import sys

@click.command()
@click.option('--opt')
@click.argument('arg')
def hello(arg, opt):
    click.echo('Opt: {}  Arg: {}'.format(opt, arg))


if __name__ == '__main__':
    hello(sys.argv[1:])
