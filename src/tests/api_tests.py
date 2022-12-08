import time
import unittest

from engine import get_documents_langs


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestEngineApi(Test):
    def _get_langs(self, coef):
        string = "The cat (Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated " \
            "species in the family Felidae and is commonly referred to as the domestic cat or house cat to distinguish it " \
            "from the wild members of the family.[4] A cat can either be a house cat, a farm cat, or a feral cat; the latter" \
            " ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their " \
            "ability to kill rodents. About 60 cat breeds are recognized by various cat registries." \

        document = string
        for _ in range(1, coef):
            document += string

        start = time.time()
        get_documents_langs(document)
        end = time.time()

        perf_time = end - start
        print(f"The elapsed time for {coef} case is {perf_time} seconds")

    def test_create_construction_incorrect_arguments(self):
        for i in range(0, 11):
            self._get_langs(i)


test_cases = (
    TestEngineApi,
)
