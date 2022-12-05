# test-task
Test task for middle qa position in futura groupe

For run this pproject you need to have preintalled `python`

After cloning the repo you need to create venv for project by 
```
pip install virtualenv #if you don't already have virtualenv installed
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To see [allure](https://docs.qameta.io/allure/) reports you need to intall it separetly 

After that create directory for reports `alluress for ex.`

To run test use `pytest -s -v --alluredir=allureress tests/`

And finally to see report results `allure serve .\alluress\`
