
# Get rid of stale files or files made during testing.
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*~' -print0 | xargs -0 rm -f

# Check for simple mistakes
pyflakes:
	pyflakes GitKraken

# Check for coding standard violations.
pep8:
	find . -name '*.py' -print0 | xargs -0 ./scripts/pep8.py --ignore E221,E222
	find . -name '*.py' -print0 | xargs -0 ./scripts/pep8.py --ignore E221,E222 --repeat | wc -l

# Check for coding standard violations and simple mistakes.
lint: pyflakes pep8

.PHONY: check lint pyflakes pep8 clean

#Ignore the exit code in pyflakes, so that pep8 is always run when "make lint"
.IGNORE: pyflakes
