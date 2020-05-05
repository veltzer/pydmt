.PHONY: all

all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pydmt tests
	@pyflakes pydmt tests
	@pytest tests -qq > /dev/null
