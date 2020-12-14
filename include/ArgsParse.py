from argparse import ArgumentParser


class ArgsParser:
    @staticmethod
    def parse():
        parser = ArgumentParser()

        parser.add_argument('-r', '--region', dest='Region id', type=int, default=1,
                            help='Идентификатор региона')

        args = parser.parse_args()
        return args
