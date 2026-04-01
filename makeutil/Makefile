.DEFAULT_GOAL := help

# Проверка переменной вынесена в отдельный блок, чтобы не дублировать код
check-variable:
ifndef PRACTICE
	$(error Внимание: нужно передать значение переменной PRACTICE, например: make create-practice PRACTICE=my_folder)
endif

create-practice: check-variable
	@echo "Creating practice directory: $(PRACTICE)"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice: check-variable
	@echo "Removing practice directory: $(PRACTICE)"
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"

#mkdir demo-practice
#mkdir demo-practice/src
#mkdir demo-practice/tests
#mkdir demo-practice/docs
#touch demo-practice/README.md
