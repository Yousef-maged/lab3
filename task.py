name: task3
on: push
jobs:
    my-job:
        runs-on: ubuntu-latest 
        steps: 
            name: my-step
            run echo "hello"
    
