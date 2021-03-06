from argparse import ArgumentParser


class ArgsParser:
    @staticmethod
    def parse():
        parser = ArgumentParser()

        parser.add_argument('-g', '--geo', dest='Geo id', type=int, default=1, help='Region id')

        parser.add_argument('-r', '--rubric', dest='Rubric id', type=int, default=1, help='Rubric id')

        args = parser.parse_args()
        return args
