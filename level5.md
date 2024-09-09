## level 5

this level is a python coding best practices
we will use venv,logger and validators.
i do have experience with venv and logger, but not with validators.
so lets see what will happend.


### progress

created a venv for both parts of the code
installed the packages validators and python-dotenv
used:

```bash
pip freeze > requirements.txt
```

to create a requirements file

next we did part 1 which invloved using env variables and validators

it is important to run the code from the venv terminal, cus the "local" ide iterpreter will not find the installed packages.

nothing too complicated

next for part 2 , we were asked to do a logger that changed based on the original env.py
for simplicity i just copied the env.py to part2.py

than we can see the logger wont show debug messages when the env is set to production

### to do
run the level 3 code, with .env variables and a logger
that will output depend on the ENV variable
and i want to capture the output to a file, so i can see the output of the logger

