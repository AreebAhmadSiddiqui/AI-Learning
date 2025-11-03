# Prompts

- Prompt are the input , instructions or query that we give the model to get an output

## Types of prompts

### 1. Static Prompts

- Ye jo normal query to llm ko bhejte ho

### 2. Dynamic Prompts

- Ismein to ek template prepare karke rakhte ho aur usmein variable inject karte ho
- Dekho bhai agar user dalega prompt to wo to kuch bhi daal sakta hai 
- Instead usse neccessary information ya varibales le lo baaki ham ek detailed prompt banaenge wo bhejna chat model ko

## Note

- Why use prompttemplate why can't we use f strings??

    - you can use f strings as well
    - But pt provides ( validation (over inputs , any extra input), tightly coupled with the langchain ecosystem, reusable)