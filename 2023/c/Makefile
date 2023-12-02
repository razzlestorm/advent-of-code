build:
	@read -p "Enter day: " file; \
	gcc $$file.c -o $$file

clean:
	ls | grep -P "^[0-9]+$$" | xargs -d "\n" rm
