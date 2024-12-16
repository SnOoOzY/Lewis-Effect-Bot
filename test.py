import randfacts
import asyncio

def testFacts():
    x = randfacts.get_fact()
    print(x)

testFacts()