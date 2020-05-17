from click.testing import CliRunner

from testing.lpblocks.signon import hello


def test_hello_world():

    runner = CliRunner()
    result = runner.invoke(hello, ['--opt', 'An Option', 'An Arg'])
    assert result.exit_code == 0
    assert result.output == 'Opt: An Option  Arg: An Arg\n'

    result = runner.invoke(hello, ['An Arg'])
    assert result.exit_code == 0
    assert result.output == 'Opt: None  Arg: An Arg\n'


if __name__ == '__main__':
    test_hello_world()
