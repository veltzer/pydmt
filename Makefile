.PHONY: all
all:
	@pylint --rcfile=.pylint.rc --reports=n --score=n pydmt tests
	@pyflakes pydmt tests
	@pytest tests -qq > /dev/null
	@python -m unittest discover -s .

.PHONY: pytest
pytest:
	@pytest tests

.PHONY: inspect
inspect:
	$(PYCHARM_HOME)/bin/inspect.sh $(PWD) .idea/inspectionProfiles/profiles_settings.xml inspections
