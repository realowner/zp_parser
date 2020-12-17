from argparse import ArgumentParser


class ArgsParser:
    @staticmethod
    def parse():
        parser = ArgumentParser()

        parser.add_argument('-g', '--geo', dest='geo_id', type=int, help='Region id')
        parser.add_argument('-r', '--rubric', dest='rubric_id', type=int, help='Rubric id')

        args = parser.parse_args()
        return args
